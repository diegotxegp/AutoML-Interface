import tkinter as tk
from tkinter import ttk

from master_table import input_features_label_text

class InputFeatures(tk.Frame):
    def __init__(self, notebook, preprocess, configuration):
        super().__init__(notebook)

        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

        input_features_label = tk.Label(self, text=input_features_label_text)
        input_features_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        df = self.configuration.get_dataset().read_file()
        input_features = df.columns.toList()

        seleccion = []
        for i, opcion in enumerate(input_features):
            var = tk.IntVar()  # Variable que controla si el Checkbutton está seleccionado o no
            chk = ttk.Checkbutton(self, text=opcion, variable=var)
            chk.pack(anchor='w', pady=2)
            seleccion.append(var)

        self.ok_button = tk.Button(self, text="Ok", command=lambda:self.preprocess.enable_next_question_tab())
        self.ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

