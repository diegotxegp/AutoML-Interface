from datetime import datetime

class Configuration:
    def __init__(self):        
        self.project = None
        self.dataset = None
        self.input_features = None
        self.target = None
        self.path = None
        self.algorithm = None
        self.filetype = None
        self.separator = None
        self.missing_data = None
        self.runtime = None
        self.maximize_minimize = None
        self.metrics = None
        self.timestamp = datetime.now()

    def get_project(self):
        return self.project
    
    def set_project(self, project):
        self.project = project

    def get_dataset(self):
        return self.dataset
    
    def set_dataset(self, dataset):
        self.dataset = dataset

    def get_input_features(self):
        return self.input_features
    
    def set_input_features(self, input_features):
        self.input_features = input_features

    def get_target(self):
        return self.target
    
    def set_target(self, target):
        self.target = target

    def get_path(self):
        return self.path
    
    def set_path(self, path):
        self.path = path

    def get_algorithm(self):
        return self.algorithm
    
    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def get_filetype(self):
        return self.filetype
    
    def set_filetype(self, filetype):
        self.filetype = filetype

    def get_separator(self):
        return self.separator
    
    def set_separator(self, separator):
        self.separator = separator

    def get_missing_data(self):
        return self.missing_data

    def set_missing_data(self, missing_data):
        self.missing_data = missing_data

    def get_runtime(self):
        return self.runtime
    
    def set_runtime(self, runtime):
        self.runtime = runtime

    def get_maximize_minimize(self):
        return self.maximize_minimize
    
    def set_maximize_minimize(self, maximize_minimize):
        self.maximize_minimize = maximize_minimize

    def get_metrics(self):
        return self.metrics
    
    def set_metrics(self, metrics):
        self.metrics = metrics

    def get_timestamp(self):
        return self.timestamp
    
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp