# this application reads data from the api in another container and displays the meal suggestion 
# to the user
from flask import Flask, render_template
import os, json, requests
app = Flask(__name__)

@app.route('/')
def home():
    menuItems = get_menu()
    return render_template('index.html', food_name=menuItems["item"], price=menuItems["price"],image=menuItems["image"])

def get_menu():
    response=requests.get(os.environ.get("API_ENDPOINT"))
    return json.loads(response.text)


if __name__ == "__main__":
    port=int(os.environ.get("CONSUMER_PORT"))
    app.run(debug=True, host=os.environ.get("CONSUMER_HOST"), port=port)
