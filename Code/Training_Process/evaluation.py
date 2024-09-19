import tkinter as tk
from tkinter import scrolledtext

from descriptions import info_text
from utils import split_frame

class Evaluation:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        self.training_process = training_process

    def draw_frame(self):
        left_frame, right_frame = split_frame(self.frame)

        self.evaluation_frame(left_frame)
        self.description_frame(right_frame)

    def evaluation_frame(self, frame):
        # Text widget
        info_box = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, info_text)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)

        self.ok_button = tk.Button(self.frame, text="Ok", command=lambda:self.training_process.enable_next_tab())
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)