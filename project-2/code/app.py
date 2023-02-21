import pickle
import time

import pandas as pd
import requests
from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS

from model import trim_songs

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

model_not_loaded = True
while model_not_loaded:
    try:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), f"[API-INFO] loading model")
        app.model = pickle.load(open('data/model.pkl', 'rb'))
        model_not_loaded = False
    except:
        print(time.strftime('%Y-%m-%d %H:%M:%S'),
              '[API-INFO] error loading model')
        time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S'), f"[API-INFO] model loaded")

# ui

songs = []


@app.route('/', methods=['GET'])
def index():
    return redirect('/ui')


@app.route('/ui', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/add_song', methods=['POST'])
def add_song():
    song = request.form['song']
    songs.append(song)

    print(songs)
    return render_template('index.html', songs=songs)


@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    # Call the API to get song recommendation
    try:
        api_url = 'http://localhost:30510/api/recommend'
        payload = {
            "songs": songs
        }
        response = requests.post(api_url, json=payload)
        recommended_songs = response.json()['tracklist']
    except:
        recommended_songs = ['Error getting recommendation']

    # Clear the list of songs
    songs.clear()

    return render_template('recommendation.html', recommended_songs=recommended_songs)


# api
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'online',
        'version': app.model['version'],
        'model_date': app.model['model_date'],
        'time': time.strftime('%Y-%m-%d %H:%M:%S')
    })


@app.route('/api/recommend', methods=['POST'])
def recommend():
    songs = request.json
    mdl = app.model['model']
    version = app.model['version']
    model_date = app.model['model_date']
    # recommend songs
    df_songs = pd.DataFrame(songs)
    df_songs['track_name'] = df_songs['songs'].apply(trim_songs)
    df_songs = df_songs.drop('songs', axis=1)
    recommendation = mdl.predict(df_songs)

    if type(recommendation) != type([]):
        recommendation = []

    # pack response
    response = dict(
        version=version,
        model_date=model_date,
        tracklist=recommendation
    )

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=30510)
