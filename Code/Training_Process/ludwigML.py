import tkinter as tk
from tkinter import messagebox
import pandas as pd

from ludwig.automl import auto_train, create_auto_config
from ludwig.api import LudwigModel
from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split
from ludwig.visualize import compare_performance
from ludwig.visualize import confusion_matrix

class Ludwig:
    def __init__(self, configuration):
        self.configuration = configuration
        self.df = self.read_file(configuration.dataset.path) # Dataframe from dataset file path

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

        self.input_features()
        self.output_features()
        self.metric()
        self.runtime()
        self.samples()

    def train(self):
        """
        Train the model.
        """
        self.model = LudwigModel(self.config)
        self.model.train(dataset=self.df)

    def compare_performance(self):
        eval_stats, predictions, output_directory = self.model.evaluate(
            self.split_df,
            split="full",
            collect_predictions=True,
            collect_overall_stats=True,
            skip_save_eval_stats=False,
            skip_save_predictions=False,
            output_directory="results/test_results",
            return_type="dict"
        )

        from ludwig.visualize import compare_performance
        compare_performance(
            eval_stats,
            output_feature_name=self.target,
            model_names=None,
            output_directory=None,
            file_format='pdf'
        )

    def confusion_matrix(self):
        eval_stats, predictions, output_directory = self.model.evaluate(
            self.split_df,
            split="full",
            collect_predictions=True,
            collect_overall_stats=True,
            skip_save_eval_stats=False,
            skip_save_predictions=False,
            output_directory="results/test_results",
            return_type="dict"
        )

        from ludwig.visualize import confusion_matrix
        confusion_matrix(
            [eval_stats],
            self.model.training_set_metadata,
            output_feature_name = self.target,
            top_n_classes = [10],
            normalize=True,
            model_names=None,
            output_directory=None,
            file_format='pdf'
        )

    def input_features(self):
        self.configuration.input_features = {i_f["column"]: i_f['type'] for i_f in self.config["input_features"]}
    
    def output_features(self):
        self.configuration.target = {o_f["column"]: o_f['type'] for o_f in self.config["output_features"]}
    
    def metric(self):
        self.configuration.metric = {self.config["hyperopt"]["metric"]:self.config["hyperopt"]["goal"]}
    
    def runtime(self):
        self.configuration.runtime = self.config["hyperopt"]["executor"]["time_budget_s"]
    
    def samples(self):
        self.configuration.samples = self.config["hyperopt"]["executor"]["num_samples"]

    def configuration_to_config(self):
        self.set_features()
        self.set_missing_data()
    
    def set_features(self):
        """Set selected features into the config"""
        input_features = []
        output_features = []

        for feature_name, feature_type in self.configuration.input_features.items():
                feature = {
                    "name": feature_name,
                    "column": feature_name,
                    "type": feature_type
                }
                input_features.append(feature)

        for feature_name, feature_type in self.configuration.target.items():
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

    def set_missing_data(self):
        self.config["preprocessing"]["missing_value_strategy"] = self.configuration.missing_data
