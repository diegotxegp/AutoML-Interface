import tkinter as tk
from tkinter import ttk

from master_table import input_feature_types
from utils import split_frame

feature_classes = ["input", "output", ""]

class Features:
    def __init__(self, notebook, preprocess, configuration):
        self.frame = tk.Frame(notebook)

        self.preprocess = preprocess  # Referencia a preprocess
        self.configuration = configuration # Referencia a configuration

        # Usando grid() para organizar left_frame y right_frame
        self.left_frame = tk.Frame(self.frame)
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        self.right_frame = tk.Frame(self.frame)
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        self.frame.grid_columnconfigure(0, weight=1)  # Expandir columnas
        self.frame.grid_columnconfigure(1, weight=1)

    def draw_frame(self):
        row_counter = 1

        # Para las características de entrada
        for i_f, type in self.configuration.input_features.items():
            label = tk.Label(self.left_frame, text=i_f)
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")

            feature_class = ttk.Combobox(self.left_frame, values=feature_classes)
            feature_class.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
            feature_class.set("input")

            feature_type = ttk.Combobox(self.left_frame, values=input_feature_types)
            feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
            feature_type.set(type)

            row_counter += 1

        # Para las características de salida
        for o_f, type in self.configuration.target.items():
            label = tk.Label(self.left_frame, text=o_f)
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")

            feature_class = ttk.Combobox(self.left_frame, values=feature_classes)
            feature_class.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
            feature_class.set("output")

            feature_type = ttk.Combobox(self.left_frame, values=input_feature_types)
            feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
            feature_type.set(type)

            row_counter += 1
