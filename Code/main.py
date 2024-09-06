import tkinter as tk
from tkinter import ttk, messagebox, font

from Training_Process.training_process import TrainingProcess
from descriptions import welcome_title, welcome_text

class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("AutoML-Interface")
        self.geometry("800x600")  # Set main window size

        # Create the menu bar
        self.create_menu_bar()

        # Create the initial window
        self.create_initial_frame()

    def create_initial_frame(self):
        """
        Initial frame with 'Train' and 'Predict' options.
        """
        self.initial_frame = tk.Frame(self)
        self.initial_frame.pack(fill=tk.BOTH, expand=True)

        # Create the welcome label with a larger and bold font
        welcome_font = font.Font(family="Helvetica", size=16, weight="bold")
        welcome_label = tk.Label(self.initial_frame, text=welcome_title, font=welcome_font)
        welcome_label.pack(pady=(20, 10), anchor="n")  # Positioned at the top

        # Add a paragraph below the welcome label
        paragraph_label = tk.Label(self.initial_frame, text=welcome_text)
        paragraph_label.pack(pady=(0, 20), anchor="n")  # Positioned below the welcome label

        # Create a frame for the buttons to keep them together
        button_frame = tk.Frame(self.initial_frame)
        button_frame.pack(expand=True)  # Expand to fill the available space

        # Create the 'Train' button and add it to the button_frame
        train_button = tk.Button(button_frame, text="Train a model", command=self.training_process, width=20, height=2)
        train_button.pack(pady=(0, 10))  # Add some space below the Train button

        # Create the 'Predict' button and add it to the button_frame
        predict_button = tk.Button(button_frame, text="Predict new data", command=self.training_process, width=20, height=2)
        predict_button.pack(pady=(10, 0))  # Add some space above the Predict button



    def training_process(self):
        """
        Init the train process.
        """
        self.initial_frame.pack_forget() # Hide the initial frame

        TrainingProcess(self) # Init the train process

    def reset_to_initial_frame(self):
        """
        Reset the interface back to the initial frame with 'Train' and 'Predict' options.
        """
        # Destroy the current initial_frame to ensure it's fully removed
        self.initial_frame.destroy()

        # Recreate the initial frame
        self.create_initial_frame()

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
        file_menu.add_command(label="Train", command=self.training_process)
        file_menu.add_command(label="Predict", command=self.training_process)

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
