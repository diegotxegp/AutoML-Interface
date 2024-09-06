import tkinter as tk

class Mode(tk.Frame):
    def __init__(self, notebook, train_process):
        # Button frame
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)

        # Run AutoML automatically
        automl_button = tk.Button(button_frame, text="Automatic ML", command=self.train_process, width=20, height=2)
        automl_button.pack(pady=(0, 10))

        # Generate a config from dataset
        semiml_button = tk.Button(button_frame, text="Semiautomatic ML", command=self.train_process, width=20, height=2)
        semiml_button.pack(pady=(10, 0))