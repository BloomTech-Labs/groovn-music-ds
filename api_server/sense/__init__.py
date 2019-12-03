# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
CORS(app)
df = pd.read_csv('sense/similar_songs_prediction.csv')

@app.route("/",methods=['GET', 'POST'])
def test():
    """
    A test function
    """
    return "Groovn Music API active!"

@app.route('/testget',methods=['GET', 'POST'])
def get():
    """
    A test function for get request
    """
    data = request.get_json(force=True)
    return data.get('body')

@app.route('/model1',methods=['GET', 'POST'])
def predict():
    """
    Baseline Prediction using NearNeighbor
    """
    song_ids = request.get_json(force=True)
    final_list = []
    for song_id in song_ids.get('request'):
        final_list.extend(df[df.id == song_id].values.tolist()[0][1:])

    data={"data":list(set(final_list))}
    return jsonify(data)

@app.route('/model1_flexible',methods=['GET', 'POST'])
def predict2():
    """
    Baseline Prediction using NearNeighbor
    """
    song_ids = request.get_json(force=True)
    final_list = []
    for song_id in song_ids.get('request'):
        if (len(df[df.id == song_id].values.tolist()) != 0):
            final_list.extend(df[df.id == song_id].values.tolist()[0][1:])

    data={"data":list(set(final_list))}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)