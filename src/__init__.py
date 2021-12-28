# create the flask app
import pandas as pd
from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD

=======
>>>>>>> 547f5ff8248f652b6b391f003d012f7ad2d3e26c

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_PATH'] = "./csvFiles"
app.config['dataset'] = pd.DataFrame()

# Déclaration des controllers
import src.Controller.uploadController
import src.Controller.nettoyageController
