# src/recommender/recommendation.py

'''
Definimos el módulo principal de recomendación para cada empleado 
que utiliza el motor semántico para generar recomendaciones de cursos 
basadas en habilidades y sus descripciones.
Este módulo extrae habilidades de un DataFrame de empleados y genera recomendaciones de cursos.
'''

import pandas as pd
from typing import List
from training_recommender.engine.semantic_engine import SemanticRecommender


def extract_skills_from_employee(row: pd.Series, skill_columns: List[str]) -> List[str]:
    """
    Extrae las habilidades únicas desde múltiples columnas de un registro de empleado.
    Args:
        row (pd.Series): fila del DataFrame de empleado.
        skill_columns (List[str]): lista de nombres de columnas que contienen habilidades.
    Returns:
        List[str]: lista de habilidades únicas.
    """
    skills = []
    for col in skill_columns:
        value = row.get(col)
        if pd.notna(value) and value.strip().lower() != "none":
            skills.append(value.strip())
    return list(set(skills))  # elimina duplicados


def generate_recommendations_for_employees(employee_df: pd.DataFrame,
                                           recommender: SemanticRecommender,
                                           skill_columns: List[str],
                                           top_k_per_skill: int = 3,
                                           max_courses_per_employee: int = 5) -> pd.DataFrame:
    """
    Genera recomendaciones de cursos para cada empleado basado en sus habilidades.

    Args:
        employee_df (pd.DataFrame): base de empleados.
        recommender (SemanticRecommender): motor semántico de recomendación.
        skill_columns (List[str]): columnas que contienen habilidades.
        top_k_per_skill (int): cursos por habilidad.
        max_courses_per_employee (int): número final de cursos recomendados por empleado.

    Returns:
        pd.DataFrame: el mismo DF de empleados con columna 'recommended_courses'.
    """
    recommendations = []

    for _, row in employee_df.iterrows():
        skills = extract_skills_from_employee(row, skill_columns)
        seen_courses = set()
        employee_courses = []

        for skill in skills:
            recs = recommender.recommend(skill, top_k=top_k_per_skill)
            for rec in recs:
                if rec["course_title"] not in seen_courses:
                    seen_courses.add(rec["course_title"])
                    employee_courses.append(rec["course_title"])
                if len(employee_courses) >= max_courses_per_employee:
                    break
            if len(employee_courses) >= max_courses_per_employee:
                break

        recommendations.append(", ".join(employee_courses))

    employee_df = employee_df.copy()
    employee_df["recommended_courses"] = recommendations
    return employee_df
