### 3️⃣ How to connect to the web API
1. send request to https://sensemodel.herokuapp.com/model1 with sample body that include song ids:

```
Example 1:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl"]}

Example 2:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl", "35cOyocq8Gb6UcT0NWeTwn", "4ZD1VFoJ9LyV65KhPO9TZ5", "3j8FPquKEOygdUMLLs1Pxr"]}

5 similar songs will be recommended per song_id.  Request list size is dynamic and result will be unique.
```

2. send request to https://sensemodel.herokuapp.com/model1_flexible with sample body that include song ids:
```
Example 1:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl", "wrong_id"]}

Example 2:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl", "35cOyocq8Gb6UcT0NWeTwn", "4ZD1VFoJ9LyV65KhPO9TZ5", "3j8FPquKEOygdUMLLs1Pxr", "wrong_id"]}
```
3. Send request to https://sensemodel.herokuapp.com/model2 with sample body that include spotify song audio features:
```
Example 1:
{
  "request": [
    {
      "track_id": "any_song_id",
      "acousticness": 0.00582,
      "danceability": 0.743,
      "duration_ms": 238373,
      "energy": 0.339,
      "instrumentalness": 0,
      "key": 1,
      "liveness": 0.0812,
      "loudness": -7.678,
      "mode": 1,
      "speechiness": 0.409,
      "tempo": 203.927,
      "time_signature": 4,
      "valence": 0.118,
      "popularity": 15
    },
    {
      "track_id": "any_song_id2",
      "acousticness": 0.00582,
      "danceability": 0.743,
      "duration_ms": 238373,
      "energy": 0.339,
      "instrumentalness": 1,
      "key": 1,
      "liveness": 0.0812,
      "loudness": -7.678,
      "mode": 1,
      "speechiness": 0.409,
      "tempo": 203.927,
      "time_signature": 4,
      "valence": 0.118,
      "popularity": 15
    }
  ]
}

Example 2:
{
  "request": [
    {
      "track_id": "4MUF5hjHDYbJF2YtKFp0MI",
      "acousticness": 0.00582,
      "danceability": 0.743,
      "duration_ms": 238373,
      "energy": 0.339,
      "instrumentalness": 0,
      "key": 1,
      "liveness": 0.0812,
      "loudness": -7.678,
      "mode": 1,
      "speechiness": 0.409,
      "tempo": 203.927,
      "time_signature": 4,
      "valence": 0.118,
      "popularity": 15
    },
    {
      "track_id": "6e8Voz3K2vcOsydNtxbwaQ",
      "acousticness": 0.00582,
      "danceability": 0.743,
      "duration_ms": 238373,
      "energy": 0.339,
      "instrumentalness": 1,
      "key": 1,
      "liveness": 0.0812,
      "loudness": -7.678,
      "mode": 1,
      "speechiness": 0.409,
      "tempo": 203.927,
      "time_signature": 4,
      "valence": 0.118,
      "popularity": 15
    },
    {
      "track_id": "4ZD1VFoJ9LyV65KhPO9TZ5",
      "acousticness": 0.03582,
      "danceability": 0.743,
      "duration_ms": 238373,
      "energy": 0.339,
      "instrumentalness": 1,
      "key": 1,
      "liveness": 0.3812,
      "loudness": -7.678,
      "mode": 1,
      "speechiness": 0.409,
      "tempo": 203.927,
      "time_signature": 4,
      "valence": 0.718,
      "popularity": 15
    }
  ]
}
```
Request list size is dynamic

### Test out song
1. http://open.spotify.com/track/{id}
```
Example 1:
http://open.spotify.com/track/4MUF5hjHDYbJF2YtKFp0MI
```