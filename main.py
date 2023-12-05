# main.py

from seed import *
from jdlv_utils import *
import tkinter as tk

class JeuDeLaVieGUI:
    def __init__(self, root, taille):
        self.root = root
        self.root.title("Conway's Game of Life By Klaynight-dev")
        self.root.configure(bg="#F5F5F5")  # Couleur de fond pour toute la fenêtre

        self.taille_grille = taille
        self.jeu_en_cours = False

        self.jeu_de_la_vie = Grille(self.taille_grille, grille_initiale=generer_grille_initiale(self.taille_grille))

        self.canvas = tk.Canvas(self.root, width=self.taille_grille * 20, height=self.taille_grille * 20,
                                bg="white", bd=1, relief=tk.RAISED)  # Bordure pour le canevas
        self.canvas.pack(pady=10)

        self.cellules = [[self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="#E0E0E0", outline="#D3D3D3")
                          for j in range(self.taille_grille)]
                         for i in range(self.taille_grille)]

        self.frame_largeur = tk.Frame(self.root, bg="#F5F5F5")  # Couleur de fond pour les cadres
        self.frame_largeur.pack(pady=5)
        self.label_largeur = tk.Label(self.frame_largeur, text="Largeur:", font=("Arial", 12), bg="#F5F5F5")
        self.label_largeur.pack(side=tk.LEFT)
        self.input_largeur = tk.Entry(self.frame_largeur, width=5, font=("Arial", 12))
        self.input_largeur.pack(side=tk.LEFT)
        self.input_largeur.insert(0, str(self.taille_grille))

        self.frame_hauteur = tk.Frame(self.root, bg="#F5F5F5")
        self.frame_hauteur.pack(pady=5)
        self.label_hauteur = tk.Label(self.frame_hauteur, text="Hauteur:", font=("Arial", 12), bg="#F5F5F5")
        self.label_hauteur.pack(side=tk.LEFT)
        self.input_hauteur = tk.Entry(self.frame_hauteur, width=5, font=("Arial", 12))
        self.input_hauteur.pack(side=tk.LEFT)
        self.input_hauteur.insert(0, str(self.taille_grille))

        self.btn_changer_taille = tk.Button(self.root, text="Changer Taille", command=self.changer_taille,
                                            font=("Arial", 12), padx=10, pady=5, bg="#4CAF50", fg="white", bd=0)
        self.btn_changer_taille.pack(pady=5)

        self.btn_demarrer_arreter = tk.Button(self.root, text="Démarrer", command=self.demarrer_arreter_jeu,
                                              font=("Arial", 12), padx=10, pady=5, bg="#2196F3", fg="white", bd=0)
        self.btn_demarrer_arreter.pack()

        self.canvas.bind("<Button-1>", self.changer_etat_cellule)

        self.root.after(1000, self.update_game)

    def changer_etat_cellule(self, event):
        cellule_x = event.x // 20
        cellule_y = event.y // 20

        cellule = self.jeu_de_la_vie.grille[cellule_y][cellule_x]
        if cellule.est_vivant():
            cellule.mourir()
        else:
            cellule.naitre()

        color = "white" if not cellule.est_vivant() else "black"
        self.canvas.itemconfig(self.cellules[cellule_y][cellule_x], fill=color)

    def demarrer_arreter_jeu(self):
        if self.jeu_en_cours:
            self.jeu_en_cours = False
            self.btn_demarrer_arreter.config(text="Démarrer")
        else:
            self.jeu_en_cours = True
            self.btn_demarrer_arreter.config(text="Arrêter")
            self.update_game()

    def update_game(self):
        if self.jeu_en_cours:
            self.jeu_de_la_vie.mettre_a_jour()

            # Utiliser la nouvelle taille de la grille
            taille_actuelle = len(self.jeu_de_la_vie.grille)

            for i in range(taille_actuelle):
                for j in range(taille_actuelle):
                    if i < len(self.cellules) and j < len(self.cellules[i]):
                        color = "white" if not self.jeu_de_la_vie.grille[i][j].est_vivant() else "black"
                        self.canvas.itemconfig(self.cellules[i][j], fill=color)

            self.root.after(500, self.update_game)

    def changer_taille(self):
        largeur = int(self.input_largeur.get())
        hauteur = int(self.input_hauteur.get())

        self.taille_grille = largeur if largeur > 0 else self.taille_grille
        hauteur = hauteur if hauteur > 0 else self.taille_grille

        self.jeu_de_la_vie = Grille(self.taille_grille, grille_initiale=generer_grille_initiale(self.taille_grille))

        # Réinitialiser l'interface graphique avec la nouvelle taille
        self.canvas.config(width=largeur * 20, height=hauteur * 20)

        # Recréer la liste self.cellules avec les dimensions correctes
        self.cellules = [[self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="white")
                          for j in range(largeur)]
                         for i in range(hauteur)]

        self.taille_grille = largeur  # Mise à jour de la taille actuelle de la grille





if __name__ == "__main__":
    root = tk.Tk()
    jeu = JeuDeLaVieGUI(root, 20)
    root.iconphoto(False, tk.PhotoImage(file="content/img/logo.ico"))
    root.mainloop()
