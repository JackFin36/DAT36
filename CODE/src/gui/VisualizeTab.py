import os
import sys
import numpy as np
from PyQt6 import QtWidgets, uic
import pyqtgraph as pg
from pyqtgraph import PlotWidget
sys.path.append(r"C:\Users\duong\Desktop\DATool\DAT36-main\CODE\src\classes")
from DataManager import DataManager

class VisualizeTab(QtWidgets.QWidget):
    def __init__(self, MainWindow, data_manager: DataManager):
        super().__init__()
        uic.loadUi(r'C:\Users\duong\Desktop\DATool\DAT36-main\CODE\ui\VisualizeTab.ui', self)  # Lade die UI-Datei

        self.DM = data_manager
        self.MW = MainWindow
        self.DiagType = None
        # Widgets zuweisen
        
        self.PlotWindow = self.findChild(PlotWidget, "PlotArea")
        # General Settings
        self.diagramTypeCB = self.findChild(QtWidgets.QComboBox, "DiagramTypeComboBox")
        self.nameXAxisTE = self.findChild(QtWidgets.QTextEdit, "NameXAxisTextEdit")
        self.nameYAxisTE = self.findChild(QtWidgets.QTextEdit, "NameYAxisTextEdit")
        self.plotTitleTE  = self.findChild(QtWidgets.QTextEdit, "PlotTitleTextBox")
        self.showGridChB = self.findChild(QtWidgets.QCheckBox, "ShowGridCheckBos")
        self.showLegendChB = self.findChild(QtWidgets.QCheckBox, "ShowLegendCheckBox")
        self.applyGenerals = self.findChild(QtWidgets.QPushButton, "ApplyGeneralSettingsButton")
        # Graph Settings
        self.applyGraphSettingsButton = self.findChild(QtWidgets.QPushButton, "ApplyGraphSettingsButton")
        self.colourCB = self.findChild(QtWidgets.QComboBox, "ColourComboBox")
        self.graphNameTE = self.findChild(QtWidgets.QTextEdit, "GraphNameTextEdit")
        self.lineTypeCB = self.findChild(QtWidgets.QComboBox, "LineTypeComboBox")
        self.selectGraphCB = self.findChild(QtWidgets.QComboBox, "SelectGraphComboBox")
        # Export Layout
        self.exportButton = self.findChild(QtWidgets.QPushButton, "ExportButton")
        self.selectFileTypeCB = self.findChild(QtWidgets.QComboBox, "SelectFileTypeComboBox")
        # fill the DiagramType ComboBox
        diagTypes = ['Line Plot', 'Scatter Plot', 'Bar Plot', 'Boxplot', 'Heatmap', '3D Plot']
        self.diagramTypeCB.addItems(diagTypes)
        # Verbindungen einrichten
        self.applyGenerals.clicked.connect(self.applyGs)
        self.diagramTypeCB.currentIndexChanged.connect(self.setDiagType)

    def applyGs(self):
        x_selection = self.DM.selected_x
        y_selection = self.DM.selected_y
        print(x_selection, y_selection)
        X = self.DM.get_data(self.DM.selected_file, x_selection)
        Y = self.DM.get_data(self.DM.selected_file, y_selection)
        self.create_plot_test(X,Y)


    def setDiagType(self, index):    
        selected_item = self.diagramTypeCB.itemText(index)
        self.DiagType = selected_item

    def scattery(self, X, Y):
        self.PlotWindow.clear()
        self.PlotWindow.setBackground('w')
        self.PlotWindow.addLegend()
        self.PlotWindow.showGrid(x=True,y=True)
        self.PlotWindow.setLabel('left','y-Data')
        self.PlotWindow.setLabel('bottom','x-Data')
        
        scatter = pg.ScatterPlotItem(x=X, y=Y, pen=pg.mkPen('b', width=2), brush=pg.mkBrush(255, 0, 0, 120))
        self.PlotWindow.addItem(scatter)

    def create_plot(self, x, y):
        # Clear previous plots (optional)
        self.PlotWindow.clear()
        
        # Sort the data
        sorted_indices = np.argsort(x)
        x_sorted = np.array(x, dtype=float)[sorted_indices]
        y_sorted = np.array(y, dtype=float)[sorted_indices]
    
        if self.DiagType == 'Line Plot':
            plot = pg.PlotDataItem(x_sorted,y_sorted,pen=pg.mkPen('b', width=2))
            self.PlotWindow.addItem(plot)
        
        elif self.DiagType == 'Scatter Plot':
            scatter = pg.ScatterPlotItem(x, y, pen=pg.mkPen('b', width=2), brush=pg.mkBrush(255, 0, 0, 120))
            self.PlotWindow.addItem(scatter)

        elif self.DiagType == 'Bar Plot':
            bar = pg.BarGraphItem(x=x_sorted,height=y_sorted, width = 1.)
            self.PlotWindow.addItem(bar)  # Bar plot
        
        elif self.DiagType == 'Boxplot':
            # Boxplot logic here (requires additional implementation)
            pass
        
        elif self.DiagType == 'Heatmap':
            # Heatmap logic here (requires additional implementation)
            pass
        
        elif self.DiagType == '3D Plot':
            # 3D plot logic here (requires additional implementation)
            pass


    def create_plot_test(self, x, y):
        # Clear previous plots (optional)
        self.PlotWindow.clear()
        try:
            sorted_indices = np.argsort(x)
            x_sorted = np.array(x, dtype=float)[sorted_indices]
            y_sorted = np.array(y, dtype=float)[sorted_indices]
            opt = 1
        except ValueError:
            try:
                x_strings = np.array(x, dtype=str)
                y_floats = np.array(y, dtype=float)
                opt = 2
            except ValueError:
                x_strings = np.array(y, dtype=str)
                y_floats = np.array(x, dtype=float)
                opt = 2
            except Exception as e:
                print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

        # Check if x and y contain numeric data
        if opt == 1:
            # Sort the data
            sorted_indices = np.argsort(x)
            x_sorted = np.array(x, dtype=float)[sorted_indices]
            y_sorted = np.array(y, dtype=float)[sorted_indices]

            if self.DiagType == 'Line Plot':
                plot = pg.PlotDataItem(x_sorted, y_sorted, pen=pg.mkPen('b', width=2))
                self.PlotWindow.addItem(plot)

            elif self.DiagType == 'Scatter Plot':
                scatter = pg.ScatterPlotItem(x_sorted, y_sorted, pen=pg.mkPen('b', width=2), brush=pg.mkBrush(255, 0, 0, 120))
                self.PlotWindow.addItem(scatter)

            elif self.DiagType == 'Bar Plot':
                bar = pg.BarGraphItem(x=x_sorted, height=y_sorted, width=1.0)
                self.PlotWindow.addItem(bar)

        elif opt == 2:

            if self.DiagType == 'Bar Plot':
                x_pos = np.arange(len(x_strings))  # Set x positions for bars
                bar = pg.BarGraphItem(x0=x_pos - 0.4, x1=x_pos + 0.4, height=y_floats)
                self.PlotWindow.addItem(bar)
                self.PlotWindow.getAxis('bottom').setTicks([list(zip(x_pos, x_strings))])  # Set x-ticks to names
                

            elif self.DiagType == 'Line Plot':
                x_pos = np.arange(len(x))  # Use indices for the x-axis
                line_plot = pg.PlotDataItem(x_pos, y_floats, pen=pg.mkPen('b', width=2))
                self.PlotWindow.addItem(line_plot)
                self.PlotWindow.getAxis('bottom').setTicks([list(zip(x_pos, x_strings))])  # Set x-ticks to names
                                
            elif self.DiagType == 'Scatter Plot':
                x_pos = np.arange(len(x))  # Use indices for the x-axis
                scatter_plot = pg.ScatterPlotItem(x_pos, y_floats, pen=pg.mkPen('b', width=2), brush=pg.mkBrush(255, 0, 0, 120))
                self.PlotWindow.addItem(scatter_plot)
                self.PlotWindow.getAxis('bottom').setTicks([list(zip(x_pos, x_strings))])  # Set x-ticks to names
                
        else:
            print("Invalid data types provided for plotting.")