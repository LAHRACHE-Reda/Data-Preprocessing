import pandas as pd
import glob
import os
from flask import request
from src import app


# location = "../MachineLearningCSV/MachineLearningCVE/*.csv"


# concatenate all files and return dataframe
def concatenate(location):
    excel_files = glob.glob(location)
    dataset = pd.DataFrame()
    # Concatenate files
    for excel_file in excel_files:
        dataset2 = pd.read_csv(excel_file, low_memory=False)
        dataset = pd.concat([dataset, dataset2])
    return dataset


# upload file to csvFiles folder
def upload_csv():
    for f in request.files.getlist('file_name'):
        f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
