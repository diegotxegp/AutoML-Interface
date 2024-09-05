import tkinter as tk
from tkinter import ttk, PanedWindow

from master_table import separators, separator_label_text, paned_window

class Separator(tk.Frame):
    def __init__(self, notebook, preprocess, configuration):
        super().__init__(notebook)

        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

        left_frame, right_frame = paned_window(self)

        self.separator_frame(left_frame)
        self.description_frame(right_frame)

    def separator_frame(self, frame):
        label = tk.Label(frame, text=separator_label_text)
        label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        combo = ttk.Combobox(frame, values=separators)
        combo.pack(side=tk.TOP, anchor="w", padx=5, pady=5)
        combo.set(separators[0])

        ok_button = tk.Button(self, text="Ok", command=lambda:self.ok(combo.get()))
        ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

    def ok(self, value_separator):
        self.configuration.set_separator(value_separator)
        self.preprocess.enable_next_question_tab()
