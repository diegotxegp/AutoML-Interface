import tkinter as tk
from tkinter import messagebox
import pandas as pd

from ludwig.automl import auto_train, create_auto_config
from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split
from ludwig.visualize import compare_performance
from ludwig.visualize import confusion_matrix

class Ludwig:
    def __init__(self, dataset_path):
        self.df = self.read_file(dataset_path) # Dataframe from dataset file path

        columns = self.df.columns.tolist()
        self.target = columns[-1] # Last feature is commonly the target

        self.config = None
        self.model = None

    def read_file(self, dataset_path):
        """
        Read the dataframe of a file
        """
        try:
            if dataset_path.endswith((".csv", ".fwf", ".tsv")):
                    return pd.read_csv(dataset_path)
            elif dataset_path.endswith((".xlsx", ".xls")):
                return pd.read_excel(dataset_path)
            elif dataset_path.endswith((".feather")):
                return pd.read_feather(dataset_path)
            elif dataset_path.endswith((".h5", ".hdf5")):
                return pd.read_hdf(dataset_path)
            elif dataset_path.endswith((".html", ".htm")):
                return pd.read_html(dataset_path)[0]
            elif dataset_path.endswith((".json", ".jsonl")):
                return pd.read_json(dataset_path)
            elif dataset_path.endswith((".parquet")):
                return pd.read_parquet(dataset_path)
            elif dataset_path.endswith((".pkl", ".pickle")):
                return pd.read_pickle(dataset_path)
            elif dataset_path.endswith((".sas7bdat", ".xpt")):
                return pd.read_sas(dataset_path)
            elif dataset_path.endswith((".sav")):
                return pd.read_spss(dataset_path)
            elif dataset_path.endswith((".dta")):
                return pd.read_stata(dataset_path)
            else:
                messagebox.showwarning("Warning", "File format not compatible.")
                return

        except Exception as e:
            messagebox.showerror("Error", f"File cannot be loaded: {e}")

        print("Dataset loaded successfully")

    def automl(self, dataset_path):
        """
        Automatically trains a model.
        """
        messagebox.showinfo("Start", "AutoML-Interface starting...")

        split_df = get_repeatable_train_val_test_split(self.df, self.target, random_seed=42)

        auto_train_results = auto_train(
            dataset=split_df,
            target=self.target,
            time_limit_s=7200,
            tune_for_memory=False,
            user_config={'hyperopt': {'goal': 'maximize', 'metric': 'accuracy', 'output_feature': f"{self.target}"},
                'preprocessing': {'split': {'column': 'split', 'type': 'fixed'}}},
        )

        self.model = auto_train_results.best_model

        print("Model trained successfully")

    def autoconfig(self):
        """
        Automatically generates a configuration file.
        """
        self.split_df = get_repeatable_train_val_test_split(self.df, self.target, random_seed=42)

        self.config = create_auto_config(
            dataset=self.split_df,
            target=self.target,
            time_limit_s=7200,
            tune_for_memory=False,
            user_config={'hyperopt': {'goal': 'maximize', 'metric': 'accuracy', 'output_feature': f"{self.target}"}},
        )

        print("Config generated successfully")

    def input_features(self):
        input_feature_dict = {i_f["column"]: i_f['type'] for i_f in self.config["input_features"]}
        return input_feature_dict
    
    def output_features(self):
        output_feature_dict = {o_f["column"]: o_f['type'] for o_f in self.config["output_features"]}
        return output_feature_dict
    
    def metric(self):
        metric_dict = {self.config["hyperopt"]["metric"]:self.config["hyperopt"]["goal"]}
        return metric_dict
    
    def runtime(self):
        return self.config["hyperopt"]["executor"]["time_budget_s"]
    
    def samples(self):
        return self.config["hyperopt"]["executor"]["num_samples"]
    
    def set_features(self, configuration):
        """Set selected features into the config"""
        input_features = []
        output_features = []

        for feature_name, feature_type in configuration.input_features.items():
                feature = {
                    "name": feature_name,
                    "column": feature_name,
                    "type": feature_type
                }
                input_features.append(feature)

        for feature_name, feature_type in configuration.target.items():
                feature = {
                    "name": feature_name,
                    "column": feature_name,
                    "type": feature_type
                }
                output_features.append(feature)

        self.config["input_features"] = input_features
        self.config["output_features"] = output_features

        self.config["trainer"]["validation_field"] = output_features[0]["name"]
        self.config["hyperopt"]["output_feature"] = output_features[0]["name"]

        self.target = self.config["output_features"][0]["name"]
