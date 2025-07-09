# 🧠 Sistema Recomendador de Cursos para Planes de Formación en Empresas

> Proyecto de tesis de maestría en Visual Analytics and Big Data
Universidad Internacional de La Rioja (UNIR)

## 📝 Descripción general
Este proyecto implementa un sistema de recomendación de cursos personalizados para empleados de una empresa, basado en información realista sobre sus posiciones, habilidades requeridas, desempeño, plan de sucesión, y estrategia corporativa. Utiliza técnicas modernas de análisis semántico con embeddings, NLP, modelado temático (LDA), y modelos basados en TF-IDF, todo desarrollado en Python con una arquitectura modular, reproducible y escalable.


## 🔍 Objetivo
El objetivo es ayudar a los equipos de Talento Humano a construir planes de desarrollo personalizados a través de recomendaciones formativas relevantes, alineadas con la estrategia del negocio.


## 📌 ¿Por qué este proyecto es relevante?
* Integra datos organizacionales reales en el diseño de algoritmos de recomendación.
* Enfocado en Recursos Humanos y desarrollo de talento, un área aún poco explorada con sistemas recomendadores personalizados.
* Útil para áreas de People Analytics, HR Tech, L&D y Talent Management.

## 🗂️ Estructura del proyecto

```bash
recommender-systems/
│
├── data/                         # Datos de entrada
│   ├── processed/                # CSV procesados para uso del modelo
│   │   ├── 1_employee_dataset_new.csv        # Dataset de empleados (privado)
│   │   └── 2_en_courses_9categories.csv      # Dataset de cursos de Udemy (público)
│   └── raw/                      # Datos sin procesar
│       └── datasets_udemy/      # Otros archivos originales de cursos
│
├── docs/                         # Documentos académicos y presentaciones  # Licencia CC-BY-NC 4.0
│   ├── 0_ppt_Sistema_Recomendador_TFM.pdf
│   └── 0_TFM_Juliana_Andrea_Amezquita_Abello.pdf
│
├── notebooks/                   # Exploraciones y prototipos en Jupyter
│   ├── Análisis_Exploratorio_dataset_cursos.ipynb
│   ├── Análisis_Exploratorio_Dataset_Empleados_F.ipynb
│   └── Modelo_Sistema_Recomendador_F_v2022.ipynb
│
├── scripts/                     # Scripts ejecutables
├── src/                         # Código fuente del motor recomendador
│   └── recommender/
│       ├── data/                # Futuro: carga o procesamiento de datos
│       ├── engine/              # Motores de recomendación (TF-IDF, LDA, embeddings)
│       ├── interface/           # Futuro: interfaz o integraciones (ej. APIs o Streamlit)
│       ├── recommendation.py    # Lógica principal de recomendación
│       └── __init__.py
│
├── .gitignore                   # Archivos excluidos del control de versiones
├── LICENSE                      # Apache 2.0
├── poetry.lock                  # Lockfile de dependencias
├── pyproject.toml               # Configuración del proyecto con Poetry
└── README.md                    # Este archivo
```

## 🧪 Tecnologías y librerías utilizadas
* Python 3.10
* Poetry para gestión de entorno y dependencias
* sentence-transformers para embeddings semánticos
* scikit-learn, pandas, numpy, matplotlib, seaborn
* gensim para modelado LDA
* NLTK, spaCy, re para NLP clásico
* Power BI y Streamlit para posibles visualizaciones
* JupyterLab para exploración y prototipado

## ⚙️ ¿Cómo ejecutar el proyecto?

1. Clonar el repositorio:

```bash
git clone https://github.com/juli-amezquita/recommender-systems.git
cd recommender-systems
```

2. Instalar las dependencias:

```bash
poetry install
````

3. Asegúrate de subir manualmente el archivo privado:

```bash
data/private/1_employee_dataset_new.csv
````
> ⚠️ Nota: recuerda que debes colocar el archivo 1_employee_dataset_new.csv dentro de data/processed/ (este archivo está excluido por .gitignore y no es público).

4. Ejecutar las recomendaciones:


## 📡 Estado actual
* ✅ Motores de recomendación (TF-IDF, LDA, embeddings)
* ✅ Recomendaciones personalizadas por empleado
* ✅ Estructura modular compatible con producción
* 🚧 Integración con Coursera/edX APIs (pendiente)
* 🚧 Visualización interactiva (posible Streamlit o Power BI)

## 📄 Documentación académica
Los siguientes documentos corresponden a la tesis y presentación final del proyecto:
* `docs/0_TFM_Juliana_Andrea_Amezquita_Abello.pdf`
* `docs/0_ppt_Sistema_Recomendador_TFM.pdf`

Licencia: Creative Commons BY-NC 4.0
(Permite compartir y adaptar, siempre que no sea con fines comerciales)

## 🔐 Licencia
El código está licenciado bajo Apache 2.0, lo que permite su uso libre siempre que se incluya la atribución correspondiente.
Los documentos contenidos en la carpeta `docs/` (incluyendo la tesis y presentaciones) están licenciados bajo **Creative Commons BY-NC 4.0**, lo que prohíbe su uso con fines comerciales sin autorización previa.

## 👩🏼‍🦱 Autora
Juliana Amézquita Abello\
Gerente de Reclutamiento | Consultora en People Analytics y HR Tech\
Especializada en soluciones basadas en datos para RRHH\
📍 Colombia\
🔗 [LinkedIn](https://www.linkedin.com/in/juliana-amezquita/)
