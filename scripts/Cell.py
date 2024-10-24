# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:19:04 2024

@author: ablot
"""

class Cell:
    
    def __init__(self, revealled=False, bomb=False, flag=False):
        """Initialise une cellule avec une valeur par défaut (0)."""
        self.revealled = False
        self.bomb = False
        self.flag = False
    
    def __repr__(self):
        """Affiche la valeur de la cellule lorsqu'on l'affiche."""
        return str(self.revealled) +  str(self.bomb) + str(self.flag)
    
    def reveal (self):
        self.valeur = True
        
    def put_mine (self):
        self.bomb = True
    
    def put_flag (self):
        self.flag = True
    
    
    def remove_flag (self):
        self.flag = False
        
        
    