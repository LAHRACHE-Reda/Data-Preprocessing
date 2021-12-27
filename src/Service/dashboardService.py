from src import app


# def get_columns_details():
#     return app.config['dataset'].dtypes


# return different columns that not have a string type (can be chosen like an X)
def get_columns_name():
    columns = []
    for col in app.config['dataset'].columns:
        if app.config['dataset'].dtypes[col] != "object":  # object = String type
            columns.append(col)
    return columns


def get_classes_column():
    result = ""
    for col in app.config['dataset'].columns:
        if app.config['dataset'].dtypes[col] == "object":
            result = col
            break
    return result


# check which columns have string type and extract distinct classes (Y values)
def get_classes_name():
    result = get_classes_column()
    classes = []
    for label in app.config['dataset'][result].unique():
        classes.append(label)
    return classes


# return size of each class
def get_classes_size():
    result = get_classes_column()
    return app.config['dataset'][result].value_counts()
