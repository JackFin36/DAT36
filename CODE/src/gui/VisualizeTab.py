import os
import sys
import numpy as np
from PyQt6 import QtWidgets, uic
import pyqtgraph as pg
from pyqtgraph import PlotWidget
sys.path.append(r"C:\Users\duong\Desktop\DATool\DAT36-main\CODE\src\classes")
from DataManager import DataManager

class VisualizeTab(QtWidgets.QWidget):
    def __init__(self, MainWindow, data_manager: DataManager):
        super().__init__()
        uic.loadUi(r'C:\Users\duong\Desktop\DATool\DAT36-main\CODE\ui\VisualizeTab.ui', self)  # Lade die UI-Datei

        self.DM = data_manager
        self.MW = MainWindow
        
        # Widgets zuweisen
        
        self.PlotWindow = self.findChild(PlotWidget, "PlotArea")
        # General Settings
        self.diagramTypeCB = self.findChild(QtWidgets.QComboBox, "DiagramTypeComboBox")
        self.nameXAxisTE = self.findChild(QtWidgets.QTextEdit, "NameXAxisTextEdit")
        self.nameYAxisTE = self.findChild(QtWidgets.QTextEdit, "NameYAxisTextEdit")
        self.plotTitleTE  = self.findChild(QtWidgets.QTextEdit, "PlotTitleTextBox")
        self.showGridChB = self.findChild(QtWidgets.QCheckBox, "ShowGridCheckBos")
        self.showLegendChB = self.findChild(QtWidgets.QCheckBox, "ShowLegendCheckBox")
        # Graph Settings
        self.applyGraphSettingsButton = self.findChild(QtWidgets.QPushButton, "ApplyGraphSettingsButton")
        self.colourCB = self.findChild(QtWidgets.QComboBox, "ColourComboBox")
        self.graphNameTE = self.findChild(QtWidgets.QTextEdit, "GraphNameTextEdit")
        self.lineTypeCB = self.findChild(QtWidgets.QComboBox, "LineTypeComboBox")
        self.selectGraphCB = self.findChild(QtWidgets.QComboBox, "SelectGraphComboBox")
        # Export Layout
        self.exportButton = self.findChild(QtWidgets.QPushButton, "ExportButton")
        self.selectFileTypeCB = self.findChild(QtWidgets.QComboBox, "SelectFileTypeComboBox")

        # Verbindungen einrichten
        #self.exportButton.clicked.connect(self.exportFile)
        #self.fileSelector.currentIndexChanged.connect(self.file_selected)


    def scattery(self, X, Y):
        self.PlotWindow.clear()
        self.PlotWindow.setBackground('w')
        self.PlotWindow.addLegend()
        self.PlotWindow.showGrid(x=True,y=True)
        self.PlotWindow.setLabel('left','y-Data')
        self.PlotWindow.setLabel('bottom','x-Data')
        
        scatter = pg.ScatterPlotItem(x=X, y=Y, pen=pg.mkPen('b', width=2), brush=pg.mkBrush(255, 0, 0, 120))
        self.PlotWindow.addItem(scatter)