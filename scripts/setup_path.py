# scripts/setup_path.py

import os
import sys

def add_src_to_path():
    """
    Agrega la carpeta 'src/' al sys.path si no está incluida aún.
    Esto permite importar módulos como 'from recommender.engine import ...'
    desde scripts o notebooks que estén fuera del módulo.
    """
    src_path = os.path.abspath("src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
