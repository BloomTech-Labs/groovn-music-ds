import requests

def test_endpoints():
    URL = 'https://sensemodel.herokuapp.com/'
    PARAMS = {""}
    r = requests.get(URL)
    print(r.text)
    assert r.text == "Groovn Music API active!"

    URL = 'https://sensemodel.herokuapp.com/model1'
    PARAMS = {"request":["4MUF5hjHDYbJF2YtKFp0MI"]}
    r = requests.get(URL, json=PARAMS)
    expected_result={
        "data": [
            "6e8Voz3K2vcOsydNtxbwaQ",
            "4ZD1VFoJ9LyV65KhPO9TZ5",
            "5DjNBCWKdD2y8zyIxmKbbl",
            "6ghs7wcpS23FOsDpR8D2MW",
            "35cOyocq8Gb6UcT0NWeTwn"
        ]
    }
    print(r.json())
    assert r.json() == expected_result

    
    URL = 'https://sensemodel.herokuapp.com/model1_flexible'
    PARAMS = {"request":["bad_data","5DjNBCWKdD2y8zyIxmKbbl"]}
    r = requests.get(URL, json=PARAMS)
    expected_result={
        "data": [
            "4ZD1VFoJ9LyV65KhPO9TZ5",
            "5NhqdHEGfM78WWnJARI0iM",
            "3CZmkivge9jnZzWxjm757B",
            "35cOyocq8Gb6UcT0NWeTwn",
            "4MUF5hjHDYbJF2YtKFp0MI"
        ]
    }
    print(r.json())
    assert r.json() == expected_result
    return 0

if (test_endpoints() == 0):
    print("all tests PASSED!")