from flask import Flask, jsonify
import os
from sqlalchemy import create_engine

app = Flask(__name__)


db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('PG_USER')
db_pass = os.environ.get('PG_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('PG_PORT') 

db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db = create_engine(db_string)

def get_rec_from_db():
    query = "SELECT MealName,MealPrice FROM Meals ORDER BY RANDOM() LIMIT 1;"
    rows = db.execute(query)

    row_list = []
    for row in rows:
        t = (row[0], row[1])
        row_list.append(t)

    return list(row_list)

@app.route('/')
@app.route('/recommendation/')
def index():
    return jsonify(get_rec_from_db())

app.run(host=os.environ.get('API_HOSTNAME'), port=os.environ.get('API_PORT'))