import tkinter as tk
from tkinter import ttk

from master_table import separators

class TimeDependable:
    def __init__(self, notebook, preprocess):
        self.frame = tk.Frame(notebook)

        self.notebook = notebook
        self.preprocess = preprocess  # Reference to preprocess

        label_separator = tk.Label(self.frame, text="Which separator among columns does your data use?")
        label_separator.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        value_separator = ttk.Combobox(self.frame, values=separators)
        value_separator.pack(side=tk.TOP, anchor="w", padx=5, pady=5)
        value_separator.set(separators[0])

        self.ok_button = tk.Button(self.frame, text="Ok", command=lambda:self.preprocess.enable_next_question_tab())
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

