import tkinter as tk

class Mode:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        self.training_process = training_process

    def draw_frame(self):
        # Button frame
        button_frame = tk.Frame(self.frame)
        button_frame.pack(expand=True)

        # Run AutoML automatically
        automl_button = tk.Button(button_frame, text="Automatic ML", command=self.training_process, width=20, height=2)
        automl_button.pack(pady=(0, 10))

        # Generate a configuration file from dataset
        semiml_button = tk.Button(button_frame, text="Semiautomatic ML", command=lambda:self.training_process.semiml(), width=20, height=2)
        semiml_button.pack(pady=(10, 0))