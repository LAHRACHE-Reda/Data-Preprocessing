import os

from flask import request
from werkzeug.utils import redirect

from src import app
import src.Service.uploadService as up


location = app.config['UPLOAD_PATH']+"/*.csv"


@app.route('/')
def concatfiles():
    return up.concatenate(location).head().to_json(orient="split")


@app.route("/upload", methods=["POST"])
def uploadfiles():
    # file_name : the name of input in front end (upload)
    for f in request.files.getlist('file_name'):
        f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
    return redirect('/')
