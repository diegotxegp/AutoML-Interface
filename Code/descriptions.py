###### DESCRIPTIONS.py

# WELCOME FRAME
welcome_title = "Welcome to this AutoML interface"
welcome_text = "This tool allows you to train models and make predictions easily. ""Please select one of the options below to get started."

# INFO TAB

## Text with information about the tool
training_process_info_text = """
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
project_label_text = "Select a project"
project_help_description = "You must create a project to allocate all the models in there. Else, select one already created."

# Dataset tab
dataset_label_text = "Select a dataset"
dataset_help_description = "You must add a dataset to train. One copy of this will be saved in the project directory."

# Mode tab
mode_description = """
    * Automatic ML: Automatically trains a model.

    * Semiautomatic ML: Generates a configuration file from the dataset.
"""

# Preprocess tab.
## Separator tab.
separator_label_text = "Which separator among columns does your data use?"
## Missing data tab
missing_data_label_text = "How to treat missing data?"
## Target tab
target_label_text = "Select which is the target"
## Input feature tab
input_features_label_text = "Select which input features to train"
## Metric tab
metric_label_text = "Select a metric to evaluate the model"
## Goal tab
goal_label_text = "Select a goal to optimize the model"

## Separator
separator_help_description = """
    * comma: Comma separated columns.
    * semicolon: Semicolon separated columns.
    * backslash: Backslash separated columns.
"""

## Missing data
missing_data_help_description = """
    * fill_with_const: Replaces the missing value with a specific value specified with the fill_value parameter.

    * fill_with_mode: Replaces the missing values with the most frequent value in the column.

    * fill_with_mean: Replaces the missing values with the mean of the values in the column (number features only).

    * fill_with_false Replace the missing values with the false value in the column (binary features only).

    * bfill: Replaces the missing values with the next valid value from the subsequent rows of the input dataset.

    * ffill: Replaces the missing values with the previous valid value from the preceding rows of the input dataset.

    * drop_row: Removes the entire row from the dataset if this column is missing.
"""

## Features
features_label_text = "Modify the features to train"
features_help_description = """
    * input: Input features.
    * output: Output features.
"""

## Target
target_help_description = """
    * binary: Binary target.
    * number: Numerical target.
    * category: Categorical target.
    * bag: Bag of categorical target.
    * set: Set of categorical target.
    * sequence: Sequence of categorical target.
    * text: Text target.
    * vector: Vector target.
    * audio: Audio target.
    * date: Date target.
    * h3: H3 target.
    * image: Image target.
    * timeseries: Time series target.
"""

## Runtime
runtime_label_text = "Choose how many seconds to run the training process"
runtime_help_description = """
    * The maximum runtime of the model.
"""

## Metric
metric_label_text = "Select a metric to evaluate the model"
metric_description = """
    * accuracy: The accuracy of the model.

    * hits_at_k: The hits at k of the model.

    * loss: The loss of the model.
    """

## Time dependable
timedependable_label_text = "Is your dataset a time-dependable dataset?"
timedependable_help_description = """
    * No: This dataset does not depend on time.

    * Yes: This dataset depends on time.
"""

# Summary tab
summary_description = """
    * Project: The name of the project.

    * Dataset: The name of the dataset.

    * Samples: The number of samples in the dataset.

    * Input features: The input features of the model.

    * Target: The target feature of the model.

    * Separator: The separator used in the dataset.

    * Missing data: The missing data strategy used in the dataset.

    * Runtime: The maximum runtime of the model.

    * Metric: The metric used to evaluate the model.

    * Goal: The goal of the metric.
"""

# Train tab
train_description = """
    * Train: Trains the model.
"""

# Evaluation tab
evaluation_description = """
    * Compare Performance: Compares the performance of the model with the original dataset.

    * Confusion Matrix: Generates a confusion matrix to evaluate the model.
"""

interface_menu_about = "AutoML-Interface v2.0\nDeveloped by Diego\n(2024)"