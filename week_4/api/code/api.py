# This application returns a randomly selected food item in JSON format
from flask import Flask, jsonify
import os
import json
from random import randint

app = Flask(__name__)

@app.route('/')
def random_food():
    with open('/app/foodlist.json') as fp:
        data = json.load(fp)
        random_index = randint(0, len(data["menu"])-1)
        return json.dumps(data["menu"][random_index])

if __name__ == "__main__":
    port=int(os.environ.get("API_PORT"))
    app.run(debug=True, host=os.environ.get("API_HOST"), port=port)




