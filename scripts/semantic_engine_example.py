from training_recommender.engine.semantic_engine import SemanticRecommender
from training_recommender.recommendation import generate_recommendations_for_employees
import pandas as pd

# Cargar los datos
df_courses = pd.read_csv("data/processed/2_en_courses_9categories.csv")
df_employees = pd.read_csv(".secrets/1_employee_dataset_new.csv")

# Instanciar y entrenar el motor semántico
recommender = SemanticRecommender()
recommender.fit(df_courses, text_column="Summary")

# Definir columnas de skills
skill_columns = [
    "succession_plan_skill_1", "succession_plan_skill_2", "succession_plan_skill_3",
    "performance_measure_skill_1", "performance_measure_skill_2", "performance_measure_skill_3",
    "position_skill_1", "position_skill_2", "position_skill_3",
    "corporate_skill_1", "corporate_skill_2"
]

# Generar recomendaciones
df_final = generate_recommendations_for_employees(df_employees, recommender, skill_columns)

# Guardar el resultado para Power BI, Excel o visualización
df_final.to_csv("outputs/employees_with_recommendations.csv", index=False)
