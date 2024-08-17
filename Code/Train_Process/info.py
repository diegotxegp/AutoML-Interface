import tkinter as tk
from tkinter import scrolledtext

from master_table import info_text, enable_next_tab

class Info(tk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)

        self.notebook = notebook

        # Text widget
        text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        text_widget.pack(fill='both', expand=True)

        text_widget.insert(tk.END, info_text)

        # Text editing disabled
        text_widget.config(state=tk.DISABLED)

        self.ok_button = tk.Button(self, text="Ok", command=lambda:enable_next_tab(self.notebook))
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)
