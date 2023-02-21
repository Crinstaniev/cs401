from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/recommend', methods=['POST'])
def recommend_songs():
    song_list = request.json.get('songList')
    print(song_list)
    # Your recommendation algorithm goes here
    recommended_songs = [
        {'id': 1, 'name': 'Song 1'},
        {'id': 2, 'name': 'Song 2'},
        {'id': 3, 'name': 'Song 3'}
    ]
    return jsonify(recommended_songs)

if __name__ == '__main__':
    app.run(debug=True)
