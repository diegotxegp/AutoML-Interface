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
from master_table import training_tab_names

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
        self.instance_list = []

    def draw_training_tabs(self):
        """
        Create tabs of the training process
        """
        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        tab_name = training_tab_names[0]

        tab_class = globals()[tab_name]

        tab_instance = tab_class(self.notebook, self)
        self.instance_list.append(tab_instance)
        tab_instance.draw_frame()
        self.notebook.add(tab_instance.frame, text=tab_name, state="normal")

        for tab_name in training_tab_names[1:]:
            tab_class = globals()[tab_name]
            tab_instance = tab_class(self.notebook, self)
            self.instance_list.append(tab_instance)
            self.notebook.add(tab_instance.frame, text=tab_name, state="disabled")

    def enable_next_tab(self):
        """
        Enable the next shadowed tab
        """
        current_tab = self.notebook.index('current')
        total_tabs = len(self.notebook.tabs())
        
        if current_tab < total_tabs - 1:
            next_tab = current_tab + 1
            self.notebook.tab(next_tab, state="normal")
            self.notebook.select(next_tab)

            self.instance_list[next_tab].draw_frame()

    def semiml(self):
        ludwig = Ludwig(self.configuration.dataset.path)
        ludwig.autoconfig()
        self.configuration.input_features = ludwig.input_features()
        self.configuration.target = ludwig.output_features()
        self.configuration.metric = ludwig.metric()
        self.configuration.runtime = ludwig.runtime()
        self.configuration.samples = ludwig.samples()

        self.enable_next_tab()
