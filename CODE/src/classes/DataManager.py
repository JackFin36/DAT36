import numpy as np
import pandas as pd
import json
import os

class DataManager():
    def __init__(self):
        self.datasets = {}  # Dictionary to store datasets with filenames as keys

    def import_csv(self, file_path):
        """Import a CSV file and convert it to a NumPy array."""
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            self.datasets[file_path] = df.to_numpy()
            print(f"Imported CSV: {file_path}")
        else:
            print(f"File not found: {file_path}")

    def import_json(self, file_path):
        """Import a JSON file and convert it to a NumPy array."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            # Convert to DataFrame and then to NumPy array
            df = pd.json_normalize(data)
            self.datasets[file_path] = df.to_numpy()
            print(f"Imported JSON: {file_path}")
        else:
            print(f"File not found: {file_path}")

    def import_txt(self, file_path):
        """Import a TXT file and convert it to a NumPy array."""
        if os.path.exists(file_path):
            # Assuming the TXT file is space-separated or tab-separated
            df = pd.read_csv(file_path, delim_whitespace=True, header=None)
            self.datasets[file_path] = df.to_numpy()
            print(f"Imported TXT: {file_path}")
        else:
            print(f"File not found: {file_path}")

    def get_data(self, file_path):
        """Retrieve the NumPy array for the given file path."""
        return self.datasets.get(file_path, None)

    def list_datasets(self):
        """List all imported datasets."""
        return list(self.datasets.keys())
