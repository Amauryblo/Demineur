# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:28:39 2024

@author: ablot
"""
from Cell import Cell

import random

class Grille_facile:
    
    def __init__(self, lignes=10, colonnes=10):
        #
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[Cell() for _ in range(colonnes)] for _ in range(lignes)]
        
        
    def afficher(self):

        for ligne in self.grille:
            print(' '.join(map(str, ligne)))
    
    def GenerateMine(self, nombre):

        indices = [(i, j) for i in range(self.lignes) for j in range(self.colonnes)]
        cellules_choisies = random.sample(indices, nombre)
        
        for (i, j) in cellules_choisies:
            self.grille[i][j].put_mine()
    
    
    
    
    def GenerateHint(self):
        
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if not self.grille[i][j].bomb:  # On ne calcule pas l'indice pour les bombes
                    self.grille[i][j].hint = self.Getneighbors(i, j)

    def Getneighbors(self, ligne, colonne):
        
        bombes = 0
        # Parcours des 8 cellules voisines (et vérification des bords)
        for x in range(ligne - 1, ligne + 2):
            for y in range(colonne - 1, colonne + 2):
                if 0 <= x < self.lignes and 0 <= y < self.colonnes:  # Vérifie si on est dans les limites
                    if self.grille[x][y].bomb:  # Si la cellule est une bombe
                        bombes += 1
        return bombes

                    
                    

# Exemple d'utilisation
grille = Grille_facile()
grille.afficher()

# Modifier une case

grille.GenerateMine(10)
grille.GenerateHint()

# Afficher à nouveau après modification
print("\nAprès modification :")
grille.afficher()























