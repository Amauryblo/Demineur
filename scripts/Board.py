# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:28:39 2024

@author: ablot
"""
from Cell import Cell

import random

class Grille_facile:
    
    def __init__(self, lignes=10, colonnes=10):
        """Creation d'une grille de taille donnée"""
        
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[Cell() for _ in range(colonnes)] for _ in range(lignes)]
        
        
    def afficher(self):
        """affiche dans la console la grille avec les valeurs des cases que l'ont souhaite afficher.
        Le choix de ces valeurs se fait dans la classe Cell avec la méthode __repr__
            
        """

        for ligne in self.grille:
            print(' '.join(map(str, ligne)))
    
    
    def GenerateMine(self, nombre):
        """Place un nombre de mine aléatoirement dans la grille"""
        indices = [(i, j) for i in range(self.lignes) for j in range(self.colonnes)]
        cellules_choisies = random.sample(indices, nombre)
        
        for (i, j) in cellules_choisies:
            self.grille[i][j].put_mine()
    
    
    
    
    def GenerateHint(self):
        """Calcul un indice pour chacune des cases"""
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if not self.grille[i][j].bomb:  #pas d'indice pour les bombes
                    self.grille[i][j].hint = self.Getneighbors(i, j)


    def Getneighbors(self, ligne, colonne):
        """récupère le nombre de bombes alentours, sera utilisé pour calculer l'indice"""
        bombes = 0
        # Parcours des 8 cellules voisines (et vérification des bords)
        for x in range(ligne - 1, ligne + 2):
            for y in range(colonne - 1, colonne + 2):
                if 0 <= x < self.lignes and 0 <= y < self.colonnes:  # Vérifie si on est dans les limites
                    if self.grille[x][y].bomb:  # Si la cellule est une bombe
                        bombes += 1
        return bombes



    def get_cell(self, ligne, colonne):
        """Retourne la case aux coordonnées spécifiées"""
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            return self.grille[ligne][colonne]
        else:
            raise IndexError("Les coordonnées sont hors limites.")
    
    
    def reveal_all(self):
        """non utilisé, devait servir à reveler l'ensemble des cases à la fin du jeu"""
        for i in range(self.lignes):
            for j in range(self.colonnes):
                Cell=self.get_cell(i,j)
                Cell.reveal()
    
    
                    
    def reveal_zone(self, ligne, colonne):
        """Révèle une zone autour d'une cellule si elle n'est pas une bombe et a un hint de 0"""
        cellule = self.get_cell(ligne, colonne)
        
        # Arrête la récursion si la cellule est hors limites, déjà révélée ou une bombe
        if not cellule or cellule.revealed or cellule.bomb:
            return  # Ne pas continuer pour les cellules hors limite ou déjà révélées
    
        # Marque la cellule comme révélée
        cellule.revealed = True
        
        print(f"Cellule révélée à ({ligne}, {colonne}) avec hint = {cellule.hint}")  # Debugging
    
        # Si hint est 0, révéler toutes les cellules voisines
        if cellule.hint == 0:
            for x in range(ligne - 1, ligne + 2):
                for y in range(colonne - 1, colonne + 2):
                    # Révéler chaque cellule voisine valide
                    if (x, y) != (ligne, colonne) and 0 <= x < self.lignes and 0 <= y < self.colonnes:
                        voisin = self.get_cell(x, y)
                        if voisin and not voisin.revealed:
                            self.reveal_zone(x, y)  # Appel récursif sur le voisin

# # # Exemple d'utilisation
# grille = Grille_facile()
# # grille.afficher()

# # # # Modifier une case
# grille.GenerateMine(15)
# grille.GenerateHint()
# # C = grille.get_cell(1,1)
# # # # C.reveal()
# # # # C.put_flag()

# grille.reveal_zone(1,9)
# grille.afficher()

# grille.reveal_zone(8,4)
# grille.afficher()
# grille.reveal_all()
# grille.reveal_all()
# # grille[1][1].reveal()
# # Afficher à nouveau après modification
# print("\nAprès modification :")
# grille.afficher()























