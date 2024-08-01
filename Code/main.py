# File: Code/main.py

import os
import tkinter as tk
from tkinter import ttk

from Projects.projects import ProjectManager
from Datasets.datasets import DatasetManager

class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("AutoML-Interface")
        self.geometry("800x600")  # Set main window size

        # Variable to store the selected project
        self.selected_project = None

        # Create the menu
        self.create_menu()

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the tabs
        self.create_tabs()

    def create_menu(self):
        """
        Create the menu bar with dropdown options.
        """
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def create_tabs(self):
        """
        Create all the tabs
        """
        # Projects tab
        self.projects_tab = ProjectManager(self.notebook, self)
        self.notebook.add(self.projects_tab, text="Projects")

        # Datasets tab
        self.datasets_tab = DatasetManager(self.notebook)
        self.notebook.add(self.datasets_tab, text="Datasets")
        self.update_dataset_tab()

        # Add 7 more tabs
        for i in range(2, 9):
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=f"Tab {i+1}")

    def update_dataset_tab(self):
        """
        Update dataset tab according to the project selected.
        """
        for widget in self.datasets_tab.winfo_children():
            widget.destroy()
        
        if self.selected_project:
            datasets_dir = os.path.join(self.selected_project.directory, "Datasets")

            if os.path.exists(datasets_dir) and os.path.isdir(datasets_dir):
                dataset_listbox = tk.Listbox(self.datasets_tab)
                dataset_listbox.pack(fill=tk.BOTH, expand=True)

                datasets = os.listdir(datasets_dir)
                
                if datasets:
                    for dataset in datasets:
                        dataset_listbox.insert(tk.END, dataset)
                else:
                    label = tk.Label(self.datasets_tab, text="No datasets found in 'Datasets' folder.")
                    label.pack(pady=10)
            else:
                label = tk.Label(self.datasets_tab, text="Datasets folder does not exist.")
                label.pack(pady=10)
        else:
            label = tk.Label(self.datasets_tab, text="No project selected.")
            label.pack(pady=10)

    def set_selected_project(self, project):
        """
        Set the project to work
        """
        self.selected_project = project
        self.update_dataset_tab()

    def show_about(self):
        tk.messagebox.showinfo("About", "AutoML-Interface v2.0\nDeveloped by Diego\n2024")

def main():
    app = MainApp()
    app.mainloop()

if __name__ == "__main__":
    main()
