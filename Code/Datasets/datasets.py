# File: Code/Datasets/datasets.py

import os
import tkinter as tk
from tkinter import simpledialog, messagebox, Text
from datetime import datetime

class Dataset:
    def __init__(self, name, description='', type = '', version = '', format = '', directory='', created_at=None):
        self.name = name
        self.description = description
        self.type = type # Train - Validation - Test - Prediction
        self.version = version
        self.format = format
        self.directory = directory
        self.created_at = created_at if created_at else datetime.now()

    def __repr__(self):
        return f"Dataset(name={self.name}, description={self.description}, directory={self.directory}, created_at={self.created_at})"

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

        datasets_dir = os.path.join(project.directory, "Datasets")

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
                    directory=dataset_path,
                    created_at=created_at
                )

                self.datasets.append(dataset)
                self.dataset_listbox.insert(tk.END, dataset.name)

        self.select_button = tk.Button(self, text="Select Dataset", command=self.select_dataset)
        self.select_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.search_button = tk.Button(self, text="Add dataset", command=self.add_dataset)
        self.search_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def select_dataset(self):
        selected_name = self.dataset_listbox.get(tk.ACTIVE)
        selected_dataset = next((ds for ds in self.datasets if ds.name == selected_name), None)
        if selected_dataset:
            self.main_app.set_selected_dataset(selected_dataset)
            messagebox.showinfo("Dataset Selected",
                                f"Name: {selected_dataset.name}\n"
                                f"Description: {selected_dataset.description}\n"
                                f"Directory: {selected_dataset.directory}\n"
                                f"Created At: {selected_dataset.created_at}")
        else:
            messagebox.showwarning("Warning", "Please select a dataset.")

    def add_dataset(self):
        search_term = simpledialog.askstring("Search Dataset", "Enter the name of the dataset to search:", parent=self)
        if search_term:
            found = False
            for dataset in self.datasets:
                if search_term.lower() in dataset.name.lower():
                    messagebox.showinfo("Dataset Found",
                                        f"Name: {dataset.name}\n"
                                        f"Description: {dataset.description}\n"
                                        f"Directory: {dataset.directory}\n"
                                        f"Created At: {dataset.created_at}")
                    found = True
                    break
            if not found:
                messagebox.showinfo("No Dataset Found", f"No dataset found with the name containing '{search_term}'.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dataset Manager")
    root.geometry("600x400")
    app = DatasetManager(root, main_app=None)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
