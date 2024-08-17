# Master table

welcome_title = "Welcome to this AutoML interface"
welcome_text = "This tool allows you to train models and make predictions easily. ""Please select one of the options below to get started."

# Text with information about the tool
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