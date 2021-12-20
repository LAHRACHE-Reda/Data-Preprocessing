from src import app
import src.Service.nettoyageService as net


@app.route('/null_values')
def null_values():
    return net.identify_null_values().to_json()


@app.route('/delete_null')
def drop_null():
    total_deleted = app.config['dataset'].isna().sum().sum()
    net.drop_null_values()
    return {"total": int(total_deleted)}   # return total deleted null rows
