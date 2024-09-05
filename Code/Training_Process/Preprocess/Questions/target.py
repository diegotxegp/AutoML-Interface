import tkinter as tk
from tkinter import ttk

from master_table import target_label_text

class Target(tk.Frame):
    def __init__(self, notebook, preprocess, configuration):
        super().__init__(notebook)

        self.notebook = notebook
        self.preprocess = preprocess  # Reference to preprocess

        target_label = tk.Label(self, text=target_label_text)
        target_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        self.ok_button = tk.Button(self, text="Ok", command=lambda:self.ok)
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def ok(self, target):
        self.select_target
        self.configuration.set_target(target)
        self.preprocess.enable_next_question_tab()

    def select_target(self): ## Corregir
        df = self.configuration.get_dataset().read_file()

        features = self.df.columns.tolist()

        selected_target = tk.StringVar()
        selected_target.set(features[-1])

        for i, feature in enumerate(features):
            label = tk.Label(self.frame, text=feature)
            label.grid(row=i+1, column=0, padx=5, pady=5, sticky="ew")

            checkbox = tk.Radiobutton(self.frame, text="", variable=selected_target, value=feature)
            checkbox.grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")

