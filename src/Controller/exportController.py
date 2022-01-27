from src import app
import src.Service.exportService as exp
from flask import make_response


@app.route('/latestData')
def lateset_data():
    resp = make_response(exp.getLatestData().to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
