# File: Code/Projects/projects.py

import os
import tkinter as tk
from tkinter import simpledialog, messagebox, Text
from datetime import datetime

# Path to the projects directory
PROJECTS_DIR = "Projects"

class Project:
    def __init__(self, title, description='', directory='', created_at=None):
        self.title = title
        self.description = description
        self.directory = directory
        self.created_at = created_at if created_at else datetime.now()

    def __repr__(self):
        return f"Project(title={self.title}, description={self.description}, directory={self.directory}, created_at={self.created_at})"

class ProjectManager(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app  # Reference to the main application
        self.project_listbox = tk.Listbox(self)
        self.project_listbox.pack(fill=tk.BOTH, expand=True)

        self.projects = []
        self.load_projects()

        self.select_button = tk.Button(self, text="Select Project", command=self.select_project)
        self.select_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.new_project_button = tk.Button(self, text="Create New Project", command=self.create_new_project)
        self.new_project_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def load_projects(self):
        self.project_listbox.delete(0, tk.END)
        if os.path.exists(PROJECTS_DIR):
            self.projects.clear()
            project_dirs = os.listdir(PROJECTS_DIR)
            sorted_dirs = sorted(project_dirs)
            for project_dir in sorted_dirs:
                project_path = os.path.join(PROJECTS_DIR, project_dir)
                description_file = os.path.join(project_path, 'description.txt')
                description = ''
                if os.path.exists(description_file):
                    with open(description_file, 'r') as file:
                        description = file.read().strip()
                created_at = datetime.fromtimestamp(os.path.getctime(project_path))
                project = Project(
                    title=project_dir,
                    description=description,
                    directory=project_path,
                    created_at=created_at
                )
                self.projects.append(project)
                self.project_listbox.insert(tk.END, project.title)

    def select_project(self):
        selected_title = self.project_listbox.get(tk.ACTIVE)
        selected_project = next((proj for proj in self.projects if proj.title == selected_title), None)
        if selected_project:
            self.main_app.set_selected_project(selected_project)
            messagebox.showinfo("Project Selected",
                                f"Title: {selected_project.title}\n"
                                f"Description: {selected_project.description}\n"
                                f"Directory: {selected_project.directory}\n"
                                f"Created At: {selected_project.created_at}")
        else:
            messagebox.showwarning("Warning", "Please select a project.")

    def create_new_project(self):
        new_project_name = simpledialog.askstring("New Project", "Enter the name of the new project:", parent=self)
        if new_project_name:
            new_project_desc = self.get_project_description()
            new_project_path = os.path.join(PROJECTS_DIR, new_project_name)
            if not os.path.exists(new_project_path):
                os.makedirs(new_project_path)
                if new_project_desc:
                    desc_file_path = os.path.join(new_project_path, "description.txt")
                    with open(desc_file_path, "w") as desc_file:
                        desc_file.write(new_project_desc)
                self.load_projects()
                messagebox.showinfo("Project Created", f"The project '{new_project_name}' has been created at: {new_project_path}")
            else:
                messagebox.showerror("Error", "A project with that name already exists.")

    def get_project_description(self):
        desc_window = tk.Toplevel(self)
        desc_window.title("Project Description")
        desc_window.geometry("400x300+100+100")  # Open description window at (100, 100) on the screen

        desc_label = tk.Label(desc_window, text="Enter the description of the new project:")
        desc_label.pack(pady=10)

        desc_text = Text(desc_window, height=10)
        desc_text.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(desc_window)
        button_frame.pack(fill=tk.X)

        def on_ok():
            self.project_desc = desc_text.get("1.0", tk.END).strip()
            desc_window.destroy()

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        self.wait_window(desc_window)
        return getattr(self, 'project_desc', '')

