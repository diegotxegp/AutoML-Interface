import tkinter as tk

from Ludwig.ludwig import Ludwig

from utils import split_frame

class Train:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        
        self.training_process = training_process
        self.configuration = self.training_process.configuration

    def draw_frame(self):
        left_frame, right_frame = split_frame(self.frame)

        self.train_frame(left_frame)
        self.description_frame(right_frame)

    def train_frame(self, frame):
        # Create a frame for the buttons to keep them together
        button_frame = tk.Frame(frame)
        button_frame.pack(expand=True)  # Expand to fill the available space

        # Create the 'Train' button and add it to the button_frame
        train_button = tk.Button(button_frame, text="Train", command=self.train, width=20, height=2)
        train_button.pack(pady=(0, 10))  # Add some space below

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

    def train(self):
        self.training_process.train()