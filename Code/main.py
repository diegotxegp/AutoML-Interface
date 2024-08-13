import os
import tkinter as tk
from tkinter import ttk, messagebox

from Projects.projects import ProjectManager
from Datasets.datasets import DatasetManager
from Preprocess.preprocess import Preprocess

class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("AutoML-Interface")
        self.geometry("800x600")  # Set main window size

        # Variables to store the selected project and dataset
        self.selected_project = None
        self.selected_dataset = None

        # Create the menu
        self.create_menu_bar()

        # Create the initial window with buttons
        self.create_initial_window()

    def create_initial_window(self):
        """
        Create the initial window with 'Train' and 'Predict' buttons.
        """
        self.initial_frame = tk.Frame(self)
        self.initial_frame.pack(fill=tk.BOTH, expand=True)

        train_button = tk.Button(self.initial_frame, text="Train", command=self.show_tabs, width=20, height=2)
        train_button.pack(pady=20)

        predict_button = tk.Button(self.initial_frame, text="Predict", command=self.show_tabs, width=20, height=2)
        predict_button.pack(pady=20)

    def show_tabs(self):
        """
        Show the tabs and hide the initial buttons.
        """
        self.initial_frame.pack_forget()
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.create_tabs()

    def create_tabs(self):
        """
        Create all the tabs (Projects, Datasets, Preprocess...).
        """
        # Project tab
        self.project_tab = ProjectManager(self.notebook, self)
        self.notebook.add(self.project_tab, text="Projects")

        # Dataset tab
        self.dataset_tab = DatasetManager(self.notebook, self)
        self.notebook.add(self.dataset_tab, text="Datasets")

        # Preprocess tab
        self.preprocess_tab = Preprocess(self.notebook, self)
        self.notebook.add(self.preprocess_tab, text="Preprocess")

        # Additional tabs
        for tab_name in ["Train", "Metrics", "Model", "Test", "Predict", "Results"]:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name)

    def reset_to_initial_window(self):
        """
        Reset the interface back to the initial window with 'Train' and 'Predict' buttons.
        """
        if hasattr(self, 'notebook'):
            self.notebook.pack_forget()
        self.create_initial_window()

    def create_menu_bar(self):
        """
        Create the menu bar with dropdown options.
        """
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Reset", command=self.reset_to_initial_window)
        file_menu.add_command(label="Train", command=self.show_tabs)
        file_menu.add_command(label="Predict", command=self.show_tabs)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def show_about(self):
        messagebox.showinfo("About", "AutoML-Interface v2.0\nDeveloped by Diego\n2024")

# Main
def main():
    app = MainApp()
    app.mainloop()

if __name__ == "__main__":
    main()
