import tkinter as tk
from tkinter import ttk

from Training_Process.configuration import Configuration
from Training_Process.info import Info
from Training_Process.project import ProjectManager
from Training_Process.dataset import DatasetManager
from Training_Process.mode import Mode
from Training_Process.Preprocess.preprocess import Preprocess
from Training_Process.summary import Summary
from Training_Process.train import Train

from utils import enable_next_tab

class TrainingProcess:
    def __init__(self, main):

        self.dataset_manager = None
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
        self.configuration.set_project(selected_project)
        self.dataset_manager.load_datasets()

    def get_project(self):
        return self.configuration.get_project()
    
    def set_dataset(self, selected_dataset):
        """
        Set dataset to work
        """
        self.configuration.set_dataset(selected_dataset)
        #self.preprocess.create_question_tabs()

    def get_configuration(self):
        return self.configuration

    def enable_next_tab(self):
        """
        Enable the next tab
        """
        enable_next_tab(self.notebook)