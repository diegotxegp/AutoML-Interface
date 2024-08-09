# File: Code/Projects/projects.py

import os
import tkinter as tk
from tkinter import simpledialog, messagebox, Text
from datetime import datetime

# Path to the projects directory
PROJECTS_DIR = "Projects"

class Project:
    def __init__(self, name, description='', path='', created_at=None):
        self.name = name
        self.description = description
        self.path = path
        self.created_at = created_at if created_at else datetime.now()

    def __repr__(self):
        return f"Project(name={self.name}, description={self.description}, directory={self.path}, created_at={self.created_at})"
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_path(self):
        return self.path
    
    def get_created_at(self):
        return self.created_at

class ProjectManager(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)

        self.main_app = main_app  # Reference to the main application

        self.projects = []

        self.project_listbox = tk.Listbox(self)
        self.project_listbox.pack(fill=tk.BOTH, expand=True)
        
        self.load_projects()

        self.select_button = tk.Button(self, text="Select Project", command=self.select_project)
        self.select_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.new_project_button = tk.Button(self, text="Create New Project", command=self.create_new_project)
        self.new_project_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def load_projects(self):
        """
        Load the list of projects
        """
        self.project_listbox.delete(0, tk.END)
        self.projects.clear()

        if os.path.exists(PROJECTS_DIR):
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
                    name=project_dir,
                    description=description,
                    path=project_path,
                    created_at=created_at
                )

                self.projects.append(project)
                self.project_listbox.insert(tk.END, project.name)

    def select_project(self):
        """
        Select the project chosen in the list of projects
        """
        selected_index = self.project_listbox.curselection()

        if selected_index:
            selected_project = self.projects[selected_index[0]]
            self.main_app.set_selected_project(selected_project)

            # Show a message with details of the selected project
            messagebox.showinfo("Project Selected",
                                f"Name: {selected_project.name}\n"
                                f"Description: {selected_project.description}\n"
                                f"Path: {selected_project.path}\n"
                                f"Created At: {selected_project.created_at}")
        else:
            messagebox.showwarning("Warning", "Please select a project.")

    def create_new_project(self):
        new_project_name = simpledialog.askstring("New Project", "Enter the name of the new project:", parent=self)

        if new_project_name:
            new_project_desc = self.ask_description()
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

        def on_ok():
            self.project_description = description_text.get("1.0", tk.END).strip()
            description_window.destroy()

        button_frame = tk.Frame(description_window)
        button_frame.pack(fill=tk.X)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        self.wait_window(description_window) # Wait until description completed

        return getattr(self, 'project_description', '')
