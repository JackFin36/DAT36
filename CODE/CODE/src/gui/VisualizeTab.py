import os
import sys
import numpy as np
from PyQt6 import QtWidgets, uic
import pyqtgraph
from pyqtgraph import PlotWidget
sys.path.append(r'CODE\src\classes')
from DataManager import DataManager

class VisualizeTab(QtWidgets.QWidget):
    def __init__(self, MainWindow, data_manager: DataManager):
        super().__init__()
        uic.loadUi(r'CODE/ui/VisualizeTab.ui', self)  # Lade die UI-Datei

        self.DM = data_manager
        self.MW = MainWindow
        # Widgets zuweisen
        self.PlotWindow = self.findChild(PlotWidget, "PlotArea")

        # Verbindungen einrichten
        #self.import_button.clicked.connect(self.selectButtonImport)
        #self.fileSelector.currentIndexChanged.connect(self.file_selected)

        self.plotty()

    def plotty(self):
        self.PlotWindow.clear()
        self.PlotWindow.setBackground('w')
        self.PlotWindow.addLegend()
        self.PlotWindow.showGrid(x=True,y=True)
        self.PlotWindow.setLabel('left','y-Data')
        self.PlotWindow.setLabel('bottom','x-Data')

        X = np.linspace(0,100,100)
        Y = np.random.rand(100)
        self.PlotWindow.plot(X,Y)