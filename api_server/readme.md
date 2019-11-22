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

Request list size is dynamic
```