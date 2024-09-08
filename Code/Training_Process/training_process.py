import tkinter as tk
from tkinter import ttk
from datetime import datetime

from Training_Process.ludwigML import Ludwig

from Training_Process.info import Info
from Training_Process.project import ProjectManager
from Training_Process.dataset import DatasetManager
from Training_Process.mode import Mode
from Training_Process.Preprocess.preprocess import Preprocess
from Training_Process.summary import Summary
from Training_Process.train import Train

from utils import enable_next_tab

class Configuration:
    def __init__(self):        
        self.project = None
        self.dataset = None
        self.path = None
        self.timestamp = datetime.now()
        self.config = None
        self.input_features = None
        self.target = None
        self.algorithm = None
        self.fileformat = None
        self.separator = None
        self.missing_data = None
        self.runtime = None
        self.maximize_minimize = None
        self.metrics = None

class TrainingProcess:
    def __init__(self, main):

        self.dataset_manager = None # Hacer que dataset_manager se ejecute cuando detecte que cambia a su pestaña
        self.configuration = Configuration()

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(main)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.create_training_tabs()

    def create_training_tabs(self):
        """
        Create tabs for each section (Projects, Datasets, Preprocess, etc.).
        """
        # Info tab
        info = Info(self.notebook)
        self.notebook.add(info, text="Info")

        # Project tab
        project_manager = ProjectManager(self.notebook, self)
        self.notebook.add(project_manager, text="Project", state="disabled")

        # Dataset tab
        self.dataset_manager = DatasetManager(self.notebook, self)
        self.notebook.add(self.dataset_manager, text="Dataset", state="disabled")

        # Mode tab
        mode = Mode(self.notebook, self)
        self.notebook.add(mode, text="Mode", state="disabled")

        # Questions tab
        preprocess = Preprocess(self.notebook, self)
        self.notebook.add(preprocess, text="Preprocess", state="disabled")

        # Summary tab
        summary = Summary(self.notebook, self)
        self.notebook.add(summary, text="Summary", state="disabled")

        # Train tab
        train = Train(self.notebook, self)
        self.notebook.add(train, text="Train", state="disabled")

        # Pestañas adicionales
        for tab_name in ["Evaluation"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name, state="disabled")

    def set_project(self, selected_project):
        """
        Set project to work
        """
        self.configuration.project = selected_project
        self.dataset_manager.load_datasets()
    
    def set_dataset(self, selected_dataset):
        """
        Set dataset to work
        """
        self.configuration.dataset = selected_dataset

    def enable_next_tab(self):
        """
        Enable the next tab
        """
        enable_next_tab(self.notebook)

    def semiml(self):
        self.ludwig = Ludwig(self.configuration.dataset.path)
        self.ludwig.autoconfig()
        print(self.ludwig.config)
