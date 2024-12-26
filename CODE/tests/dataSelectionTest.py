import sys 
sys.path.append(r'C:\Users\duong\Desktop\DATool\DAT36-main\CODE\src\classes')
from DataManager import DataManager

DM = DataManager()
DM.process_file(r'random_data.csv')

import numpy as np
X = DM.get_data(r'random_data.csv', 'Alter')
Y = DM.get_data(r'random_data.csv', 'Einkommen')
y = np.array([97545, 77544, 41147, 90401, 37721, 80081, 25207, 95424, 82290, 93561])
x = np.array([35, 46, 55, 19, 18, 45, 32, 49, 25, 43])
print(y)
print(Y)
print(type(y), type(Y))
print(np.array_equal(y,Y))
#plt.plot(X,Y)
#plt.show()
    
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication  # Importiere QApplication

# PyQtGraph-Anwendung erstellen
app = QApplication([])  # Verwende QApplication

# Plot-Fenster erstellen
plot_widget = pg.plot(title="Beispielplot")
#plot_widget.plot(X, Y, pen='b')  # x und y sind NumPy Arrays

# Streudiagramm erstellen
scatter = pg.ScatterPlotItem(x=X, y=Y, pen=pg.mkPen('b', width=2), brush=pg.mkBrush(255, 0, 0, 120))  # blaue Umrandung, rote Füllung
plot_widget.addItem(scatter)

# Fenster anzeigen
pg.QtGui.QGuiApplication.exec()  # Verwende exec() für das Fenster-Loop