import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text, ttk
from datetime import datetime

class Configuration:
    def __init__(self, name, description, path, related_dataset, timestamp=None):
        self.name = name
        self.description = description
        self.path = path
        self.related_dataset = related_dataset
        self.timestamp = timestamp if timestamp else datetime.now()


class Preprocess(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)

        self.main_app = main_app  # Reference to the main application
        self.configurations = []

        label = tk.Label(self, text="No dataset selected.")
        label.pack(pady=10)

    def question_tabs(self):
        """
        Show a series of tabs with a question for each to know about the dataset introduced
        """
        for widget in self.winfo_children():
            widget.destroy()

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Additional tabs
        for tab_name in ["Configuration file","Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name)