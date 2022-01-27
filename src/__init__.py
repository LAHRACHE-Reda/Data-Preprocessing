# create the flask app
import pandas as pd
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['UPLOAD_PATH'] = "./csvFiles"
app.config['dataset'] = pd.DataFrame()

# Déclaration des controllers
import src.Controller.uploadController
import src.Controller.nettoyageController
import src.Controller.dashboardController
import src.Controller.exportController
