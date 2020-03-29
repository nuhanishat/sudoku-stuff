#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 04:34:15 2020

@author: nuha
"""

import sys
from PyQt5 import QtWidgets, QGridLayout, QPushButton, QApplication

class SudokuApp(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        
        for x in range(3):
            for y in range(3):
                buttons = QPushButton(str(str(3*x+y)))
                
                grid_layout.addWidget(buttons, x, y)
                
            grid_layout.setColumnStretch(x, x+1)
            
        self.setWindowTitle('Nuha\'s Sudoku Solver')
        
    def createWindow():
        
                
                
        

def createWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle('Nuha\'s Sudoku Solver')
    window.setGeometry(0, 0, 800, 500)
    
    buttonA = QtWidgets.QPushButton(window)
    buttonB = QtWidgets.QPushButton(window)
    buttonC = QtWidgets.QPushButton(window)
    buttonD = QtWidgets.QPushButton(window)
    #labelA = QtWidgets.QLabel(window)
    
    buttonA.setText('Easy')
    buttonB.setText('Medium')
    buttonC.setText('Hard')
    buttonD.setText('Solve')
    #labelA.setText('Show Label')
    
    buttonA.move(10, 10)
    buttonB.move(10, 50)
    buttonC.move(10, 90)
    buttonD.move(10, 250)
    #labelA.move(500, 100)
    
    window.show()
    sys.exit(app.exec_())

createWindow()

