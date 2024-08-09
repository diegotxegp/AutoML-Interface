import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text
from datetime import datetime

class Configuration:
    def __init__(self, name, description, path, dataset, timestamp=None):
        self.name = name
        self.description = description
        self.path = path
        self.related_dataset = dataset
        self.timestamp = timestamp if timestamp else datetime.now()


class Preprocess(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)

        self.main_app = main_app  # Reference to the main application
        self.configurations = []

        label = tk.Label(self, text="No dataset selected.")
        label.pack(pady=10)