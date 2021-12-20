from src import app
import src.Service.uploadService as up

location = app.config['UPLOAD_PATH']+"/*.csv"


# @app.route('/')
# def concatfiles():
#     # up.concatenate(location)
#     # up.createTable(df)  # Create table from csv files
#     #
#     # conn = dbconn.db_connection()
#     # cur = conn.cursor()
#     # cur.execute("""SELECT * FROM datasetTable LIMIT 5""")
#     # data = []
#     # for row in cur.fetchall():
#     #     data.append(dict(row))
#     #
#     print(dataset.head(), file=sys.stdout)
#     return dataset.to_json()   # retourn first 10 rows


@app.route("/upload", methods=["POST"])
def uploadfiles():
    # file_name : the name of input in front end (upload)
    # for f in request.files.getlist('file_name'):
    #     f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
    up.upload_csv()
    app.config['dataset'] = up.concatenate(location)
    # up.createTable(dataset)  # Create table from csv files
    return app.config['dataset'].head(10).to_json()    # return 5 row
