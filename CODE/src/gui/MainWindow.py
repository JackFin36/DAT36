import sys
from PyQt6 import QtWidgets, uic
from DropArea import DropArea
from ImportButtons import ImportDataButton

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'CODE\ui\MainWindow.ui', self)  # Replace with your .ui file name
        self.setWindowTitle("Data Analysis Tool 36")

        # Assigning objects to important widgets

        self.import_button = self.findChild(QtWidgets.QPushButton, "importButton")  # Button for importing data

        self.table_widget = self.tableWidget  # Table widget to display data
        self.drop_area = self.DropArea  # QTextEdit for drag-and-drop

        # Connect signals to slots
        self.import_button.clicked.connect(self.buttonImport)
        #self.search_button.clicked.connect(self.search_directory)

        self.show()

    def buttonImport(self):
        ImportDataButton.import_data(self)
