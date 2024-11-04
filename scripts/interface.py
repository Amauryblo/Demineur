# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:48:13 2024

@author: ablot
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QCheckBox 
from Board import Grille_facile
from interface_grille import Window

class Fenetre(QWidget):
    def __init__(self):
        """Création de l'interface avec les options de démarrage"""
        super().__init__()
        
        self.resize(1000, 800)
        
        # Bouton pour commencer la partie
        self.bouton1 = QPushButton("Commencer partie")
        self.bouton1.clicked.connect(self.appui_bouton1)

        # Checkboxes pour le choix du niveau
        self.checkbox_debutant = QCheckBox("Débutant")
        self.checkbox_intermediaire = QCheckBox("Intermédiaire")
        self.checkbox_confirme = QCheckBox("Confirmé")

        # Connecte chaque checkbox à une méthode pour gérer les sélections uniques
        self.checkbox_debutant.stateChanged.connect(self.selection_unique)
        self.checkbox_intermediaire.stateChanged.connect(self.selection_unique)
        self.checkbox_confirme.stateChanged.connect(self.selection_unique)

        # Création du layout
        layout = QVBoxLayout()
        layout.addWidget(self.bouton1)
        layout.addWidget(self.checkbox_debutant)
        layout.addWidget(self.checkbox_intermediaire)
        layout.addWidget(self.checkbox_confirme)
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")

    def selection_unique(self):
        """Permet de faire en sorte qu'un seul niveau soit sélectionné à la fois."""
        sender = self.sender()
        if sender == self.checkbox_debutant:
            self.checkbox_intermediaire.setChecked(False)
            self.checkbox_confirme.setChecked(False)
        elif sender == self.checkbox_intermediaire:
            self.checkbox_debutant.setChecked(False)
            self.checkbox_confirme.setChecked(False)
        elif sender == self.checkbox_confirme:
            self.checkbox_debutant.setChecked(False)
            self.checkbox_intermediaire.setChecked(False)

    def appui_bouton1(self):
        """Démarre la partie avec le niveau sélectionné."""
        # Vérifie le niveau sélectionné
        niveau = None
        if self.checkbox_debutant.isChecked():
            niveau = "Débutant"
            lignes, colonnes = 10, 10 
        elif self.checkbox_intermediaire.isChecked():
            niveau = "Intermédiaire"
            lignes, colonnes = 15, 15 
        elif self.checkbox_confirme.isChecked():
            niveau = "Confirmé"
            lignes, colonnes = 20, 20 

        if niveau:
            print(f"Appui sur le bouton1 - Niveau sélectionné : {niveau}")
            self.close()
            # Ouvrir la fenêtre de jeu avec le niveau sélectionné
            fen = Window(lignes=lignes, colonnes=colonnes)
            fen.show()
        else:
            # Affiche une alerte si aucun niveau n'est sélectionné
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un niveau pour commencer la partie.")
        

            
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)


fen = Fenetre()
fen.show()

app.exec_()