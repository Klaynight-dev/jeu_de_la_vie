# jdlv_utils.py

from seed import *
from jdlv_utils import *
import tkinter as tk

class Cellule:
    def __init__(self, etat=False):
        self.etat = etat  # False pour morte, True pour vivante

    def est_vivant(self):
        return self.etat

    def mourir(self):
        self.etat = False

    def naitre(self):
        self.etat = True


class Grille:
    def __init__(self, taille, grille_initiale=None):
        self.taille = taille
        if grille_initiale is None:
            self.grille = np.empty((self.taille, self.taille), dtype=object)
            for i in range(self.taille):
                for j in range(self.taille):
                    self.grille[i][j] = Cellule()
        else:
            self.grille = grille_initiale

    def compter_voisins_vivants(self, ligne, colonne):
        voisins_vivants = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and 0 <= ligne + i < self.taille and 0 <= colonne + j < self.taille:
                    if self.grille[ligne + i][colonne + j].est_vivant():
                        voisins_vivants += 1
        return voisins_vivants

    def mettre_a_jour(self):
        nouvelle_grille = np.empty((self.taille, self.taille), dtype=object)

        for i in range(self.taille):
            for j in range(self.taille):
                cellule_courante = self.grille[i][j]
                nb_voisins = self.compter_voisins_vivants(i, j)

                if cellule_courante.est_vivant():
                    if nb_voisins < 2 or nb_voisins > 3:
                        nouvelle_grille[i][j] = Cellule(False)
                    else:
                        nouvelle_grille[i][j] = Cellule(True)
                else:
                    if nb_voisins == 3:
                        nouvelle_grille[i][j] = Cellule(True)
                    else:
                        nouvelle_grille[i][j] = Cellule(False)

        self.grille = nouvelle_grille