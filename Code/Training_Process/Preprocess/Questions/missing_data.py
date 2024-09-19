import tkinter as tk
from tkinter import ttk

from master_table import missing_data_options
from descriptions import missing_data_label_text
from utils import split_frame

class MissingData:
    def __init__(self, notebook, preprocess, configuration):
        self.frame = tk.Frame(notebook)

        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

    def draw_frame(self):
        left_frame, right_frame = split_frame(self.frame)

        self.missing_data_frame(left_frame)
        self.description_frame(right_frame)

    def missing_data_frame(self, frame):
        label = tk.Label(frame, text=missing_data_label_text)
        label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        combo = ttk.Combobox(frame, values=missing_data_options)
        combo.pack(side=tk.TOP, anchor="w", padx=5, pady=5)
        combo.set(missing_data_options[0])

        self.ok_button = tk.Button(self, text="Ok", command=lambda:self.ok(combo.get()))
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)
    
    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

    def ok(self, value):
        self.configuration.set_missing_data(value)
        self.preprocess.enable_next_question_tab()