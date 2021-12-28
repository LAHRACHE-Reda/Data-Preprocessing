import glob
import os
import pandas as pd
from flask import request
from src import app
#from src.dbConnection import db_connection


# location = "../MachineLearningCSV/MachineLearningCVE/*.csv"


# concatenate all files and return dataframe
def concatenate(location):
    excel_files = glob.glob(location)
    app.config['dataset'] = pd.DataFrame()
    # Concatenate files
    for excel_file in excel_files:
        dataset2 = pd.read_csv(excel_file, low_memory=False)
        app.config['dataset'] = pd.concat([app.config['dataset'], dataset2])
    return app.config['dataset']


# upload file to csvFiles folder
def upload_csv():
    for f in request.files.getlist('fileName'):
        f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))


# create table from dataframe
# def createtable(df):
#     conn = db_connection()
#     df.to_sql("datasetTable", conn, if_exists="replace")
#     conn.commit()
#     conn.close()
