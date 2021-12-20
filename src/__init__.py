# create the flask app
import pandas as pd
from flask import Flask

app = Flask(__name__)

app.config['UPLOAD_PATH'] = "./csvFiles"
app.config['dataset'] = pd.DataFrame()


# Déclaration des controllers
import src.Controller.uploadController
import src.Controller.nettoyageController
