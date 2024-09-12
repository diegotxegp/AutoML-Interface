import tkinter as tk
from tkinter import ttk

from master_table import input_feature_types
from utils import split_frame

feature_classes = ["input", "output", ""]

class Features:
    def __init__(self, notebook, preprocess, configuration):
        self.frame = tk.Frame(notebook)

        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

        self.left_frame, self.right_frame = split_frame(self.frame)

        #self.features_frame(self.left_frame)


    def features_frame(self, frame):
        row_counter = 1

        for i_f, type in self.configuration.input_features.items():
              
            label = tk.Label(frame, text = i_f)
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")

            feature_class = ttk.Combobox(frame, values=feature_classes)
            feature_class.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
            feature_class.set("input")

            feature_type = ttk.Combobox(frame, values=input_feature_types)
            feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
            feature_type.set(type)

            row_counter += 1

        for i_f, type in self.configuration.output_features.items():
              
            label = tk.Label(frame, text = i_f)
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")

            feature_class = ttk.Combobox(frame, values=feature_classes)
            feature_class.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
            feature_class.set("output")

            feature_type = ttk.Combobox(frame, values=input_feature_types)
            feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
            feature_type.set(type)

            row_counter += 1