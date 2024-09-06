import tkinter as tk
from tkinter import scrolledtext

from descriptions import info_text
from utils import enable_next_tab

class Summary(tk.Frame):
    def __init__(self, notebook, training_process):
        super().__init__(notebook)

        self.training_process = training_process

        # Text widget
        info_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, info_text)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)

        self.ok_button = tk.Button(self, text="Ok", command=lambda:self.training_process.enable_next_tab())
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)