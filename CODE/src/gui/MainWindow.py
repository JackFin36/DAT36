import sys
from PyQt6 import QtWidgets, uic
from DropArea import DropArea
from ImportButtons import ImportDataButton
sys.path.append(r'CODE\src\classes')
from DataManager import DataManager


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'CODE\ui\MainWindow.ui', self)  # Replace with your .ui file name
        self.setWindowTitle("Data Analysis Tool 36")

        self.DM = DataManager()

        # Assigning objects to important widgets

        self.import_button = self.findChild(QtWidgets.QPushButton, "importButton")  # Button for importing data

        self.table_widget = self.findChild(QtWidgets.QTableWidget, "rawDataTabular")  # Table widget to display data

        self.drop_area = self.findChild(QtWidgets.QTextEdit, "DropArea")  # QTextEdit for drag-and-drop
        #self.DA = DropArea(self.drop_area)

        # Connect signals to slots
        self.import_button.clicked.connect(self.buttonImport)
        #self.search_button.clicked.connect(self.search_directory)

        self.show()

    def buttonImport(self):
        ImportDataButton.import_data(self)
        self.display_data_in_tabs(self, self.DM.datasets)
    
    
    def display_data_in_tabs(self, dataframe):
        for column in dataframe.columns:

            self.table_widget.setRowCount(dataframe.shape[0])  # Anzahl der Zeilen
            self.table_widget.setColumnCount(1)  # Eine Spalte
            
            # Setze den Header für die Tabellenspalte
            self.table_widget.setHorizontalHeaderLabels([column])
            
            # Füge die Daten in die Tabelle ein
            for row in range(dataframe.shape[0]):
                item = QtWidgets.QTableWidgetItem(str(dataframe[column].iloc[row]))
                self.table_widget.setItem(row, 0, item)
            