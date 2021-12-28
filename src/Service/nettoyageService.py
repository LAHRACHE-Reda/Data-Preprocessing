# Identifier les valeurs null
from src import app

#------Valeurs nulles-----

def identify_null_values():
    return app.config['dataset'][app.config['dataset'].isna().any(axis=1)]


# Supprimer les valeurs null
def drop_null_values():
    app.config['dataset'].dropna(inplace=True)


#------Valeurs doublons-----

def identify_duplicate_values():
    return app.config['dataset'].loc[app.config['dataset'].duplicated(), :]

def drop_duplicate_values():
    app.config['dataset'].drop_duplicates(inplace=True)




