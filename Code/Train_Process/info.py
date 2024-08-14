import tkinter as tk
from tkinter import scrolledtext

from master_table import info_text

class Info(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Text widget
        text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        text_widget.pack(fill='both', expand=True)

        text_widget.insert(tk.END, info_text)

        # Deshabilitar la edición del texto (opcional)
        text_widget.config(state=tk.DISABLED)
