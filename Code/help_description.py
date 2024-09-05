# HELP DESCRIPTION

# Separator

# Missing data
missing_data_help_description = """
    fill_with_const: Replaces the missing value with a specific value specified with the fill_value parameter.
    fill_with_mode: Replaces the missing values with the most frequent value in the column.
    fill_with_mean: Replaces the missing values with the mean of the values in the column (number features only).
    fill_with_false Replace the missing values with the false value in the column (binary features only).
    bfill: Replaces the missing values with the next valid value from the subsequent rows of the input dataset.
    ffill: Replaces the missing values with the previous valid value from the preceding rows of the input dataset.
    drop_row: Removes the entire row from the dataset if this column is missing.
"""