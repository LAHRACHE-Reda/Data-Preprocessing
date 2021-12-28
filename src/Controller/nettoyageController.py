import sys

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

#showing infinit values
@app.route('/infinit_values')
def infinit_values():
    return net.indentify_infinit_values().to_json(orient='records')

#Deleting infinit values
@app.route('/delete_infinit', methods=['DELETE'])
def drop_infinit():
    nbrDeletedRows = net.drop_infinit_values()
    print(nbrDeletedRows, file=sys.stderr)
    return {"total": int(nbrDeletedRows)}
