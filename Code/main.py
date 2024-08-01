# File: Code/main.py

import tkinter as tk
from tkinter import ttk
from Code.Projects.projects import ProjectManager

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("800x600")  # Set main window size

        # Variable to store the selected project
        self.selected_project = None

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the tabs
        self.create_tabs()

    def create_tabs(self):
        # Projects tab
        self.projects_tab = ProjectManager(self.notebook, self)
        self.notebook.add(self.projects_tab, text="Projects")

        # Tab2 to show datasets
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Tab2")
        self.update_tab2()

        # Add 7 more tabs
        for i in range(2, 9):
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=f"Tab {i+1}")

    def update_tab2(self):
        for widget in self.tab2.winfo_children():
            widget.destroy()
        
        if self.selected_project:
            label = tk.Label(self.tab2, text=f"Datasets for project: {self.selected_project.title}")
            label.pack(pady=10)

            # Placeholder for dataset list
            dataset_listbox = tk.Listbox(self.tab2)
            dataset_listbox.pack(fill=tk.BOTH, expand=True)

            # Dummy data for datasets
            datasets = ["Dataset1.csv", "Dataset2.csv", "Dataset3.csv"]
            for dataset in datasets:
                dataset_listbox.insert(tk.END, dataset)
        else:
            label = tk.Label(self.tab2, text="No project selected.")
            label.pack(pady=10)

    def set_selected_project(self, project):
        self.selected_project = project
        self.update_tab2()

def main():
    app = MainApp()
    app.mainloop()

if __name__ == "__main__":
    main()
