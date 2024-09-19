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
        self.training_process = training_process # Reference to parent
        self.configuration = training_process.configuration
        self.instance_list = []

    def draw_frame(self):
        self.draw_question_tabs()

    def draw_question_tabs(self):
        """
        Create tabs of the training process
        """
        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        tab_name = preprocess_tab_names[0]

        tab_class = globals()[tab_name]

        tab_instance = tab_class(self.notebook, self, self.configuration)
        self.instance_list.append(tab_instance)
        tab_instance.draw_frame()
        self.notebook.add(tab_instance.frame, text=tab_name, state="normal")

        for tab_name in preprocess_tab_names[1:]:
            tab_class = globals()[tab_name]
            tab_instance = tab_class(self.notebook, self, self.configuration)
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

        else:
            self.training_process.enable_next_tab()
