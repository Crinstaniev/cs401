from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "welcome to the recommendation system api."


@app.route('/api/recommend', methods=['POST'])
def recommend():
    return
