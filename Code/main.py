import tkinter as tk
from tkinter import ttk, messagebox

from Train_Process.train_process import TrainProcess

class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("AutoML-Interface")
        self.geometry("800x600")  # Set main window size

        # Create the menu bar
        self.create_menu_bar()

        # Create the initial window
        self.create_main_frame()

    def create_main_frame(self):
        """
        Initial frame with 'Train' and 'Predict' options.
        """
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        train_button = tk.Button(self.main_frame, text="Train", command=self.train_process, width=20, height=2)
        train_button.pack(pady=20)

        predict_button = tk.Button(self.main_frame, text="Predict", command=self.train_process, width=20, height=2)
        predict_button.pack(pady=20)

    def train_process(self):
        """
        Init the train process.
        """
        self.main_frame.pack_forget() # Hide the initial frame

        TrainProcess(self) # Init the train process

    def reset_to_initial_frame(self):
        """
        Reset the interface back to the initial frame with 'Train' and 'Predict' options.
        """
        # Destroy the current initial_frame to ensure it's fully removed
        self.main_frame.destroy()

        # Recreate the initial frame
        self.create_main_frame()

    def create_menu_bar(self):
        """
        Create the menu bar with dropdown options.
        """
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Reset", command=self.reset_to_initial_frame)
        file_menu.add_command(label="Train", command=self.train_process)
        file_menu.add_command(label="Predict", command=self.train_process)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def show_about(self):
        messagebox.showinfo("About", "AutoML-Interface v2.0\nDeveloped by Diego\n2024")


def main():
    app = MainApp()
    app.mainloop()

if __name__ == "__main__":
    main()
