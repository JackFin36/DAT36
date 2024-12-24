import sys
from PyQt6 import QtWidgets, uic
from ImportTab import ImportTab
sys.path.append(r'CODE\src\classes')
from DataManager import DataManager

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'CODE/ui/MainWindow.ui', self)
        self.setWindowTitle("Data Analysis Tool 36")

        self.DM = DataManager()

        # MainTabWidget initialisieren
        self.mainTabWidget = self.findChild(QtWidgets.QTabWidget, "MainTabWidget")

        # ImportTab hinzufügen
        self.import_tab = ImportTab(self, self.DM)
        self.mainTabWidget.addTab(self.import_tab, "Import")

        self.show()

    def plot(self):
        self.mainTabWidget.setCurrentIndex(2)