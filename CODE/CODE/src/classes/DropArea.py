from PyQt6 import QtWidgets, QtCore, uic
import pandas as pd
import os

class DropArea(QtWidgets.QTabWidget):
    def __init__(self, DM, Import):
        super().__init__()
        self.setAcceptDrops(True)  # Enable drag and drop
        self.DM = DM
        self.Import = Import
    def dragEnterEvent(self, event):
        # Check if the dragged item is a file
        if event.mimeData().hasUrls():
            event.acceptProposedAction()  # Accept the drag action

    def dragMoveEvent(self, event):
        # Accept the move event
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Handle the dropped files
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()  # Get the file path
                self.DM.process_file(file_path)    # Process the file
                filename = os.path.basename(file_path)
                self.Import.display_data_in_tabs(self.DM.get_data(file_path), self.DM.get_headers(file_path), filename)
