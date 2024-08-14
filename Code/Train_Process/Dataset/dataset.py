import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text
from datetime import datetime
import shutil
from pathlib import Path

from master_table import filetypes

class Dataset:
    def __init__(self, name, description, path, related_project, timestamp = None):
        self.name = name
        self.description = description
        self.path = path
        self.related_project = related_project
        self.timestamp = timestamp if timestamp else datetime.now()

    def __repr__(self):
        return f"Dataset(name={self.name}, description={self.description}, path={self.path}, timestamp={self.timestamp})"

class DatasetManager(tk.Frame):
    def __init__(self, parent, train_process):
        super().__init__(parent)

        self.train_process = train_process  # Reference to train_process
        self.datasets = []

        label = tk.Label(self, text="No project selected.")
        label.pack(pady=10)

    def load_datasets(self, project):
        """
        Load list of datasets for the selected project.
        """
        for widget in self.winfo_children():
            widget.destroy()

        self.datasets.clear()

        self.dataset_listbox = tk.Listbox(self)
        self.dataset_listbox.pack(fill=tk.BOTH, expand=True)

        datasets_dir = os.path.join(project.path, "Datasets")

        if os.path.exists(datasets_dir):
            dataset_dirs = sorted(os.listdir(datasets_dir))

            for dataset_dir in dataset_dirs:
                dataset_path = os.path.join(datasets_dir, dataset_dir)

                description_file = os.path.join(dataset_path, 'description.txt')
                description = ''
                if os.path.exists(description_file):
                    with open(description_file, 'r') as file:
                        description = file.read().strip()

                timestamp = datetime.fromtimestamp(os.path.getctime(dataset_path))

                dataset = Dataset(
                    name=dataset_dir,
                    description=description,
                    path=dataset_path,
                    related_project = project,
                    timestamp=timestamp
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
            filetypes=filetypes # Filetypes saved in master_table
        )

        if path:
            try:
                project = self.train_process.get_selected_project()
                datasets_dir = os.path.join(project.path, "Datasets")
                
                if not os.path.exists(datasets_dir):
                    os.makedirs(datasets_dir)

                path = Path(path)                
                dataset_name = path.stem
                new_dataset_dir = os.path.join(datasets_dir, dataset_name)
                
                if not os.path.exists(new_dataset_dir):
                    os.makedirs(new_dataset_dir)

                    shutil.copy(path, new_dataset_dir)

                    description = self.ask_description()
                    if description:
                        description_file_path = os.path.join(new_dataset_dir, "description.txt")
                        with open(description_file_path, "w") as desc_file:
                            desc_file.write(description)

                    messagebox.showinfo("Success", "Dataset added successfully")

                    self.load_datasets(project)

                else:
                    messagebox.showerror("Error", "A dataset with that name already exists.")

            except Exception as e:
                messagebox.showerror("Error", f"File cannot be loaded: {e}")

    def select_dataset(self):
        selected_index = self.dataset_listbox.curselection()

        if selected_index:
            selected_dataset = self.datasets[selected_index[0]]
            self.train_process.set_selected_dataset(selected_dataset)
            
            messagebox.showinfo("Dataset Selected",
                                f"Name: {selected_dataset.name}\n"
                                f"Description: {selected_dataset.description}\n"
                                f"Path: {selected_dataset.path}\n"
                                f"Timestamp: {selected_dataset.timestamp}")
        else:
            messagebox.showwarning("Warning", "Please select a dataset.")

    def ask_description(self):
        """
        Ask a description for the dataset.
        """
        description_window = tk.Toplevel(self)
        description_window.title("Dataset Description")
        description_window.geometry("400x300+100+100")  # Open description window at (100, 100) on the screen

        description_label = tk.Label(description_window, text="Enter the description of the new dataset:")
        description_label.pack(pady=10)

        description_text = Text(description_window, height=10)
        description_text.pack(fill=tk.BOTH, expand=True)

        def on_ok():
            self.dataset_description = description_text.get("1.0", tk.END).strip()
            description_window.destroy()

        button_frame = tk.Frame(description_window)
        button_frame.pack(fill=tk.X)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        self.wait_window(description_window)  # Wait until description is completed

        return getattr(self, 'dataset_description', '')
