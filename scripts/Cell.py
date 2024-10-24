# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:19:04 2024

@author: ablot
"""

class Cell:
    
    def __init__(self, revealed=False, bomb=False, flag=False, hint=0):
        """Initialise une cellule avec une valeur par défaut (0)."""
        self.revealed = revealed
        self.bomb = bomb
        self.flag = flag
        self.hint = hint
    
    def __repr__(self):
        """Affiche la valeur de la cellule lorsqu'on l'affiche."""
        return str(self.revealed) +  str(self.bomb) + str(self.flag) + str(self.hint)
    
    def reveal (self):
        self.valeur = True
        
    def put_mine (self):
        self.bomb = True
    
    def put_flag (self):
        self.flag = True
    
    
    def remove_flag (self):
        self.flag = False
    
    
        
        
    