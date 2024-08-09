# File: Code/Datasets/datasets.py

import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text
from datetime import datetime
import pandas as pd
import shutil

class Dataset:
    def __init__(self, name, description='', project = '', path='', created_at=None):
        self.name = name
        self.description = description
        self.path = path
        self.created_at = created_at if created_at else datetime.now()
        self.related_project = project

    def __repr__(self):
        return f"Dataset(name={self.name}, description={self.description}, path={self.path}, created_at={self.created_at})"
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_path(self):
        return self.path
    
    def get_created_at(self):
        return self.created_at
    
    def get_related_project(self):
        return self.related_project

class DatasetManager(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)

        self.main_app = main_app  # Reference to the main application

        self.datasets = []

        label = tk.Label(self, text="No project selected.")
        label.pack(pady=10)

    def load_datasets(self, project):
        """
        Load list of projects
        """
        for widget in self.winfo_children():
            widget.destroy()

        self.datasets.clear()

        self.dataset_listbox = tk.Listbox(self)
        self.dataset_listbox.pack(fill=tk.BOTH, expand=True)

        datasets_dir = os.path.join(project.path, "Datasets")

        if os.path.exists(datasets_dir):
            dataset_dirs = os.listdir(datasets_dir)
            sorted_dirs = sorted(dataset_dirs)

            for dataset_dir in sorted_dirs:
                dataset_path = os.path.join(datasets_dir, dataset_dir)
                description_file = os.path.join(dataset_path, 'description.txt')
                description = ''
                if os.path.exists(description_file):
                    with open(description_file, 'r') as file:
                        description = file.read().strip()
                created_at = datetime.fromtimestamp(os.path.getctime(dataset_path))

                dataset = Dataset(
                    name=dataset_dir,
                    description=description,
                    path=dataset_path,
                    created_at=created_at
                )

                self.datasets.append(dataset)
                self.dataset_listbox.insert(tk.END, dataset.name)

        self.search_button = tk.Button(self, text="Add dataset", command=self.add_dataset)
        self.search_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.select_button = tk.Button(self, text="Select Dataset", command=self.select_dataset)
        self.select_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_dataset(self):
        path = filedialog.askopenfilename(
            title="Add a dataset file",
            filetypes=[
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx;*.xls"),
                ("Feather files", "*.feather"),
                ("FWF files", "*.fwf"),
                ("HDF5 files", "*.h5;*.hdf5"),
                ("HTML files", "*.html;*.htm"),
                ("JSON files", "*.json;*.jsonl"),
                ("Parquet files", "*.parquet"),
                ("Pickle files", "*.pkl;*.pickle"),
                ("SAS files", "*.sas7bdat;*.xpt"),
                ("SPSS files", "*.sav"),
                ("Stata files", "*.dta"),
                ("TSV files", "*.tsv"),
                ("All files", "*.*")
            ]
        )

        if path:
            try:
                dataset_path = os.path.join(self.main_app.get_selected_project().path, "Datasets")

                if not os.path.exists(dataset_path):
                    os.makedirs(dataset_path)

                new_dataset_path = self.ask_description()
                if new_dataset_path:
                    description_file_path = os.path.join(new_dataset_path, "description.txt")
                    with open(description_file_path, "w") as desc_file:
                        desc_file.write(new_dataset_path)

                shutil.copy(path, dataset_path)

            except Exception as e:
                messagebox.showerror("Error", f"File cannot be loaded: {e}")

        self.load_datasets
        print("Dataset loaded successfully")

    def select_dataset(self):
        selected_index = self.dataset_listbox.curselection()

        if selected_index:
            selected_dataset = self.datasets[selected_index[0]]
            self.main_app.set_selected_dataset(selected_dataset)
            
            messagebox.showinfo("Dataset Selected",
                                f"Name: {selected_dataset.name}\n"
                                f"Description: {selected_dataset.description}\n"
                                f"Path: {selected_dataset.path}\n"
                                f"Created At: {selected_dataset.created_at}")
        else:
            messagebox.showwarning("Warning", "Please select a dataset.")

    def ask_description(self):
        """
        Ask a description for the project
        """
        description_window = tk.Toplevel(self)
        description_window.title("Project Description")
        description_window.geometry("400x300+100+100")  # Open description window at (100, 100) on the screen

        description_label = tk.Label(description_window, text="Enter the description of the new project:")
        description_label.pack(pady=10)

        description_text = Text(description_window, height=10)
        description_text.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(description_window)
        button_frame.pack(fill=tk.X)

        def on_ok():
            self.project_desciption = description_text.get("1.0", tk.END).strip()
            description_window.destroy()

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        self.wait_window(description_window) # Wait until description completed
        return getattr(self, 'project_description', '')