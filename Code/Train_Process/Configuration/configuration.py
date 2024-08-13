from datetime import datetime

class Configuration:
    def __init__(self, selected_project=None, selected_dataset=None, input_features=None,
                 output_features=None, path=None, algorithm=None, filetype = None, separator=None,
                 runtime=None, maximize_minimize=None, metrics=None, timestamp=None):
        
        self.selected_project = selected_project
        self.selected_dataset = selected_dataset
        self.input_features = input_features
        self.output_features = output_features
        self.path = path
        self.algorithm = algorithm
        self.filetype = filetype
        self.separator = separator
        self.runtime = runtime
        self.maximize_minimize = maximize_minimize
        self.metrics = metrics
        self.timestamp = timestamp if timestamp else datetime.now()