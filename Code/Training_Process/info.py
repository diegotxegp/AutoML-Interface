import tkinter as tk
from tkinter import scrolledtext

from descriptions import info_text
from utils import enable_next_tab

class Info:
    def __init__(self, notebook):

        self.frame = tk.Frame(notebook)
        self.notebook = notebook

    def draw_frame(self):
        # Text widget
        text_widget = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=50, height=15)
        text_widget.pack(fill='both', expand=True)

        text_widget.insert(tk.END, info_text)

        # Text editing disabled
        text_widget.config(state=tk.DISABLED)

        self.ok_button = tk.Button(self.frame, text="Ok", command=lambda:enable_next_tab(self.notebook))
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)
