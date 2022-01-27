import json
import sys

from src import app
import src.Service.dashboardService as da


# @app.route('/columns_details')
# def columns_details():
#     return da.get_columns_details().to_json()


@app.route('/columns')
def columns_name():
    print(da.get_classes_size().to_json(), file=sys.stdout)
    return json.dumps(da.get_columns_name())


@app.route('/count_class')
def classes_size():
    print(da.get_classes_size().to_json(), file=sys.stdout)
    return da.get_classes_size().to_json()
