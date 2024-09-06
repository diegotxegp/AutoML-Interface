import tkinter as tk

from ludwigML import Ludwig

class Mode(tk.Frame):
    def __init__(self, notebook, training_process):
        super().__init__(notebook)

        self.training_process = training_process

        # Button frame
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)

        # Run AutoML automatically
        automl_button = tk.Button(button_frame, text="Automatic ML", command=self.training_process, width=20, height=2)
        automl_button.pack(pady=(0, 10))

        # Generate a configuration file from dataset
        semiml_button = tk.Button(button_frame, text="Semiautomatic ML", command=lambda:self.semiml(), width=20, height=2)
        semiml_button.pack(pady=(10, 0))

    def semiml(self):
        ludwig = Ludwig()