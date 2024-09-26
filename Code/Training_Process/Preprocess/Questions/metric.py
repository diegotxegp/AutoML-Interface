import tkinter as tk
from tkinter import ttk

from descriptions import metric_label_text
from master_table import metrics, goals
from utils import split_frame

class Metric:
    def __init__(self, notebook, preprocess, configuration):
        self.frame = tk.Frame(notebook)
        self.preprocess = preprocess  # Reference to preprocess
        self.configuration = configuration # Reference to configuration

    def draw_frame(self):
        self.left_frame, self.right_frame = split_frame(self.frame)

        self.metric_frame(self.left_frame)
        self.description_frame(self.right_frame)

    def metric_frame(self, frame):
        label = tk.Label(frame, text=metric_label_text)
        label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        # Metric
        metric_label = tk.Label(frame, text="Metric:")
        metric_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        feature_type = []
        for target, type in self.configuration.target.items():
            feature_type = type

        metric = ttk.Combobox(frame, values=metrics.get(feature_type))
        metric.pack(side=tk.TOP, anchor="w", padx=5, pady=5)
        metric.set(metrics.get(feature_type)[0])

        # Goal
        goal_label = tk.Label(frame, text="Goal:")
        goal_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

        goal = ttk.Combobox(frame, values=goals)
        goal.pack(side=tk.TOP, anchor="w", padx=5, pady=5)
        goal.set(goals[0])

        ok_button = tk.Button(frame, text="Ok", command=lambda:self.ok(metric.get(), goal.get()))
        ok_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def description_frame(self, frame):
        description_label = tk.Label(frame, text="Help description")
        description_label.pack(side=tk.TOP, anchor="w", padx=5, pady=5)

    def ok(self, metric, goal):
        self.configuration.metric = {metric: goal}
        self.preprocess.enable_next_tab()
