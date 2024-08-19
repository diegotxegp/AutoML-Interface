import tkinter as tk
from tkinter import messagebox

from ludwig.automl import auto_train, create_auto_config
from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split
from ludwig.visualize import compare_performance
from ludwig.visualize import confusion_matrix

class Ludwig:
    def __init__(self):
        self.df = None
        self.target = None
        self.config = None
        self.model = None
        self.split_df = None
        self.test_df = None
    

    def automl(df, target):
        messagebox.showinfo("Start", "AutoML-Interface starting...")

        split_df = get_repeatable_train_val_test_split(df, target, random_seed=42)

        auto_train_results = auto_train(
            dataset=split_df,
            target=target,
            time_limit_s=7200,
            tune_for_memory=False,
            user_config={'hyperopt': {'goal': 'maximize', 'metric': 'accuracy', 'output_feature': f"{target}"},
                'preprocessing': {'split': {'column': 'split', 'type': 'fixed'}}},
        )

        model = auto_train_results.best_model
        return model

    """
    Semi-AutoML
    """
    def autoconfig(self):

        self.popup("Creating a default configuration.")

        import pprint

        from ludwig.automl import create_auto_config
        from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split

        columns = self.df.columns.tolist()
        self.target = columns[-1]
        split_df = get_repeatable_train_val_test_split(self.df, self.target, random_seed=42)

        auto_config = create_auto_config(
            dataset=split_df,
            target=self.target,
            time_limit_s=7200,
            tune_for_memory=False,
            user_config={'hyperopt': {'goal': 'maximize', 'metric': 'accuracy', 'output_feature': f"{self.target}"},
                'preprocessing': {'split': {'column': 'split', 'type': 'fixed'}}},
        )

        pprint.pprint(auto_config)

        self.config = auto_config