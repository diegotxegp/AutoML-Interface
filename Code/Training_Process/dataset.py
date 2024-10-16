import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text, scrolledtext
import pandas as pd
from datetime import datetime
import shutil
from pathlib import Path

from master_table import file_formats
from descriptions import dataset_label_text, dataset_help_description
from utils import split_frame

class Dataset:
    def __init__(self, name, description, path, related_project):
        self.name = name
        self.description = description
        self.path = path
        self.file_format = None  # Completar
        self.related_project = related_project
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"Dataset(name={self.name}, description={self.description}, path={self.path}, timestamp={self.timestamp})"

class DatasetManager:
    def __init__(self, notebook, train_process):
        self.frame = tk.Frame(notebook)
        self.training_process = train_process  # Reference to train_process
        self.datasets = []

    def draw_frame(self):
        left_frame, right_frame = split_frame(self.frame)
        
        self.dataset_manager_frame(left_frame)
        self.description_frame(right_frame)

    def dataset_manager_frame(self, frame):
        self.load_datasets(frame)

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, dataset_help_description)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)

    def load_datasets(self, frame):
        """
        Load list of datasets for the selected project.
        """
        for widget in frame.winfo_children():
            widget.destroy()

        self.datasets.clear()

        dataset_label = tk.Label(frame, text=dataset_label_text)
        dataset_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        self.dataset_listbox = tk.Listbox(frame)
        self.dataset_listbox.pack(fill=tk.BOTH, expand=True)

        project = self.training_process.configuration.project
        datasets_dir = os.path.join(project.path, "Datasets")

        if os.path.exists(datasets_dir):
            # Recorre todos los subdirectorios en datasets_dir
            for dataset_dir in sorted(os.listdir(datasets_dir)):
                dataset_path = os.path.join(datasets_dir, dataset_dir)
                
                if os.path.isdir(dataset_path):
                    # Recorre todos los archivos en el subdirectorio actual
                    for root, dirs, files in os.walk(dataset_path):
                        for file in files:
                            # Separa el nombre del archivo de su extensión
                            file_name, file_extension = os.path.splitext(file)

                            # Filtra solo los archivos que tienen el mismo nombre que el subdirectorio
                            if file_name == dataset_dir:
                                file_path = os.path.join(root, file)

                                # Leer la descripción si existe
                                description_file = os.path.join(root, 'description.txt')
                                description = ''
                                if os.path.exists(description_file):
                                    with open(description_file, 'r') as f:
                                        description = f.read().strip()

                                dataset = Dataset(
                                    name=f"{file_name}{file_extension}",
                                    description=description,
                                    path=file_path,
                                    related_project=project
                                )

                                self.datasets.append(dataset)
                                self.dataset_listbox.insert(tk.END, dataset.name)

        self.search_button = tk.Button(frame, text="Add a dataset", command=self.add_dataset)
        self.search_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.select_button = tk.Button(frame, text="Select a dataset", command=self.select_dataset)
        self.select_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_dataset(self):
        path = filedialog.askopenfilename(
            title="Add a dataset file",
            filetypes=file_formats
        )

        if path:
            project = self.training_process.configuration.project
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

                self.load_datasets(self.frame)  # Agregar el frame correcto

            else:
                messagebox.showerror("Error", "A dataset with that name already exists.")

    def select_dataset(self):
        selected_index = self.dataset_listbox.curselection()

        if selected_index:
            selected_dataset = self.datasets[selected_index[0]]
            self.training_process.configuration.dataset = selected_dataset
            
            messagebox.showinfo("Dataset Selected",
                                f"Name: {selected_dataset.name}\n"
                                f"Description: {selected_dataset.description}\n"
                                f"Path: {selected_dataset.path}\n"
                                f"Timestamp: {selected_dataset.timestamp}")
            
            self.training_process.enable_next_tab()
        else:
            messagebox.showwarning("Warning", "Please select a dataset.")

    def ask_description(self):
        """
        Ask a description for the dataset.
        """
        description_window = tk.Toplevel(self.frame)  # El parent debe ser un widget de Tkinter, aquí es self.frame
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

        self.frame.wait_window(description_window)  # Aquí llamamos a wait_window desde self.frame, que es un widget de Tkinter

        return getattr(self, 'dataset_description', '')
