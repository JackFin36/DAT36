import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
sys.path.append(r'CODE\src\classes')
from DataManager import DataManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Beispiel")
        self.setGeometry(100, 100, 600, 400)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        DM = DataManager()
        DM.process_file(r'random_data.csv')

        # Tab hinzufügen
        self.add_tab(DM.get_data(r'random_data.csv'))

    def add_tab(self, data):
        tab = QWidget()
        layout = QVBoxLayout()

        # Tabelle erstellen
        table = QTableWidget(data.shape[0], data.shape[1])
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                table.setItem(i, j, QTableWidgetItem(str(data[i, j])))

        layout.addWidget(table)
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, "Dataset")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())