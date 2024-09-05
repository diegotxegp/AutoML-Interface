import tkinter as tk
from tkinter import PanedWindow

# Master table

welcome_title = "Welcome to this AutoML interface"
welcome_text = "This tool allows you to train models and make predictions easily. ""Please select one of the options below to get started."

# Info tab. Text with information about the tool
info_text = """
You have just chosen to train a model. Follow the next tabs to continue with the process of training.

1- Create a new project to allocate all the models in there. Else, select one already created.
2- Add a dataset to train. One copy of this will be saved in the project directory.
3- A series of questions will be asked to understand what you want to do.
4- Train. Brush up the summary of the previous data and push "Train".
5- After training, some graphics will be showed to check its performance.

Along this process, you can always check this information to make sure your steps.

AFTER READING THIS, PRESS "OK" TO CONTINUE
"""

# Project tab

# Dataset tab

# Preprocess tab.

## Separator tab.
separator_label_text = "Which separator among columns does your data use?"
## Missing data tab
missing_data_label_text = "How to treat missing data?"
## Target tab
target_label_text = "Select which is the target"
## Input feature tab
input_features_label_text = "Select which input features to train"

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
            ]
feature_classes = ["input", "output", ""]
input_feature_types = ["binary", "number", "category", "bag", "set", "sequence", "text", "vector", "audio", "date", "h3", "image", "timeseries"]
output_feature_types = ["binary", "number", "category", "bag", "set", "sequence", "text", "vector"]
separators = [",", ";", "\\"]
missing_data_options = ["fill_with_const", "fill_with_mode", "fill_with_mean", "fill_with_false", "bfill", "ffill", "drop_row"]

# Enables the next shadowed tab
def enable_next_tab(notebook) -> bool:
    current_tab = notebook.index('current')
    total_tabs = len(notebook.tabs())
    
    # There is more tabs: True
    if current_tab < total_tabs - 1:
        next_tab = current_tab + 1
        notebook.tab(next_tab, state="normal")
        notebook.select(next_tab)

    # There is not more tabs: False
    else:
        return False

# Creates a two-side window
def paned_window(frame):
        paned_window = PanedWindow(frame, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=5)
        paned_window.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(paned_window)
        right_frame = tk.Frame(paned_window)

        paned_window.add(left_frame)
        paned_window.add(right_frame)

        return left_frame, right_frame