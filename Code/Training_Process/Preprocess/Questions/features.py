import tkinter as tk
from tkinter import ttk, scrolledtext

from master_table import features_io, input_feature_types, output_feature_types
from descriptions import features_help_description, features_label_text
from utils import split_frame

class Features:
    def __init__(self, notebook, preprocess, configuration):
        self.frame = tk.Frame(notebook) # Features frame
        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

    def draw_frame(self):
        self.left_frame, self.right_frame = split_frame(self.frame)

        self.features_frame(self.left_frame)
        self.description_frame(self.right_frame)

    def features_frame(self, frame):
        features = []

        row_counter = 1

        title_label = tk.Label(frame, text=features_label_text)
        title_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

        # input features
        for i_f, type in self.configuration.input_features.items():
            label = tk.Label(frame, text=i_f)
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")

            feature_io = ttk.Combobox(frame, values=features_io)
            feature_io.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
            feature_io.set("input")

            feature_type = ttk.Combobox(frame, values=input_feature_types)
            feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
            feature_type.set(type)

            features.append((i_f, feature_io, feature_type))

            row_counter += 1

        # target (output features)
        for target, type in self.configuration.target.items():
            label = tk.Label(frame, text=target)
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")

            feature_io = ttk.Combobox(frame, values=features_io)
            feature_io.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
            feature_io.set("output")

            feature_type = ttk.Combobox(frame, values=output_feature_types)
            feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
            feature_type.set(type)

            features.append((target, feature_io, feature_type))

            row_counter += 1

        ok_button = tk.Button(frame, text="Ok", command=lambda:self.ok(features))
        ok_button.grid(row=row_counter, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Text widget
        info_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
        info_box.pack(fill='both', expand=True)

        info_box.insert(tk.END, features_help_description)

        # Text editing disabled
        info_box.config(state=tk.DISABLED)      

    def feature_classifier(self, features):
        input_features = {}
        output_features = {}

        for feature_name, feature_io, feature_type in features:
            if feature_io.get() == "input":
                input_features[feature_name] = feature_type.get()

            if feature_io.get() == "output":
                output_features[feature_name] = feature_type.get()

        self.configuration.input_features = input_features
        self.configuration.target = output_features

    def ok(self, features):
        self.feature_classifier(features)
        self.preprocess.enable_next_tab()
