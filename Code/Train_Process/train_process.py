import tkinter as tk
from tkinter import ttk

from Train_Process.Project.project import ProjectManager
from Train_Process.Dataset.dataset import DatasetManager
from Train_Process.Preprocess.preprocess import Preprocess
from Train_Process.Configuration.configuration import Configuration
from Train_Process.info import Info

class TrainProcess:
    def __init__(self, main):
        self.main = main

        self.configuration = Configuration()

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.create_tabs()

    def create_tabs(self):
        """
        Create tabs for each section (Projects, Datasets, Preprocess, etc.).
        """
        # Info tab
        frame = Info(self.notebook)
        self.notebook.add(frame, text="Info")
        # Project tab
        self.project_manager = ProjectManager(self.notebook, self)
        self.notebook.add(self.project_manager, text="Select a project")

        # Dataset tab
        self.dataset_manager = DatasetManager(self.notebook, self)
        self.notebook.add(self.dataset_manager, text="Add a dataset")

        # Preprocess tab
        self.preprocess = Preprocess(self.notebook, self)
        self.notebook.add(self.preprocess, text="Some questions")

        # Pestañas adicionales
        for tab_name in ["Train", "Metrics of performance"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name)

    def set_selected_project(self, project):
        """
        Set project to work
        """
        self.configuration.selected_project = project
        self.dataset_manager.load_datasets(self.configuration.selected_project)

    def get_selected_project(self):
        return self.configuration.selected_project
    
    def set_selected_dataset(self, dataset):
        """
        Set dataset to work
        """
        self.configuration.selected_dataset = dataset
        self.preprocess.question_tabs
