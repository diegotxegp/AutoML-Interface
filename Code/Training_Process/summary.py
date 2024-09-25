import tkinter as tk
from tkinter import scrolledtext

from descriptions import summary_description
from utils import split_frame

class Summary:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        self.training_process = training_process
        self.configuration = self.training_process.configuration

    def draw_frame(self):
        left_frame, right_frame = split_frame(self.frame)

        self.summary_frame(left_frame)
        self.description_frame(right_frame)

    def summary_frame(self, frame):
        dataset_label = tk.Label(frame, text="Revise the chosen values before training")
        dataset_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        summary_text = (f"Project: {self.configuration.project.path}\n"
                f"Dataset: {self.configuration.dataset.path}\n"
                f"Samples: {self.configuration.samples}\n"
                f"Input features: {self.configuration.input_features}\n"
                f"Target: {self.configuration.target}\n"
                f"Separator: {self.configuration.separator}\n"
                f"Missing data: {self.configuration.missing_data}\n"
                f"Runtime: {self.configuration.runtime}\n"
                f"Metric: {self.configuration.metric}\n")

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=30, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, summary_text)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)

        self.ok_button = tk.Button(frame, text="Ok", command=lambda:self.training_process.enable_next_tab())
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, summary_description)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)