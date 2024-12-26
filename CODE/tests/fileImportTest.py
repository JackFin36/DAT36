import pandas as pd
import numpy as np

# Anzahl der Zeilen
num_rows = 10

# Erstelle zufällige Daten
#data = {
#    'Name': [f'Person {i+1}' for i in range(num_rows)],
#    'Alter': np.random.randint(18, 60, size=num_rows),
#    'Stadt': np.random.choice(['Berlin', 'München', 'Hamburg', 'Köln'], size=num_rows),
#    'Einkommen': np.random.randint(20000, 100000, size=num_rows)
#}

# Erstelle DataFrame
#df = pd.DataFrame(data)

# Speichere als CSV-Datei
#CSV_TEST = df.to_csv('random_data.csv', index=False)
#print("CSV-Datei 'random_data.csv' wurde erstellt.")
#JSON_TEST = df.to_json('random_data.json', index=False)
#print("JSON-Datei 'random_data.json' wurde erstellt.")
#

import sys 
sys.path.append(r'C:\Users\duong\Desktop\DATool\DAT36-main\CODE\src\classes')
from DataManager import DataManager

DM = DataManager()
DM.process_file(r'random_data.csv')
print(DM.get_allData(r'random_data.csv'))

DM.process_file(r'random_data.json')
print(DM.get_allData(r'random_data.json'))