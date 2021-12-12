# create the flask app

from flask import Flask

app = Flask(__name__)

app.config['UPLOAD_PATH'] = "./csvFiles"

import src.Controller.uploadController
