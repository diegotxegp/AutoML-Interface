import tkinter as tk
from tkinter import ttk

from Training_Process.Preprocess.Questions.separator import Separator
from Training_Process.Preprocess.Questions.missing_data import MissingData
from Training_Process.Preprocess.Questions.features import Features
from Training_Process.Preprocess.Questions.timedependable import TimeDependable
from Training_Process.Preprocess.Questions.metric import Metric

from utils import enable_next_tab
from master_table import preprocess_tab_names

class Preprocess:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        self.parent_notebook = notebook
        self.training_process = training_process  # Reference to the main application

        self.configuration = training_process.configuration

    def draw_frame(self):

        label = tk.Label(self.frame, text="No dataset selected.")
        label.pack(pady=10)

        self.draw_question_tabs()

    def draw_training_tabs(self):
        """
        Create tabs of the training process
        """
        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        tab_name = preprocess_tab_names[0]

        tab_class = globals()[tab_name]

        tab_instance = tab_class(self.notebook, self)
        self.instance_list.append(tab_instance)
        tab_instance.draw_frame()
        self.notebook.add(tab_instance.frame, text=tab_name, state="normal")

        for tab_name in preprocess_tab_names[1:]:
            tab_class = globals()[tab_name]
            tab_instance = tab_class(self.notebook, self)
            self.instance_list.append(tab_instance)
            self.notebook.add(tab_instance.frame, text=tab_name, state="disabled")

    def draw_question_tabs(self):
        """
        Show a series of tabs with questions to know about the dataset introduced
        """
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Create the notebook (tab container)
        self.question_notebook = ttk.Notebook(self.frame)
        self.question_notebook.pack(fill=tk.BOTH, expand=True)

        # Input features tab
        features = Features(self.question_notebook, self, self.configuration)
        features.draw_frame()
        self.question_notebook.add(features.frame, text="Features", state="normal")

        # Separator tab
        separator = Separator(self.question_notebook, self, self.configuration)
        self.question_notebook.add(separator, text="Separator", state="normal")

        # Missing data tab
        missing_data = MissingData(self.question_notebook, self, self.configuration)
        self.question_notebook.add(missing_data, text="Missing data?", state="normal")

        time_dependable = TimeDependable(self.question_notebook, self)
        self.question_notebook.add(time_dependable.frame, text="Does it depend on time?", state="normal")

        metrics = Metric(self.question_notebook, self)
        self.question_notebook.add(metrics, text="Metrics", state="normal")

    def enable_next_question_tab(self):
        if enable_next_tab(self.question_notebook) == False:
            enable_next_tab(self.parent_notebook)
