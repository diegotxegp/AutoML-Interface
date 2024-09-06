import tkinter as tk
from tkinter import ttk

from Training_Process.configuration import Configuration
from Training_Process.info import Info
from Training_Process.project import ProjectManager
from Training_Process.dataset import DatasetManager
from Training_Process.Preprocess.preprocess import Preprocess
from Training_Process.train import Train

from utils import enable_next_tab

class TrainingProcess:
    def __init__(self, main):
        self.main = main

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Windows
        self.info = None
        self.project_manager = None
        self.dataset_manager = None
        self.preprocess = None
        self.train = None

        self.configuration = Configuration()

        self.create_training_tabs()

    def create_training_tabs(self):
        """
        Create tabs for each section (Projects, Datasets, Preprocess, etc.).
        """
        # Info tab
        self.info = Info(self.notebook)
        self.notebook.add(self.info, text="Info")

        # Project tab
        self.project_manager = ProjectManager(self.notebook, self)
        self.notebook.add(self.project_manager, text="Select a project", state="disabled")

        # Dataset tab
        self.dataset_manager = DatasetManager(self.notebook, self)
        self.notebook.add(self.dataset_manager, text="Select a dataset", state="disabled")

        """# Config tab
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="Config file", state="disabled")"""

        # Questions tab
        self.preprocess = Preprocess(self.notebook, self)
        self.notebook.add(self.preprocess, text="Some questions", state="disabled")

        """# Summary tab
        self.summary = Train(self.notebook, self)
        self.notebook.add(self.sumary, text="Summary", state="disabled")"""

        # Train tab
        self.train = Train(self.notebook, self)
        self.notebook.add(self.train, text="Train", state="disabled")

        # Pestañas adicionales
        for tab_name in ["Metrics of performance"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name, state="disabled")

    def set_selected_project(self, selected_project):
        """
        Set project to work
        """
        self.configuration.set_project(selected_project)
        self.dataset_manager.load_datasets()

    def get_selected_project(self):
        return self.configuration.get_project()
    
    def set_selected_dataset(self, selected_dataset):
        """
        Set dataset to work
        """
        self.configuration.set_dataset(selected_dataset)
        self.preprocess.create_question_tabs()

    def get_configuration(self):
        return self.configuration

    def enable_next_tab(self):
        enable_next_tab(self.notebook)
