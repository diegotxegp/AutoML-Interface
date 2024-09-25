import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from Ludwig.ludwig import Ludwig

from Training_Process.info import Info
from Training_Process.project import ProjectManager
from Training_Process.dataset import DatasetManager
from Training_Process.mode import Mode
from Training_Process.Preprocess.preprocess import Preprocess
from Training_Process.summary import Summary
from Training_Process.train import Train
from Training_Process.evaluation import Evaluation

from utils import popup
from master_table import training_tab_names, automl_framework

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
        self.automl_framework = None

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

    def autoconfig(self):
        """
        Generate a configuration file from the dataset
        """
        self.automl_framework = globals()[automl_framework](self.configuration)
        self.automl_framework.autoconfig()

        print(self.automl_framework.config)

        self.enable_next_tab()

    def train(self):
        self.automl_framework.train()

        model_dir = os.path.dirname(self.configuration.dataset.path)+"/model"

        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        self.automl_framework.model.save(model_dir)
        self.automl_framework.model.save_config(model_dir)

        self.enable_next_tab()

    def compare_performance(self):
        self.automl_framework.compare_performance()

    def confusion_matrix(self):
        self.automl_framework.confusion_matrix()