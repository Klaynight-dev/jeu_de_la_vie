# seed.py
import numpy as np
from main import Cellule  # Importez la classe Cellule depuis main.py si nécessaire

def generer_grille_initiale(taille):return np.array([[Cellule(np.random.choice([False, True])) for _ in range(taille)] for _ in range(taille)])