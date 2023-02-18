from flask import Flask, request, jsonify
from model import trim_songs
import pickle
import pandas as pd

app = Flask(__name__)
app.model = pickle.load(open('data/model.pkl', 'rb'))

@app.route('/api/health', methods=['GET'])
def health():
    return 'OK'

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
    app.run(debug=True)