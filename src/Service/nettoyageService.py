# Identifier les valeurs null
import sys

import numpy as np

from src import app


def identify_null_values():
    return app.config['dataset'][app.config['dataset'].isna().any(axis=1)]


# Supprimer les valeurs null
def drop_null_values():
    app.config['dataset'].dropna(inplace=True)


#Identify the infinit values
def indentify_infinit_values():
    return app.config['dataset'][app.config['dataset'].isin([np.inf, -np.inf]).any(axis=1)]

#Delete infinit values
def drop_infinit_values():
    index = app.config['dataset'].index
    condition = app.config['dataset'].isin([np.inf, -np.inf]).any(axis=1)
    indices = index[condition]
    indices_list = indices.tolist()
    for i in indices_list:
        app.config['dataset'].drop(index=i, inplace=True)
    return len(indices_list)

