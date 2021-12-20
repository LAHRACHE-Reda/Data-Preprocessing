# Identifier les valeurs null
from src import app


def identify_null_values():
    return app.config['dataset'][app.config['dataset'].isna().any(axis=1)]


# Supprimer les valeurs null
def drop_null_values():
    app.config['dataset'].dropna(inplace=True)
