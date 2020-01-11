# 1️⃣ Groovn Music - Data Science

You can find the project at [Groovn Music](https://github.com/Lambda-School-Labs/groovn-music-ds).

## 1️⃣ Contributor

|                                       [Jason Pham ](https://github.com/extrajp2014)                                        |
| :-----------------------------------------------------------------------------------------------------------: | 
|                      [<img src="https://avatars0.githubusercontent.com/u/36387815?s=460&v=4" width = "180" />](https://github.com/)|
|            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/extrajp2014)             |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Python](https://img.shields.io/badge/python-v3.7-blue)

## Project Overview

1️⃣ [Trello Board](https://trello.com/b/wRlpwQHc/groovn-music)

1️⃣ [Product Canvas](https://www.notion.so/fa46a4ff908642fa9c7011e5c1342f6f?v=4dfdf951ee6845c0be6a536d4fb124e7)

The purpose of this project to build a data science recommendation system that generate new song according to previous user's preferences.

Music Recommendation API

1. What Feature(s) is/are this API connected to?

    Music Recommendation

2. What will this API integration accomplish in the feature(s) to which it’s connected?

    The Python API web server will host a data model that can perform on-demand prediction for similar songs that user may like. The result data can retrieved through GET and POST function.

3. What alternatives did you consider?

    Pre-populate prediction for popular songs and store them within playlists inside a database

4. Why did you decide on this solution? (what are the advantages?)

    The recommendation will be on-demand and result will be dynamic. This also provides more flexibility when updating to newer predictive model.

5. What are the potential challenges can you foresee?

    The time to retrieve recommendation may take longer due to server limitation.

### Tech Stack

1. HTTP Web server and Web Applications

- Gunicorn
    - Automatic worker process management
    - Multiple worker configurations
    - Light on server resources and fairly fast
- Flask
    - Lightweight and extensible Python web framework
    - Extensions available to enhance additional features

2. Heroku Infrastructure

- Pickle for model deployment

- REST API with the Flask Framework

- Heroku Pipelines to maintain continuous workflow

### 2️⃣ Predictions

- Sklearn or XGBoost package to predict user’s music preference based on regression or neighbors-based learning methods

- Pandas, Numpy, and other Anaconda scientific packages for data analysis

### Data Sources

-   [Project Data](https://github.com/Lambda-School-Labs/groovn-music-ds/tree/master/data)
-   [Spotify API](https://developer.spotify.com/documentation/web-api/reference/)


### Python Notebooks

[Python Notebook 1](./spotify_prediction.ipynb)

### 3️⃣ How to connect to the data API Endpoints

1. send request to https://sensemodel.herokuapp.com/model1 with sample body that include song ids:
```
Example 1:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl"]}

Example 2:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl", "35cOyocq8Gb6UcT0NWeTwn", "4ZD1VFoJ9LyV65KhPO9TZ5", "3j8FPquKEOygdUMLLs1Pxr"]}
```

2. send request to https://sensemodel.herokuapp.com/model1_flexible with sample body that include song ids:
```
Example 1:
{"request":["bad_data_song_id","4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "5DjNBCWKdD2y8zyIxmKbbl"]}

Example 2:
{"request":["4MUF5hjHDYbJF2YtKFp0MI", "6e8Voz3K2vcOsydNtxbwaQ", "4ZD1VFoJ9LyV65KhPO9TZ5", "bad_data_song_id", "5DjNBCWKdD2y8zyIxmKbbl", "35cOyocq8Gb6UcT0NWeTwn", "4ZD1VFoJ9LyV65KhPO9TZ5", "3j8FPquKEOygdUMLLs1Pxr"]}
```

5 similar songs will be recommended per song_id.  Request list size is dynamic

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/groovn-music-be/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/groovn-music-fe/blob/master/README.md) for details on the front end of our project.