# Jeu de la Vie de Conway en Python

Ce programme Python implémente le Jeu de la Vie de Conway avec une interface graphique Tkinter. Le Jeu de la Vie est un automate cellulaire qui évolue en fonction d'états initiaux donnés et de règles simples.

## Fonctionnalités

### Cellule
- La classe `Cellule` représente une cellule dans la grille du jeu.
- Chaque cellule peut être soit morte (`False`) soit vivante (`True`).
- Méthodes disponibles : `est_vivant()`, `mourir()`, `naitre()`.

### Grille
- La classe `Grille` représente la grille du jeu.
- Initialisation d'une grille avec une taille donnée et une configuration initiale.
- Compte le nombre de voisins vivants pour chaque cellule.
- Met à jour l'état de la grille selon les règles du Jeu de la Vie.

### JeuDeLaVieGUI
- Interface graphique réalisée avec Tkinter pour afficher la grille du jeu.
- Crée une fenêtre avec un canvas pour afficher la grille.
- Met à jour l'affichage graphique à chaque itération de la simulation.

## Utilisation
1. Assurez-vous d'avoir Python installé.
2. Exécutez le programme à l'aide de `python main.py`.
3. Une fenêtre s'ouvre, affichant la grille initiale.
4. La simulation démarre et évolue selon les règles du Jeu de la Vie.
5. Les cellules vivantes sont en noir, les cellules mortes en blanc.

## Fichiers
- `main.py`: Contient les classes `Cellule`, `Grille`, et `JeuDeLaVieGUI`.
- `seed.py`: Fonctions pour générer une configuration initiale aléatoire.

## Remarque
Ce code implémente les règles du Jeu de la Vie de Conway. La grille est mise à jour à chaque itération, modifiant l'état des cellules en fonction de leur voisinage. La configuration initiale de la grille est générée de manière aléatoire.
