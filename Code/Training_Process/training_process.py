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
        self.timestamp = datetime.now()
        self.input_features = None
        self.target = None
        self.samples = None
        self.separator = None
        self.missing_data = None
        self.runtime = None
        self.metric = None

class TrainingProcess:
    def __init__(self, main):
        self.main = main
        self.dataset_manager = None # Hacer que dataset_manager se ejecute cuando detecte que cambia a su pestaña
        self.configuration = Configuration()

    def create_training_tabs(self):
        """
        Create tabs for each section (Projects, Datasets, Preprocess, etc.).
        """
        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Info tab
        info = Info(self.notebook)
        info.draw_frame()
        self.notebook.add(info.frame, text="Info", state="normal")

        # Project tab
        project_manager = ProjectManager(self.notebook, self)
        project_manager.draw_frame()
        self.notebook.add(project_manager.frame, text="Project", state="normal")

        # Dataset tab
        self.dataset_manager = DatasetManager(self.notebook, self)
        self.notebook.add(self.dataset_manager.frame, text="Dataset", state="normal")

        # Mode tab
        mode = Mode(self.notebook, self)
        mode.draw_frame()
        self.notebook.add(mode.frame, text="Mode", state="normal")

        # Questions tab
        preprocess = Preprocess(self.notebook, self)
        preprocess.draw_frame()
        self.notebook.add(preprocess.frame, text="Preprocess", state="normal")

        # Summary tab
        summary = Summary(self.notebook, self)
        self.notebook.add(summary, text="Summary", state="normal")

        # Train tab
        train = Train(self.notebook, self)
        self.notebook.add(train, text="Train", state="normal")

        # Pestañas adicionales
        for tab_name in ["Evaluation"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name, state="normal")

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

    def enable_next_tab_prueba(self, next_tab_index):
        """Enable the next tab and draw the frame"""
        self.notebook.tab(next_tab_index, state="normal")
        self.notebook.select(next_tab_index)
        self.create_tab_content(next_tab_index)

    def semiml(self):
        ludwig = Ludwig(self.configuration.dataset.path)
        ludwig.autoconfig()
        self.configuration.input_features = ludwig.input_features()
        self.configuration.target = ludwig.output_features()
        self.configuration.metric = ludwig.metric()
        self.configuration.runtime = ludwig.runtime()
        self.configuration.samples = ludwig.samples()

        self.enable_next_tab()
