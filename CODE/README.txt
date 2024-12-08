## author: Jack Fin Duong (OG)
## Data Analysis Tool in Python Optimized for Scientific Use
## Started 07.12.2024

DAT36 
│
├── /ui                         # Directory for UI files
│   ├── main_window.ui          # Main window UI file
│   ├── dialog.ui               # Dialog UI file
│   └── other_ui_files.ui       # Additional UI files
│
├── /src                        # Source code directory
│   ├── __init__.py             # Make src a package
│   ├── main.py                 # Main entry point of the application
│   ├── /classes                # Directory for functional object classes
│   │   ├── __init__.py
│   │   ├── data_manager.py      # Class for managing data imports
│   │   ├── other_functional_class.py  # Other functional classes
│   │   └── ...
│   │
│   ├── /gui                    # Directory for graphical object classes
│   │   ├── __init__.py
│   │   ├── main_window.py       # Main window class
│   │   ├── custom_dialog.py     # Custom dialog class
│   │   └── ...
│   │
│   ├── /utils                  # Utility functions/classes
│   │   ├── __init__.py
│   │   ├── error_handling.py    # Error handling protocol
│   │   └── other_utilities.py    # Other utility functions
│   │
│   └── /resources               # Directory for resources
│       ├── icons/               # Icons and images
│       ├── stylesheets/         # CSS stylesheets for the application
│       └── ...
│
├── /tests                      # Directory for unit tests
│   ├── __init__.py
│   ├── test_data_manager.py      # Tests for the DataManager class
│   ├── test_gui_classes.py        # Tests for GUI-related classes
│   └── ...
│
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation