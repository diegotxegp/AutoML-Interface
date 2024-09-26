##### MASTER_TABLE.py

from Ludwig.ludwig_master_table import file_formats, input_feature_types, output_feature_types, separators, missing_data_options, metrics

automl_framework = "Ludwig" # Framework to use

training_tab_names = ["Info", "ProjectManager", "DatasetManager", "Mode", "Preprocess", "Summary", "Train", "Evaluation"]
preprocess_tab_names = ["Separator", "MissingData", "Features", "Runtime", "Metric", "TimeDependable"]
evaluation_tab_names = ["ComparePerformance", "ConfusionMatrix"]

# File formats
file_formats=file_formats

# Feature classes
features_io = ["input", "output", ""]

# Types available for input features
input_feature_types = input_feature_types

# Types available for output features
output_feature_types = output_feature_types

# Punctuation marks to separate columns in datasets
separators = separators

# Options to treat missing data
missing_data_options = missing_data_options

# Options to select a metric
metrics = metrics

goals = ["maximize", "minimize"]

# Timedependable
time_dependable_options = ["No", "Yes"]