import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from master_table import preprocess_tab_names
from descriptions import evaluation_description
from utils import split_frame

class Evaluation:
    def __init__(self, notebook, training_process):
        self.frame = tk.Frame(notebook)
        self.training_process = training_process
        self.instance_list = []  # Inicializar lista de instancias
        self.configuration = {}  # Asegúrate de tener una configuración inicializada

    def draw_frame(self):
        # Dividir el frame en dos subframes usando pack, no grid.
        left_frame, right_frame = split_frame(self.frame)

        self.evaluation_frame(left_frame)
        self.description_frame(right_frame)

    def draw_evaluation_tabs(self):
        """
        Create tabs of the training process
        """
        # Crear el notebook (contenedor de pestañas)
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Dibujar la primera pestaña
        tab_name = preprocess_tab_names[0]
        tab_class = globals()[tab_name]
        tab_instance = tab_class(self.notebook, self, self.configuration)
        self.instance_list.append(tab_instance)
        tab_instance.draw_frame()
        self.notebook.add(tab_instance.frame, text=tab_name, state="normal")

        # Dibujar las pestañas restantes deshabilitadas
        for tab_name in preprocess_tab_names[1:]:
            tab_class = globals()[tab_name]
            tab_instance = tab_class(self.notebook, self, self.configuration)
            self.instance_list.append(tab_instance)
            self.notebook.add(tab_instance.frame, text=tab_name, state="disabled")

    def evaluation_frame(self, frame):
        # Frame para botones dentro del frame de evaluación
        button_frame = tk.Frame(frame)  # Colocar en el frame de evaluación
        button_frame.pack(expand=True)

        # Botón Compare Performance
        automl_button = tk.Button(button_frame, text="Compare Performance", command=lambda:self.training_process.compare_performance(), width=20, height=2)
        automl_button.pack(pady=(0, 10))

        # Botón Confusion Matrix
        semiml_button = tk.Button(button_frame, text="Confusion Matrix", command=lambda: self.training_process.confusion_matrix(), width=20, height=2)
        semiml_button.pack(pady=(10, 0))

    def description_frame(self, frame):
        # Label descriptivo
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, evaluation_description)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)
