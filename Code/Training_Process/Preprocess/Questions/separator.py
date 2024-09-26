import tkinter as tk
from tkinter import ttk, scrolledtext

from master_table import separators
from descriptions import separator_label_text, separator_help_description
from utils import split_frame

class Separator:
    def __init__(self, notebook, preprocess, configuration):
        self.frame = tk.Frame(notebook)
        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

    def draw_frame(self):
        self.left_frame, self.right_frame = split_frame(self.frame)

        self.separator_frame(self.left_frame)
        self.description_frame(self.right_frame)

    def separator_frame(self, frame):
        label = tk.Label(frame, text=separator_label_text)
        label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        combo = ttk.Combobox(frame, values=separators)
        combo.pack(side=tk.TOP, anchor="w", padx=5, pady=5)
        combo.set(separators[0])

        ok_button = tk.Button(frame, text="Ok", command=lambda:self.ok(combo.get()))
        ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, separator_help_description)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)

    def ok(self, separator_value): 
        self.configuration.separator = separator_value
        self.preprocess.enable_next_tab()
