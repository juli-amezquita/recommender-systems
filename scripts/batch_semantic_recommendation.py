# scripts/batch_semantic_recommendation.py

import sys
import os
sys.path.append(os.path.abspath("src"))

from setup_path import add_src_to_path
add_src_to_path()

from training_recommender.engine.semantic_engine import SemanticRecommender
from training_recommender.recommendation import generate_recommendations_for_employees
import pandas as pd
import numpy as np
import os

# Configuración
COURSE_PATH = "data/processed/2_en_courses_9categories.csv"
EMPLOYEE_PATH = ".secrets/1_employee_dataset_new.csv"
OUTPUT_DIR = "outputs/batches"
BATCH_SIZE = 500
MODEL_NAME = "all-MiniLM-L6-v2"

# Columnas de habilidades a evaluar
skill_columns = [
    "succession_plan_skill_1", "succession_plan_skill_2", "succession_plan_skill_3",
    "performance_measure_skill_1", "performance_measure_skill_2", "performance_measure_skill_3",
    "position_skill_1", "position_skill_2", "position_skill_3",
    "corporate_skill_1", "corporate_skill_2"
]

# Cargar datos
df_courses = pd.read_csv(COURSE_PATH)
df_employees = pd.read_csv(EMPLOYEE_PATH)

# Instanciar recomendador semántico
recommender = SemanticRecommender(model_name=MODEL_NAME)

# Precalcular embeddings y cargarlos
course_embeddings_path = "outputs/course_embeddings.npy"

# Asegurarse de que la carpeta 'outputs' exista
# Extraer el directorio del path del archivo
output_dir_for_embeddings = os.path.dirname(course_embeddings_path)
if output_dir_for_embeddings and not os.path.exists(output_dir_for_embeddings):
    os.makedirs(output_dir_for_embeddings)
    print(f"Directorio creado: {output_dir_for_embeddings}")

if os.path.exists(course_embeddings_path):
    print("Cargando embeddings precalculados...")
    recommender.course_embeddings = np.load(course_embeddings_path)
    recommender.course_df = df_courses
else:
    print("Calculando embeddings de cursos...")
    recommender.fit(df_courses, text_column="Summary")
    np.save(course_embeddings_path, recommender.course_embeddings)

# Dividir en lotes y procesar
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

n_batches = int(np.ceil(len(df_employees) / BATCH_SIZE))

print(f"Procesando {len(df_employees)} empleados en {n_batches} lotes...")

for i in range(n_batches):
    batch_start = i * BATCH_SIZE
    batch_end = min((i + 1) * BATCH_SIZE, len(df_employees))
    df_batch = df_employees.iloc[batch_start:batch_end]

    output_path = f"{OUTPUT_DIR}/recommendations_batch_{i+1:02d}.csv"
    if os.path.exists(output_path):
        print(f"✅ Lote {i+1} ya procesado, saltando...")
        continue

    print(f"🔄 Procesando lote {i+1}/{n_batches}...")

    df_result = generate_recommendations_for_employees(
        df_batch, recommender, skill_columns, top_k_per_skill=3 
    )

    df_result.to_csv(output_path, index=False)
    print(f"✅ Guardado: {output_path}")

print("\n Todos los lotes han sido procesados.")
