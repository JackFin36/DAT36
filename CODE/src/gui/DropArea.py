from PyQt6 import QtWidgets, QtCore, uic
import pandas as pd

class DropArea(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)  # Enable drag and drop
        self.setText("Drag and drop your data files here")
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")

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
                self.process_file(file_path)    # Process the file

    def process_file(self, file_path):
        # Example function to process the imported file
        self.setText(f"File imported: {file_path}")
        # You can add your data import logic here (e.g., read CSV, JSON, etc.)
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
                print("CSV Data:", data)
            elif file_path.endswith('.json'):
                data = pd.read_json(file_path)
                print("JSON Data:", data)
            elif file_path.endswith('.txt'):
                data = pd.read_csv(file_path, delim_whitespace=True, header=None)
                print("TXT Data:", data)
            else:
                self.setText("Unsupported file type.")
        except Exception as e:
            self.setText(f"Error importing file: {str(e)}")