# main_window.py

import os
import sys
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from PyQt5.QtGui import QIcon

# Import the tab classes
from gui.tabs.batch_processing_tab import BatchProcessingTab  # Import the new BatchProcessingTab

def resource_path(relative_path):
    """Get the absolute path to a resource, works for development and PyInstaller."""
    try:
        # PyInstaller creates a temporary folder and stores its path in sys._MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Batch Wiz Pro by Hossein Ostovar")
        self.setGeometry(100, 100, 1200, 800)

        self.init_ui()

        # Load the stylesheet
        self.apply_stylesheet()

    def init_ui(self):
        # Create the tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Initialize tabs

        self.batch_processing_tab = BatchProcessingTab()  # Pass the general tab

        # Add tabs to the tab widget with icons

        batch_processing_icon_path = resource_path('gui/resources/batch_processing_icon.png')

        self.setWindowIcon(QIcon(resource_path('gui/resources/icon.png')))

        self.tabs.addTab(self.batch_processing_tab, QIcon(batch_processing_icon_path), "Batch Processing")  # Add the new tab

        # Optionally, set the default tab
        #self.tabs.setCurrentWidget()

    def apply_stylesheet(self):
        """Load the global stylesheet."""
        stylesheet_path = resource_path('style.qss')
        if os.path.exists(stylesheet_path):
            with open(stylesheet_path, 'r') as f:
                self.setStyleSheet(f.read())
        else:
            print(f"Warning: stylesheet not found at {stylesheet_path}")
