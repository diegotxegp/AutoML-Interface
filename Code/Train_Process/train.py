import tkinter as tk

from ludwigML import Ludwig

class Train(tk.Frame):
    def __init__(self, notebook, train_process):
        super().__init__(notebook)
        
        self.train_process = train_process
        self.configuration = self.train_process.get_configuration()

        # Create a frame for the buttons to keep them together
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)  # Expand to fill the available space

        # Create the 'Train' button and add it to the button_frame
        train_button = tk.Button(button_frame, text="Automatic", command=self.automatic, width=20, height=2)
        train_button.pack(pady=(0, 10))  # Add some space below

        # Create the 'Predict' button and add it to the button_frame
        predict_button = tk.Button(button_frame, text="Semiautomatic", command=self.semiautomatic, width=20, height=2)
        predict_button.pack(pady=(10, 0))  # Add some space above

    def automatic(self):
        df = self.configuration.get_dataset().read_file()
        target = self.configuration.get_target()

        model = Ludwig.automl(df, "class")

    def semiautomatic(self):
        a = 3
