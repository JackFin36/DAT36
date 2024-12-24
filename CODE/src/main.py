import sys
from PyQt6 import QtWidgets, uic, QtCore
sys.path.append(r'CODE\src\gui')
from MainWindow import MainWindow
      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())