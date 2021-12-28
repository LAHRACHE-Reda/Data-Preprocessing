# Identifier les valeurs null
import sys

import numpy as np

from src import app

#------Valeurs nulles-----

def identify_null_values():
    return app.config['dataset'][app.config['dataset'].isna().any(axis=1)]


# Supprimer les valeurs null
def drop_null_values():
    app.config['dataset'].dropna(inplace=True)


<<<<<<< HEAD
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
=======
#------Valeurs doublons-----

def identify_duplicate_values():
    return app.config['dataset'].loc[app.config['dataset'].duplicated(), :]

def drop_duplicate_values():
    app.config['dataset'].drop_duplicates(inplace=True)



>>>>>>> 547f5ff8248f652b6b391f003d012f7ad2d3e26c

