import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
import pandas as pd
sys.path.append(r'CODE\src\classes')
from DataManager import DataManager

class ImportDataButton(QtWidgets.QPushButton):
    def __init__(self, main_window):
        super().__init__()
        self.clicked.connect(self.import_data)  # Connect the button click to the import_data method
        self.main_window = main_window  # Reference to the main window
        self.DM = DataManager

    def import_data(self):
        # Open a file dialog to select a data file
        options = QFileDialog.Option(0)
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Data File", "", 
                                                     "CSV Files (*.csv);;JSON Files (*.json);;Text Files (*.txt);;All Files (*)", 
                                                     options=options)
        if file_path:
            # Process the selected file
            self.DM.process_file(file_path)
