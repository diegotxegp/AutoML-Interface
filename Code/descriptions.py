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
project_help_description = """You need to create a project to store all the datasets, configuration files and generated models. Alternatively, choose an existing one \
with previously stored data."""

# Dataset tab
dataset_label_text = "Select a dataset"
dataset_help_description = """You need to add a new dataset to create a model. Alternatively, choose an already existing one. One copy of this dataset will be saved \
in the project directory."""

# Mode tab
mode_description = """
    * Automatic ML: A model is trained automatically from the dataset.

    * Semiautomatic ML: A configuration file is generated from the dataset and the help of the user choosing certain parameters."""

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
    Select how to treat missing data.

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
    Manipulate the features for a good training. Select what feature is input, output or null and its type.

    * Input feature types:
        - binary, number, category, bag, set, sequence, text, vector, audio, date, h3, image, timeseries
    * Output feature types.
        - binary, number, category, bag, set, sequence, text, vector

    * Descriptions:
        - binary: Used for categorical variables with two possible values (e.g., 0/1, true/false).
        - number: Represents continuous numerical values (e.g., age, income).
        - category: Used for variables with more than two categories (e.g., product type, color).
        - bag: Represents unordered collections of words (e.g., keywords in a document).
        - set: Represents unique, unordered sets of elements (e.g., user interests, tags).
        - sequence: Ordered sequences of elements where the order matters (e.g., words in a sentence).
        - text: Used for full text inputs or outputs (e.g., product descriptions).
        - vector: Numerical vectors, often preprocessed features (e.g., word embeddings).
        - audio: Audio data, processed to extract features (e.g., voice recordings).
        - date: Date and time information (e.g., transaction dates).
        - h3: Encoded geospatial coordinates using the H3 system (e.g., location data).
        - image: Image data, used as inputs or outputs (e.g., product photos).
        - timeseries: Sequential data that changes over time (e.g., stock prices).
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
    * Select the maximum runtime to search the best model for the chosen dataset.
"""

## Metric
metric_label_text = "Select a metric to evaluate the model"
metric_help_description = """
    Select a metric to search the best model for the chosen dataset according that metric.

    * accuracy: The proportion of correct predictions over the total number of predictions.
    * loss: The value that a model is optimizing, representing the error or difference between predicted and actual values.
    * precision: The proportion of true positive predictions out of all positive predictions.
    * recall: The proportion of true positive predictions out of all actual positives (also known as sensitivity).
    * roc_auc: The area under the ROC curve, measuring the model’s ability to distinguish between classes.
    * specificity: The proportion of true negative predictions out of all actual negatives.
    * mean_squared_error: The average of the squared differences between predicted and actual values.
    * mean_absolute_error: The average of the absolute differences between predicted and actual values.
    * root_mean_squared_error: The square root of the mean of squared differences between predicted and actual values.
    * root_mean_squared_percentage_error: The square root of the mean squared percentage error, measuring relative prediction error.
    * the loss: A general term for the function used to compute the error between predictions and ground truth.
    * hits_at_k: Measures how often the correct result is within the top k predicted results.
    """

## Time dependable
timedependable_label_text = "Is your dataset a time-dependable dataset?"
timedependable_help_description = """
    Select if your dataset is time-dependable or not.
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

    * Goal: The goal of the metric. (Maximize, minimize)
"""

# Train tab
train_help_description = """
    * Train: Push the button "Train" to train the model.
"""

# Evaluation tab
evaluation_help_description = """
    * Compare Performance: Show the performance of the model with a test dataset.

    * Confusion Matrix: Generates a confusion matrix to evaluate the model.
"""

interface_menu_about = """
Developed by Diego
University of Cantabria
2024"""