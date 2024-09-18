import os
import tkinter as tk
from tkinter import simpledialog, messagebox, Text
from datetime import datetime

# Path to the projects directory
PROJECTS_DIR = "Projects"

class Project:
    def __init__(self, name, description, path):
        self.name = name
        self.description = description
        self.path = path
        self.timestamp = datetime.now()

class ProjectManager:
    def __init__(self, notebook, training_process):

        self.frame = tk.Frame(notebook)
        self.training_process = training_process  # Reference to train_process
        
        self.projects = []

    def draw_frame(self):

        self.project_listbox = tk.Listbox(self.frame)
        self.project_listbox.pack(fill=tk.BOTH, expand=True)
        
        self.load_projects()

        self.select_button = tk.Button(self.frame, text="Select a project", command=self.select_project)
        self.select_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.new_project_button = tk.Button(self.frame, text="Create a new project", command=self.create_new_project)
        self.new_project_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def load_projects(self):
        """
        Load the list of projects
        """
        self.project_listbox.delete(0, tk.END)
        self.projects.clear()

        if os.path.exists(PROJECTS_DIR):
            project_dirs = sorted(os.listdir(PROJECTS_DIR))

            for project_dir in project_dirs:
                project_path = os.path.join(PROJECTS_DIR, project_dir)

                description_file = os.path.join(project_path, 'description.txt')
                description = ''
                if os.path.exists(description_file):
                    with open(description_file, 'r') as file:
                        description = file.read().strip()

                project = Project(
                    name=project_dir,
                    description=description,
                    path=project_path
                )

                self.projects.append(project)
                self.project_listbox.insert(tk.END, project.name)

    def create_new_project(self):
        """
        Create a new project along with a brief description.
        """
        new_project_name = simpledialog.askstring("New Project", "Enter the name of the new project:", parent=self)

        if new_project_name:
            new_project_path = os.path.join(PROJECTS_DIR, new_project_name)

            if not os.path.exists(new_project_path):
                os.makedirs(new_project_path)

                new_project_description = self.ask_description()
                if new_project_description:
                    description_file_path = os.path.join(new_project_path, "description.txt")
                    with open(description_file_path, "w") as desc_file:
                        desc_file.write(new_project_description)

                messagebox.showinfo("Project Created", f"The project '{new_project_name}' has been created at: {new_project_path}")

                self.load_projects()
            else:
                messagebox.showerror("Error", "A project with that name already exists.")

    def select_project(self):
        """
        Select the project chosen in the list of projects.
        """
        selected_index = self.project_listbox.curselection()

        if selected_index:
            selected_project = self.projects[selected_index[0]]
            self.training_process.configuration.project = selected_project

            # Show a message with details of the selected project
            messagebox.showinfo("Project Selected",
                                f"Name: {selected_project.name}\n"
                                f"Description: {selected_project.description}\n"
                                f"Path: {selected_project.path}\n"
                                f"Timestamp: {selected_project.timestamp}")
            
            self.training_process.enable_next_tab()

        else:
            messagebox.showwarning("Warning", "Please select a project.")

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

        self.wait_window(description_window)  # Wait until description is completed

        return getattr(self, 'project_description', '')
