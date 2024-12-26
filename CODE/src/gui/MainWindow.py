import sys
from PyQt6 import QtWidgets, uic
sys.path.append(r"C:\Users\duong\Desktop\DATool\DAT36-main\CODE\src\gui")
from ImportTab import ImportTab
from VisualizeTab import VisualizeTab
sys.path.append(r"C:\Users\duong\Desktop\DATool\DAT36-main\CODE\src\classes")
from DataManager import DataManager

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'C:\Users\duong\Desktop\DATool\DAT36-main\CODE\ui\MainWindow.ui', self)
        self.setWindowTitle("Data Analysis Tool 36")

        self.DM = DataManager()

        # MainTabWidget initialisieren
        self.mainTabWidget = self.findChild(QtWidgets.QTabWidget, "MainTabWidget")

        # Tabs hinzufügen
        self.startSeite = QtWidgets.QCalendarWidget()
        self.mainTabWidget.addTab(self.startSeite, 'Startseite')
        self.import_tab = ImportTab(self, self.DM)
        self.mainTabWidget.addTab(self.import_tab, "Import")
        self.visualize_tab = VisualizeTab(self, self.DM)
        self.mainTabWidget.addTab(self.visualize_tab, "Visualize")
        self.analyze_tab = QtWidgets.QCalendarWidget()
        self.mainTabWidget.addTab(self.analyze_tab, 'Analyze')

        self.show()
