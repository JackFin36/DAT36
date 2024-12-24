import os
import sys
from PyQt6 import QtWidgets, uic
sys.path.append(r'CODE\src\classes')
from DropArea import DropArea
from DataManager import DataManager

class ImportTab(QtWidgets.QWidget):
    def __init__(self, MainWindow, data_manager: DataManager):
        super().__init__()
        uic.loadUi(r'CODE/ui/ImportTab.ui', self)  # Lade die UI-Datei

        self.DM = data_manager
        self.MW = MainWindow
        # Widgets zuweisen
        self.import_button = self.findChild(QtWidgets.QPushButton, "importButton")
        self.fileSelector = self.findChild(QtWidgets.QComboBox, "FileSelectionComboBox")
        self.xlistWidget = self.findChild(QtWidgets.QListView, "xDataListWidget")
        self.ylistWidget = self.findChild(QtWidgets.QListView, "yDataListWidget")
        self.table_layout = self.findChild(QtWidgets.QVBoxLayout, "tabTableLayout")  
        self.PlotButton = self.findChild(QtWidgets.QPushButton, "PlotButton")

        # Add DropArea/ Table Display area manually
        self.table_widget = DropArea(self.DM, self)
        self.table_layout.addWidget(self.table_widget)

        # Verbindungen einrichten
        self.import_button.clicked.connect(self.selectButtonImport)
        self.fileSelector.currentIndexChanged.connect(self.file_selected)
        self.PlotButton.clicked.connect(self.plot)


    def plot(self):
        # Logic still missing as Plot Tab in development
        self.MW.mainTabWidget.setCurrentIndex(2)

    def file_selected(self, index):
        self.DM.selected_file = self.fileSelector.itemText(index)
        itemList = self.DM.get_headers(self.DM.selected_file)
        self.xlistWidget.addItems(itemList)
        self.ylistWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.ylistWidget.addItems(itemList)

    def selectButtonImport(self):
        options = QtWidgets.QFileDialog.Option(0)
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Data File", "", 
                                                     "CSV Files (*.csv);;JSON Files (*.json);;Text Files (*.txt);;All Files (*)", 
                                                     options=options)
        if file_path:
            self.DM.process_file(file_path)
            filename = os.path.basename(file_path)
            self.fileSelector.addItems(self.DM.list_datasets())
            self.display_data_in_tabs(self.DM.get_data(file_path), self.DM.get_headers(file_path), filename)

    def display_data_in_tabs(self, data, headers, filename):
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