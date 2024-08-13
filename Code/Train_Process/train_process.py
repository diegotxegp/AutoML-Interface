import tkinter as tk
from tkinter import ttk

from Train_Process.Project.project import ProjectManager
from Train_Process.Dataset.dataset import DatasetManager
from Train_Process.Preprocess.preprocess import Preprocess
from Train_Process.Configuration.configuration import Configuration

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
        # Project tab
        self.project_manager = ProjectManager(self.notebook, self)
        self.notebook.add(self.project_manager, text="Project")

        # Dataset tab
        self.dataset_manager = DatasetManager(self.notebook, self)
        self.notebook.add(self.dataset_manager, text="Dataset")

        # Preprocess tab
        self.preprocess_tab = Preprocess(self.notebook, self)
        self.notebook.add(self.preprocess_tab, text="Preprocess")

        # Pestañas adicionales
        for tab_name in ["Train", "Metrics", "Info"]:
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
