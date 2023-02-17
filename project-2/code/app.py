from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def hello():
    return jsonify(dict(
        a='abababa',
        b='dfdfdfdf'
    ))
