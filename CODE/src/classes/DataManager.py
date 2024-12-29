import numpy as np
import pandas as pd
import json
import os

class DataManager():
    def __init__(self):
        self.datasets = {}  # Dictionary to store datasets with filenames as keys
        self.headers = {}   # Dictionary to store headers of the datasets with filenames as keys
        self.selected_file = None # Placeholder for later file selection
        self.selected_x = None
        self.selected_y = None

    def import_csv(self, file_path):
        """Import a CSV file and convert it to a NumPy array, also extracting headers."""
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            
            # Versuche, alle Spalten in Floats zu konvertieren, wo möglich
            for column in df.columns:
                df[column] = pd.to_numeric(df[column], errors='ignore')  # Behalte Strings

            self.datasets[file_path] = df.to_numpy()
            
            # Extract headers
            headers = df.columns.tolist()
            self.headers[file_path] = headers 
            
            print(f"Imported CSV: {file_path} with headers: {headers}")
        else:
            print(f"File not found: {file_path}")
            
    def import_json(self, file_path):
        """Import a JSON file and convert it to a NumPy array."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            # Convert to DataFrame and then to NumPy array
            df = pd.DataFrame(data)
            self.datasets[file_path] = df.to_numpy()
            headers = df.columns.tolist()
            self.headers[file_path] = headers  

            print(f"Imported JSON: {file_path} with headers: {headers}")
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

    def process_file(self, file_path):
            """Process the imported data file."""
            try:
                if file_path.endswith('.csv'):
                    self.import_csv(file_path)
                elif file_path.endswith('.json'):
                    self.import_json(file_path)
                elif file_path.endswith('.txt'):
                    self.import_txt(file_path)
                else:
                    print("Unsupported file type.")
            except Exception as e:
                print(f"Error importing file: {e}")

    def get_allData(self, file_path):
        """Retrieve the NumPy matrix for the given file path."""
        return self.datasets.get(file_path, None)
    
    def get_data(self, file_path, header):
        """Retrieve the NumPy array for the given file path based on the header."""
        Matrix = self.get_allData(file_path)
        if Matrix is not None and header in self.headers[file_path]:
            column_index = self.headers[file_path].index(header)
            return Matrix[:, column_index]  # Return the entire column corresponding to the header
        return None
    
    def get_headers(self, file_path):
        """Retrieve the headers from NumPy array for the given file path."""
        return self.headers.get(file_path, None)

    def list_datasets(self):
        """List all imported datasets (filenames)."""
        return list(self.datasets.keys())

    def selectData(self, file_path, keys=[]):
        """ Create a new dataset for further analysis with given keys"""
        dataset = self.datasets.get(file_path)
        if dataset is not None:
            return {key: dataset[key] for key in keys if key in dataset}
        return None