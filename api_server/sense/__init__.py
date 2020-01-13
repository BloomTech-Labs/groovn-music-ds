# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random
app = Flask(__name__)
CORS(app)
from sklearn.preprocessing import RobustScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KDTree
df = pd.read_csv('sense/similar_songs_prediction.csv')
df2 = pd.read_csv('sense/SpotifyAudioFeatures2019.csv')

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
    Baseline Prediction using NearNeighbor with shuffle and filter
    """
    song_ids = request.get_json(force=True)
    final_list = []
    for song_id in song_ids.get('request'):
        if (len(df[df.id == song_id].values.tolist()) != 0):
            final_list.extend(df[df.id == song_id].values.tolist()[0][1:])
    random.shuffle(final_list)
    data={"data":list(set(final_list))}
    return jsonify(data)

@app.route('/model2',methods=['GET', 'POST'])
def predict3():
    """
    Dynamic Prediction using NearNeighbor
    """
    song_info = request.get_json(force=True)
    final_list = []
    for song_dict in song_info.get('request'):
        # Data Wrangling
        s = pd.Series(song_dict)
        json_df = s.to_frame()
        temp = pd.concat([df2.drop(columns=['artist_name', 'track_name']),json_df.transpose()], sort=False)
        temp = temp.reset_index(drop=True)
        dynamic_df = temp.drop(columns=['track_id'])

        # Set up predictive model
        scaler = RobustScaler()
        X = scaler.fit_transform(dynamic_df)
        model = KDTree(X)
        X_Prediction = np.array([X[-1]])
        dist, ind = model.query(X_Prediction, k=6)
 
        # Generate prediction into list
        prediction_list = []
        for row in ind:
            song_id = [temp.track_id[i] for i in row]
            prediction_list.append(song_id) 
        columns = ['id', '1', '2', '3', '4', '5']
        final_prediction = pd.DataFrame(prediction_list, columns=columns)
        final_prediction = final_prediction.drop_duplicates(subset=['id'], keep='first')

        # Remove duplicate song
        temp_list = final_prediction.values.tolist()[0][1:]
        temp_list = list(filter((song_dict['track_id']).__ne__, temp_list))
        final_list.extend(temp_list)    
    data={"data":list(set(final_list))}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)