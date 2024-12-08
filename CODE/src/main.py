import sys
from PyQt6 import QtWidgets, uic, QtCore
sys.path.append(r'C:\Users\duong\Desktop\DATool\CODE\src\gui')
from MainWindow import MainWindow
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())