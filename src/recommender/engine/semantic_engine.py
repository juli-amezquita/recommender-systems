# src/recommender/engine/semantic_engine.py

'''
Creamos un primer módulo base para el sistema de recomendación con embeddings semánticos.
Este módulo utiliza Sentence Transformers para generar embeddings de cursos y habilidades,
y luego calcula similitudes para recomendar cursos relevantes.
'''

from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch


class SemanticRecommender:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        '''
        Inicializa el recomendador semántico con un modelo preentrenado.
        Args:
            model_name (str): nombre del modelo de Sentence Transformers a usar.
        '''
        self.model = SentenceTransformer(model_name) # Cargamos el modelo preentrenado
        self.course_embeddings = None # Embeddings de los cursos
        self.course_df = None # DataFrame de cursos

    def fit(self, course_df: pd.DataFrame, text_column: str = "Summary"):
        """
        Genera embeddings para la base de cursos.
        Args:
            course_df (pd.DataFrame): DataFrame con los cursos y sus descripciones.
            text_column (str): columna con los resúmenes o descripciones.
        """
        self.course_df = course_df.dropna(subset=[text_column]).reset_index(drop=True)
        self.course_embeddings = self.model.encode(
            self.course_df[text_column].tolist(),
            convert_to_tensor=True
        )

    def recommend(self, skill: str, top_k: int = 5):
        """
        Retorna los top_k cursos más cercanos semánticamente a una habilidad.
        Args:
            skill (str): nombre de la habilidad a buscar.
            top_k (int): número de recomendaciones.
        Returns:
            list[dict]: lista de cursos recomendados con título, score, link, etc.
        """
        if self.course_embeddings is None:
            raise ValueError("Debes llamar a `fit()` antes de usar `recommend()`.")

        skill_embedding = self.model.encode(skill, convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(skill_embedding, self.course_embeddings)[0]
        top_results = torch.topk(cosine_scores, k=top_k)

        results = []
        for score, idx in zip(top_results[0], top_results[1]):
            course = self.course_df.iloc[int(idx)]
            results.append({
                "course_title": course.get("Title"),
                "score": float(score),
                "category": course.get("Category"),
                "link": course.get("Link")
            })
        return results
