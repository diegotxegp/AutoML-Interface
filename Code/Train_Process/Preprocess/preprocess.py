import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text, ttk
from datetime import datetime

from Train_Process.Preprocess.Questions.separator import Separator
from Train_Process.Preprocess.Questions.missing_data import MissingData
from Train_Process.Preprocess.Questions.input_features import InputFeatures
from Train_Process.Preprocess.Questions.input_feature_types import InputFeatureTypes
from Train_Process.Preprocess.Questions.target import Target
from Train_Process.Preprocess.Questions.target_types import TargetTypes
from Train_Process.Preprocess.Questions.depends_on_time import DependsOnTime
from Train_Process.Preprocess.Questions.metrics import Metrics

from master_table import enable_next_tab

"""class Configuration:
    def __init__(self, name, description, path, related_dataset, timestamp=None):
        self.name = name
        self.description = description
        self.path = path
        self.related_dataset = related_dataset
        self.timestamp = timestamp if timestamp else datetime.now()"""


class Preprocess(tk.Frame):
    def __init__(self, notebook, train_process):
        super().__init__(notebook)

        self.parent_notebook = notebook

        self.train_process = train_process  # Reference to the main application

        label = tk.Label(self, text="No dataset selected.")
        label.pack(pady=10)

        self.create_question_tabs()

    def create_question_tabs(self):
        """
        Show a series of tabs with questions to know about the dataset introduced
        """
        for widget in self.winfo_children():
            widget.destroy()

        # Create the notebook (tab container)
        self.question_notebook = ttk.Notebook(self)
        self.question_notebook.pack(fill=tk.BOTH, expand=True)

        separator = Separator(self.question_notebook, self)
        self.question_notebook.add(separator, text="Separator")

        missing_data = MissingData(self.question_notebook, self)
        self.question_notebook.add(missing_data, text="Missing data?", state="disabled")

        input_features = InputFeatures(self.question_notebook, self)
        self.question_notebook.add(input_features, text="Input features", state="disabled")

        input_feature_types = InputFeatureTypes(self.question_notebook, self)
        self.question_notebook.add(input_feature_types, text="Input feature types", state="disabled")

        target = Target(self.question_notebook, self)
        self.question_notebook.add(target, text="Target", state="disabled")

        target_types = TargetTypes(self.question_notebook, self)
        self.question_notebook.add(target_types, text="Target types", state="disabled")

        depends_on_time = DependsOnTime(self.question_notebook, self)
        self.question_notebook.add(depends_on_time, text="Does it depend on time?", state="disabled")

        metrics = Metrics(self.question_notebook, self)
        self.question_notebook.add(metrics, text="Metrics", state="disabled")

    def enable_next_question_tab(self):
        if enable_next_tab(self.question_notebook) == False:
            enable_next_tab(self.parent_notebook)
