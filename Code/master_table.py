# Master table

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