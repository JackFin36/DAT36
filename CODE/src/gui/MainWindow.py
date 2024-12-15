import sys
import os
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtGui import QDragEnterEvent
from DropArea import DropArea
sys.path.append(r'CODE\src\classes')
from DataManager import DataManager

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'CODE\ui\MainWindow.ui', self)  # Replace with your .ui file name
        self.setWindowTitle("Data Analysis Tool 36")

        self.DM = DataManager()

        # Assigning objects to important widgets
        # Following section covers Data Import
        self.import_button = self.findChild(QtWidgets.QPushButton, "importButton")  # Button for importing data
        self.table_layout = self.findChild(QtWidgets.QVBoxLayout, "tabTableLayout")  # Table widget to display data
        self.table_widget = DropArea(self.DM, self)
        self.table_layout.addWidget(self.table_widget)

        #Following Section covers Data selection 
        self.fileSelector = self.findChild(QtWidgets.QComboBox,'FileSelectionComboBox')
        self.fileSelector.currentIndexChanged.connect(self.file_selected)
        
        # Connect signals to slots
        self.import_button.clicked.connect(self.selectButtonImport)
        #self.xlistWidget.itemSelectionChanged.connect(self.on_selection_changed)  

        self.show()

    def file_selected(self, index):
        self.DM.selected_file = self.fileSelector.itemText(index)
        itemList = self.DM.get_headers(self.DM.selected_file)
        self.xlistWidget = self.findChild(QtWidgets.QListView, "xDataListWidget")
        self.xlistWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)     # Erlaube Mehrfachauswahl in der QListWidget
        self.xlistWidget.addItems(itemList)  # Beispiel-Elemente zur QListWidget hinzufügen

    def selectButtonImport(self):
        options = QtWidgets.QFileDialog.Option(0)
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Data File", "", 
                                                     "CSV Files (*.csv);;JSON Files (*.json);;Text Files (*.txt);;All Files (*)", 
                                                     options=options)
        if file_path:
            # Process the selected file
            self.DM.process_file(file_path)
            self.filename = os.path.basename(file_path)
        
            self.display_data_in_tabs(self.DM.get_data(file_path), self.DM.get_headers(file_path), self.filename)
            
            self.fileSelector.addItems(self.DM.list_datasets())
            
    def display_data_in_tabs(self, data, headers,filename):
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        
        # Tabelle erstellen
        table = QtWidgets.QTableWidget(data.shape[0], data.shape[1])
        table.setHorizontalHeaderLabels(headers)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i, j])))
        
        layout.addWidget(table)
        tab.setLayout(layout)
        self.table_widget.addTab(tab, filename)
            