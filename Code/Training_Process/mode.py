import tkinter as tk
from tkinter import scrolledtext

from descriptions import mode_description
from utils import split_frame

class Mode:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        self.training_process = training_process

    def draw_frame(self):
        left_frame, right_frame = split_frame(self.frame)
        
        self.mode_frame(left_frame)
        self.description_frame(right_frame)

    def mode_frame(self, frame):
        dataset_label = tk.Label(frame, text="Choose a mode to train the model")
        dataset_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Button frame
        button_frame = tk.Frame(frame)
        button_frame.pack(expand=True)

        # Run AutoML automatically
        automl_button = tk.Button(button_frame, text="Automatic ML", command=self.training_process.auto_train, width=20, height=2)
        automl_button.pack(pady=(0, 10))

        # Generate a configuration file from dataset
        semiml_button = tk.Button(button_frame, text="Semiautomatic ML", command=lambda:self.training_process.autoconfig(), width=20, height=2)
        semiml_button.pack(pady=(10, 0))

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, mode_description)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)