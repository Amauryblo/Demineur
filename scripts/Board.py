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
    
            
    

    def GenerateMine(self, nombre, valeur):

        indices = [(i, j) for i in range(self.lignes) for j in range(self.colonnes)]
        cellules_choisies = random.sample(indices, nombre)
        
        for (i, j) in cellules_choisies:
            self.grille[i][j].Cell.Cell().put_mine

# Exemple d'utilisation
grille = Grille_facile()
grille.afficher()

# Modifier une case



# Afficher à nouveau après modification
print("\nAprès modification :")
grille.afficher()