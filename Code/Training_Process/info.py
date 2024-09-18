import tkinter as tk
from tkinter import scrolledtext

from descriptions import info_text
from utils import enable_next_tab

class Info:
    def __init__(self, notebook, training_process):

        self.frame = tk.Frame(notebook)
        self.notebook = notebook
        self.training_process = training_process

    def draw_frame(self):
        # Text widget
        text_widget = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=50, height=15)
        text_widget.pack(fill='both', expand=True)

        text_widget.insert(tk.END, info_text)

        # Text editing disabled
        text_widget.config(state=tk.DISABLED)

        self.ok_button = tk.Button(self.frame, text="Ok", command=self.training_process.enable_next_tab)
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)
