import tkinter as tk

class Train(tk.Frame):
    def __init__(self, notebook, train_process):
        super().__init__(notebook)
        
        self.train_process = train_process
        self.configuration = train_process.get_configuration()

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
        from ludwig.automl import auto_train
        from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split

        

        split_df = get_repeatable_train_val_test_split(self.df, self.target, random_seed=42)

    def semiautomatic(self):
        from ludwig.automl import create_auto_config
        from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split

        a = 3
