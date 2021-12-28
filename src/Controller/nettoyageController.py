from src import app
import src.Service.nettoyageService as net


@app.route('/null_values')
def null_values():
    return net.identify_null_values().to_json(orient='records')


@app.route('/delete_null', methods=['DELETE'])
def drop_null():
    total_deleted = app.config['dataset'].isna().sum().sum()
    net.drop_null_values()
    return {"total": int(total_deleted)}   # return total deleted null rows

#------Valeurs doublons-----
@app.route('/duplicate_values')
def duplicate_values():
    return net.identify_duplicate_values().to_json(orient='records')


@app.route('/delete_duplicate', methods=['DELETE'])
def drop_duplicate():
    totalDupl=app.config['dataset'].duplicated().sum()
    net.drop_duplicate_values()
    return {"totalDupl": int(totalDupl)}