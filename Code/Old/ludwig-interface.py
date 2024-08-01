import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
import pprint
import yaml
import json
import os

feature_classes = ["input", "output", ""]
input_feature_types = ["binary", "number", "category", "bag", "set", "sequence", "text", "vector", "audio", "date", "h3", "image", "timeseries"]
output_feature_types = ["binary", "number", "category", "bag", "set", "sequence", "text", "vector"]

separators = [",", ";", "\\"]


class AutoLudwig:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose a dataset")
        self.root.geometry("+100+100")
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=50, pady=50, fill=tk.BOTH, expand=False)
        self.df = None
        self.target = None
        self.path = None
        self.root.after(100, self.menu_window)

        self.config = {}
        self.model = None
        self.split_df = None
        self.test_df = None


    """
    AutoML
    """
    def automl(self):
        from ludwig.automl import auto_train
        from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split

        split_df = get_repeatable_train_val_test_split(self.df, self.target, random_seed=42)

        auto_train_results = auto_train(
            dataset=split_df,
            target=self.target,
            time_limit_s=7200,
            tune_for_memory=False,
            user_config={'hyperopt': {'goal': 'maximize', 'metric': 'accuracy', 'output_feature': f"{self.target}"},
                'preprocessing': {'split': {'column': 'split', 'type': 'fixed'}}},
        )

        pprint.pprint(auto_train_results)

        self.model = auto_train_results.best_model

        results_dir = os.path.join(os.path.split(self.path)[0],"ModelandConfig")
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        self.model.save(results_dir)
        self.model.save_config(results_dir)

        test_df=split_df[split_df["split"]==2]

        eval_stats, predictions, output_directory = self.model.evaluate(
            test_df,
            collect_predictions=True,
            collect_overall_stats=True,
            skip_save_eval_stats=False,
            skip_save_predictions=False,
            output_directory="test_results",
            return_type="dict"
        )

        self.close_popup()

        from ludwig.visualize import compare_performance
        compare_performance(
            eval_stats,
            output_feature_name=self.target,
            model_names=None,
            output_directory=None,
            file_format='pdf'
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


        """
        #eval_stats, predictions, output_directory = self.evaluate()

        self.close_popup()

        self.evaluate_window()
        
        #self.compare_performance(eval_stats)
        #self.confusion_matrix(eval_stats)
        """


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

        self.close_popup()

        self.io_features_window()


    """
    Train
    """
    def train(self):
        from ludwig.api import LudwigModel
        from ludwig.utils.dataset_utils import get_repeatable_train_val_test_split

        self.split_df = get_repeatable_train_val_test_split(self.df, self.target, random_seed=42)

        self.model = LudwigModel(self.config)

        self.model.train(dataset=self.split_df)

        results_dir = os.path.join(os.path.split(self.path)[0],"ModelandConfig")

        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        self.model.save(results_dir)
        self.model.save_config(results_dir)
        
        self.test_df=self.split_df[self.split_df["split"]==2]

    """
    Evaluate
    """
    def evaluate(self):
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

        return eval_stats, predictions, output_directory

    """
    Compare performance
    """
    def compare_performance(self, eval_stats):        
        from ludwig.visualize import compare_performance
        compare_performance(
            eval_stats,
            output_feature_name=self.target,
            model_names=None,
            output_directory=None,
            file_format='pdf'
        )

    """
    Confusion matrix
    """
    def confusion_matrix(self, eval_stats):
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

    def predict(self):
        self.model.predict(
            dataset=None,
            data_format=None,
            split='full',
            batch_size=128,
            generation_config=None,
            skip_save_unprocessed_output=True,
            skip_save_predictions=True,
            output_directory='results',
            return_type="dict",
            callbacks=None
            )






######################################## GUI ################################################################

    """
    Main menu. Options: 1) AutoML, 2) Load Config and 3) Load Model
    """
    def menu_window(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.root.title("Menu")

        automl_button = tk.Button(self.frame, text="AutoML", command=self.load_dataset)
        automl_button.pack(padx=10, pady=5)

        loadconfig_button = tk.Button(self.frame, text="Load Config", command=self.load_config)
        loadconfig_button.pack(padx=10, pady=5)

        loadmodel_button = tk.Button(self.frame, text="Load Model", command=self.load_model)
        loadmodel_button.pack(padx=10, pady=5)

    """
    Dataset asked.
    """
    def load_dataset(self):
        self.root.withdraw()

        self.path = filedialog.askopenfilename(
            filetypes=[
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx;*.xls"),
                ("Feather files", "*.feather"),
                ("FWF files", "*.fwf"),
                ("HDF5 files", "*.h5;*.hdf5"),
                ("HTML files", "*.html;*.htm"),
                ("JSON files", "*.json;*.jsonl"),
                ("Parquet files", "*.parquet"),
                ("Pickle files", "*.pkl;*.pickle"),
                ("SAS files", "*.sas7bdat;*.xpt"),
                ("SPSS files", "*.sav"),
                ("Stata files", "*.dta"),
                ("TSV files", "*.tsv"),
                ("All files", "*.*")
            ],
            title="Select a Dataset File"
        )

        if self.path:
            try:
                if self.path.endswith((".csv", ".fwf", ".tsv")):
                    self.df = pd.read_csv(self.path)
                elif self.path.endswith((".xlsx", ".xls")):
                    self.df = pd.read_excel(self.path)
                elif self.path.endswith(".feather"):
                    self.df = pd.read_feather(self.path)
                elif self.path.endswith((".h5", ".hdf5")):
                    self.df = pd.read_hdf(self.path)
                elif self.path.endswith((".html", ".htm")):
                    self.df = pd.read_html(self.path)[0]
                elif self.path.endswith((".json", ".jsonl")):
                    self.df = pd.read_json(self.path)
                elif self.path.endswith(".parquet"):
                    self.df = pd.read_parquet(self.path)
                elif self.path.endswith((".pkl", ".pickle")):
                    self.df = pd.read_pickle(self.path)
                elif self.path.endswith((".sas7bdat", ".xpt")):
                    self.df = pd.read_sas(self.path)
                elif self.path.endswith(".sav"):
                    self.df = pd.read_spss(self.path)
                elif self.path.endswith(".dta"):
                    self.df = pd.read_stata(self.path)
                else:
                    messagebox.showwarning("Warning", "File format not compatible.")
                    return

            except Exception as e:
                messagebox.showerror("Error", f"File cannot be loaded: {e}")

        print("Dataset loaded successfully")
        self.ml_window()


    """
    Config file asked.  #####################
    """
    def load_config(self):
        self.root.withdraw()

        self.path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Select a JSON Configuration File"
        )

        if self.path:
            try:
                if self.path.endswith(".json"):
                    with open(self.path, 'r') as file:
                        self.config = json.load(file)
                        print("Configuration loaded successfully")
                else:
                    messagebox.showwarning("Warning", "Selected file is not a JSON file.")
            except Exception as e:
                messagebox.showerror("Error", f"File cannot be loaded: {e}")

        self.load_dataset()

    """
    Model file asked. ###################
    """
    def load_model(self):
        self.path = filedialog.askopenfilename(
            filetypes=[
                ("All files", "*.*")
            ]
        )
        if self.path:
            try:
                if self.path.endswith((".*.yaml", "*.yml")):
                    with open(self.path, 'r') as file:
                        self.config = yaml.safe_load(file)
                else:
                    messagebox.showwarning("Warning", "File format not compatible.")
                    return

                self.menu_window()

            except Exception as e:
                messagebox.showerror("Error", f"File cannot be loaded: {e}")


    """
    ML menu. Options: 1) AutoML, 2) Semi-AutoML
    """
    def ml_window(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.root.deiconify()

        automl_button = tk.Button(self.frame, text="AutoML", command=self.target_window)
        automl_button.pack(padx=10, pady=5)

        autoconfig_button = tk.Button(self.frame, text="Semi-AutoML", command=self.io_features_window)
        autoconfig_button.pack(padx=10, pady=5)

        menu_button = tk.Button(self.frame, text="Menu", command=self.menu_window)
        menu_button.pack(padx=10, pady=5)

    """
    Select a target (output feature)
    """
    def target_window(self):
        self.root.title("Select target")

        for widget in self.frame.winfo_children():
            widget.destroy()

        param_label = tk.Label(self.frame, text="Feature", font=("Arial", 10, "bold"))
        param_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        target_label = tk.Label(self.frame, text="Target?", font=("Arial", 10, "bold"))
        target_label.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        columns = self.df.columns.tolist()

        selected_target = tk.StringVar()
        selected_target.set(columns[-1])

        for i, column in enumerate(columns):
            label = tk.Label(self.frame, text=column)
            label.grid(row=i+1, column=0, padx=5, pady=5, sticky="ew")

            checkbox = tk.Radiobutton(self.frame, text="", variable=selected_target, value=column)
            checkbox.grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")

        for i in range(2):
            self.frame.grid_columnconfigure(i, weight=1)

        back_button = tk.Button(self.frame, text="Back", command=self.menu_window)
        back_button.grid(row=len(columns)+1, column=0, pady=10, sticky="ew")

        close_button = tk.Button(self.frame, text="Close", command=self.root.quit)
        close_button.grid(row=len(columns)+1, column=1, pady=10, sticky="ew")

        execute_button = tk.Button(self.frame, text="Execute", command=lambda:self.automl_window(selected_target.get()))
        execute_button.grid(row=len(columns)+1, column=2, pady=10, sticky="ew")

    """
    AutoML window
    """
    def automl_window(self, target):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.root.title("AutoML")

        self.target = target

        self.root.withdraw()

        self.popup("AutoML running...")
        self.automl()
        self.close_popup()

    """
    Evaluate window
    """
    def evaluate_window(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.root.deiconify()
        self.root.title("Evaluation")

        eval_stats, predictions, output_directory = self.evaluate()

        compare_performance_button = tk.Button(self.frame, text="Compare performance", command=lambda:self.compare_performance(eval_stats))
        compare_performance_button.pack(padx=10, pady=5)

        confusion_matrix_button = tk.Button(self.frame, text="Confusion matrix", command=lambda:self.confusion_matrix(eval_stats))
        confusion_matrix_button.pack(padx=10, pady=5)

        menu_button = tk.Button(self.frame, text="Menu", command=self.menu_window)
        menu_button.pack(padx=10, pady=5)


    """
    Window of input and output features
    """
    def io_features_window(self):
        self.root.title("Input / Output")

        for widget in self.frame.winfo_children():
            widget.destroy()

        label_name = tk.Label(self.frame, text="Name", font=("Arial", 10, "bold"))
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        label_io = tk.Label(self.frame, text="Input/Output", font=("Arial", 10, "bold"))
        label_io.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        label_type = tk.Label(self.frame, text="Type", font=("Arial", 10, "bold"))
        label_type.grid(row=0, column=2, padx=5, pady=5, sticky="ew")


        features = []

        row_counter = 1

        if self.config == {}:
            label = tk.Label(self.frame, text="Config doesn't exist!")
            label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew", columnspan=3)
            row_counter += 1

        else:
            for i, feature in enumerate(self.config["input_features"]):
                label = tk.Label(self.frame, text=feature["column"])
                label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")
                
                feature_class = ttk.Combobox(self.frame, values=feature_classes)
                feature_class.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
                feature_class.set("input")

                feature_type = ttk.Combobox(self.frame, values=input_feature_types)
                feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
                feature_type.set(feature["type"])

                features.append((feature["column"], feature_class, feature_type))
                
                row_counter += 1

            for i, feature in enumerate(self.config["output_features"]):
                label = tk.Label(self.frame, text=feature["column"])
                label.grid(row=row_counter, column=0, padx=5, pady=5, sticky="ew")
                
                feature_class = ttk.Combobox(self.frame, values=feature_classes)
                feature_class.grid(row=row_counter, column=1, padx=5, pady=5, sticky="ew")
                feature_class.set("output")

                feature_type = ttk.Combobox(self.frame, values=input_feature_types)
                feature_type.grid(row=row_counter, column=2, padx=5, pady=5, sticky="ew")
                feature_type.set(feature["type"])

                features.append((feature["column"], feature_class, feature_type))
                
                row_counter += 1

        # Botones
        back_button = tk.Button(self.frame, text="Back", command=self.ml_window)
        back_button.grid(row=row_counter, column=0, pady=10, sticky="ew")

        close_button = tk.Button(self.frame, text="Close", command=self.root.quit)
        close_button.grid(row=row_counter, column=1, pady=10, sticky="ew")

        new_config_button = tk.Button(self.frame, text="New config", command=self.autoconfig)
        new_config_button.grid(row=row_counter, column=2, pady=10, sticky="ew")

        next_button = tk.Button(self.frame, text="Next", command=lambda:self.io_feature_window_aux(features))
        next_button.grid(row=row_counter, column=3, pady=10, sticky="ew")

        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)


    """
    Aux I/O feature window
    """
    def io_feature_window_aux(self, features):

        input_features = []
        output_features = []

        for feature_name, feature_class, feature_type in features:
            if feature_class.get() == "input":
                feature = {
                    "name": feature_name,
                    "column": feature_name,
                    "type": feature_type.get()
                }
                input_features.append(feature)

            if feature_class.get() == "output":
                feature = {
                    "name": feature_name,
                    "column": feature_name,
                    "type": feature_type.get()
                }
                output_features.append(feature)

            if feature_class == "":
                None

        self.config["input_features"] = input_features
        self.config["output_features"] = output_features

        self.config["trainer"]["validation_field"] = output_features[0]["name"]
        self.config["hyperopt"]["output_feature"] = output_features[0]["name"]

        self.target = self.config["output_features"][0]["name"]

        self.parameters_window()


    """
    Additional parameters
    """
    def parameters_window(self):
        self.root.title("Additional parameters")

        for widget in self.frame.winfo_children():
            widget.destroy()

        label_param = tk.Label(self.frame, text="Parameter", font=("Arial", 10, "bold"))
        label_param.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        label_value = tk.Label(self.frame, text="Value", font=("Arial", 10, "bold"))
        label_value.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        label_separator = tk.Label(self.frame, text="Separator")
        label_separator.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        value_separator = ttk.Combobox(self.frame, values=separators)
        value_separator.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        value_separator.set(",")

        label_time = tk.Label(self.frame, text="Time limit")
        label_time.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        value_time = tk.Entry(self.frame)
        value_time.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        value_time.insert(0, self.config["hyperopt"]["executor"]["time_budget_s"])

        label_metric = tk.Label(self.frame, text="Metric")
        label_metric.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        value_metric = ttk.Combobox(self.frame, values=["accuracy", "roc_auc", "loss"])
        value_metric.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        value_metric.set(self.config["hyperopt"]["metric"])

        label_goal = tk.Label(self.frame, text="Maximize / Minimize")
        label_goal.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        value_goal = ttk.Combobox(self.frame, values=["maximize", "minimize"])
        value_goal.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        value_goal.set(self.config["hyperopt"]["goal"])

        # Botones
        back_button = tk.Button(self.frame, text="Back", command=self.io_features_window)
        back_button.grid(row=5, column=0, pady=10, sticky="ew")

        close_button = tk.Button(self.frame, text="Close", command=self.root.quit)
        close_button.grid(row=5, column=1, pady=10, sticky="ew")

        execute_button = tk.Button(self.frame, text="Execute", command=lambda:self.parameters_window_aux(value_separator.get(), int(value_time.get()), value_goal.get(), value_metric.get()))
        execute_button.grid(row=5, column=2, pady=10, sticky="ew")

        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)


    def parameters_window_aux(self, delimiter, time, goal, metric):
        extension = os.path.splitext(os.path.basename(self.path))[1].lstrip('.')
        dat = {"dataset": {"format": extension, "delimiter": delimiter}}
        self.config["preprocessing"].update(dat)
        self.config["hyperopt"]["executor"]["time_budget_s"] = time
        self.config["hyperopt"]["metric"] = metric
        self.config["hyperopt"]["goal"] = goal

        self.root.withdraw()

        self.train()

        self.evaluate_window()



######################### POP_UP #############################
    """
    Pop-up
    """
    def popup(self, message):
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Running...")
        self.popup.resizable(False, False)
        
        label = tk.Label(self.popup, text=message)
        label.pack(padx=20, pady=20)

        self.popup.geometry("+100+100")

        # Hacer que la ventana emergente permanezca visible
        self.popup.update_idletasks()
        
        # Permitir que otras operaciones se ejecuten
        #self.root.update_idletasks()

    """
    Close pop-up
    """
    def close_popup(self):
        # Destruir la ventana emergente
        if self.popup:
            self.popup.destroy()




########################## MAIN #################################
def main():
    root = tk.Tk()
    root.resizable(False,False)
    app = AutoLudwig(root)
    root.mainloop()

if __name__ == "__main__":
    main()
