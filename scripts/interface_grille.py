# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:20:43 2024

@author: ablot
"""

import sys
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
from Board import Grille_facile

class Window(QWidget):
    """2ème interface, celle de la partie."""
    def __init__(self, lignes=10, colonnes=10):
        
        super().__init__()
        
        self.lignes = lignes
        self.colonnes = colonnes
        self.initUI()
        self.grille = None
        self.initGrille()
        self.click = 0 
        
        # grille = Grille_facile()
        # grille.GenerateMine(15)
        # grille.GenerateHint()

    def initUI(self):
        """Crétion d'une grille de boutons, chaque bouton correspond à une case"""
        self.grid = QGridLayout()
        
        # Configuration de la taille de la fenêtre
        self.resize(50 * self.lignes, 50 * self.colonnes)
        
        # Création des boutons pour chaque cellule de la grille
        self.buttons = {}
        for row in range(self.lignes):
            for col in range(self.colonnes):
                bouton = QPushButton("")
                bouton.setFixedSize(50, 50)  # Taille de chaque cellule

                
                # Ajoute l'event filter pour chaque bouton
                bouton.installEventFilter(self)
                
                # Connecte le clic gauche pour appeler cellClicked
                bouton.clicked.connect(lambda checked, r=row, c=col: self.cellClicked(r, c))

                
                
                
                self.grid.addWidget(bouton, row, col)
                self.buttons[(row, col)] = bouton  # Sauvegarde le bouton pour y accéder facilement
                bouton.setStyleSheet("background-color: lightgray;")
        self.setLayout(self.grid)
        self.setWindowTitle("Démineur")
        
    
    def eventFilter(self, source, event):
     # Vérifie si un clic de souris est détecté sur un bouton
     if event.type() == QEvent.MouseButtonPress and source in self.buttons.values():
         if event.button() == Qt.LeftButton:
             # Clic gauche
             for (row, col), bouton in self.buttons.items():
                 if bouton == source:
                     self.cellClicked(row, col)
                     return True
         elif event.button() == Qt.RightButton:
             # Clic droit
             for (row, col), bouton in self.buttons.items():
                 if bouton == source:
                     self.rightClickAction(row, col)
                     return True
     return super().eventFilter(source, event)
    
    
    
    
    
    def initGrille(self):
       """Initialisation de la grille venant de la classe Board. Cette grille contient les attributs bomb, flag... 
       Quand un bouton est cliqué, c'est dans cette grille que les attributs sont récupérés et modifiés'
       """
       c = self.lignes
       nombre_de_bombes = int(c + c / 4) # la densité de bombe est constante
       self.grille = Grille_facile(lignes=self.lignes, colonnes=self.colonnes)
       self.grille.GenerateMine(nombre_de_bombes)
       self.grille.GenerateHint()


    def rightClickAction(self, row, col):
        """
        Méthode appelée lorsqu'une cellule est cliquée avec le bouton droit. Ici le clic dépose un drapeau (flag)
        row : int
        col : int
        
        """
        bouton = self.buttons[(row, col)]
        C = self.grille.get_cell(row,col)
        if not C.flag:
            C.put_flag()   # méthode de Cell pour placer un drapeau ( change l'attribut "flag" de la case)
            bouton.setStyleSheet("background-color: yellow;") # les drapeaux se caractérisent par une case jaune
        else:
           C.remove_flag()
           bouton.setStyleSheet("background-color: lightgray;")

    
   


    
    def cellClicked(self, row, col):
        """Action exécuté lors d'un clic gauche sur un bouton. Ca révèle la case
        
        row : int
        col : int
        """
        C = self.grille.get_cell(row, col)
    
        if not C.flag:  # Seulement si pas de drapeau, s'il y a un drapeau la case ne peut être modifiée
            bouton = self.buttons[(row, col)]
            bouton.setStyleSheet("background-color: white")  # les cases découvertes sont blanches
    
            if C.hint != 0 and not C.bomb:
                bouton.setText(str(C.hint))  # Affiche l'indice sur la case découverte
            elif C.bomb:
                bouton.setText("X")
                self.grille.reveal_all()
                self.showGameOverDialog()  # met fin au jeu si une bombe est découverte
                return
    
            if C.hint == 0:
                self.grille.reveal_zone(row, col)  # revèle les cases alentours si il n'y a aucune bombe
    
            
            for r in range(self.lignes): # Met à jour toutes les cellules révélées
                for c in range(self.colonnes):
                    Case = self.grille.get_cell(r, c)
                    if Case.revealed:
                        bouton_reveal = self.buttons[(r, c)]
                        bouton_reveal.setStyleSheet("background-color: white")
                        if Case.hint != 0:
                            bouton_reveal.setText(str(Case.hint))
    
            # Vérifier la victoire après chaque clic
            D = self.grille.get_cell(row, col)
            D.reveal()
            if self.VerifVictoire():
                self.showGameWinDialog()
            self.grille.afficher()  # affiche l'évolution dans la console
            print(" ")
                
            
            
    def VerifVictoire(self):
        """
        Vérifie si toutes les cases sont révélées ou contiennent une bombe.
        """
        for row in range(self.lignes):
            for col in range(self.colonnes):
                cell = self.grille.get_cell(row, col)  # Récupère la cellule actuelle
                # Vérifie que chaque cellule sans bombe est révélée
                if not cell.bomb and not cell.revealed:
                    return False  # Si une cellule sans bombe n'est pas révélée, la partie n'est pas gagnée
        return True  # Toutes les cellules sans bombe sont révélées, donc victoire


        
        
        
    def showGameOverDialog(self):
        """
        Affiche une pop-up en cas de clic sur une bombe avec une option pour recommencer ou quitter
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Partie terminée")
        msg_box.setText("Vous avez cliqué sur une bombe ! Voulez-vous recommencer ?")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Gestion de la réponse de l'utilisateur
        response = msg_box.exec_()
        if response == QMessageBox.Yes:
            self.restartGame()
        else:
            self.close()  # Ferme la fenêtre


    def showGameWinDialog(self):
         """
         Affiche une pop-up lorsque toutes les cases vides ont été découvertes
         """
         msg_box = QMessageBox()
         msg_box.setWindowTitle("Partie terminée")
         msg_box.setText("Vous avez gagné !!")
         msg_box.setIcon(QMessageBox.Warning)
         msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

         # Gestion de la réponse de l'utilisateur
         response = msg_box.exec_()
         if response == QMessageBox.Yes:
             self.restartGame()
         else:
             self.close()  # Ferme la fenêtre
             
             
    def restartGame(self):
        """
        Redémarre la partie en réinitialisant la grille et les boutons.
        """
        # Supprime et réinitialise chaque bouton
        for bouton in self.buttons.values():
            bouton.setText("")
            bouton.setStyleSheet("background-color: lightgray;")
        
        # Génère une nouvelle grille
        self.initGrille()      

       
       
# Initialisation de l'application
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)



#Création et affichage de la fenêtre principale
# fen = Window()
# fen.show()

# # # Exécution de l'application
# app.exec_()

#mise en place de la grille
# grille = Grille_facile()
# grille.GenerateMine(15)
# grille.GenerateHint()
# grille.afficher()
# cellule = grille.get_cell(2, 2)

# cellule.reveal()