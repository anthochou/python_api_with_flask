##GETTING STARTED

This project implements a URL shortening service using Python and Flask. The service exposes two endpoints encode/decode to 
encode/decode URLs. Encoded URLs are case sensitive.

##PREREQUISITES

Clone the project from gitHub. The project requires to install the following libraries: 

flask, flask-restful, requests, validators, pytest

You can install them by running: 

>  pip install -r requirements.txt

##RUN THE APIs

You need first to run the Flask application by running:

> python  shortlink.py

When the application is running, the APIs can be called, leave that command window running.
Run the code below as a cell in your favorite IDE like Jupyter or Visual Code.

To encode an URL (change the port if you have a customized port):

```
  import requests, json

  BASE = "http://127.0.0.1:5000/"
  short_url_response = requests.put(BASE + "encode/longUrl", {"long_url": "https://youtube.com/skfjsldkjsd758609/"}).json()
  short_url_response = json.loads(short_url_response)
  print (short_url_response )
```

To decode a URL (replace the URL below by the encoded URL from above):

```
  import requests, json

  BASE = "http://127.0.0.1:5000/"
  response = requests.get(BASE + "decode?shorturl=http://small.url/REPLACE" ).json()
  response = json.loads(response)
  print(response)
```

##TEST

A number of unit tests are implemented: encode/decode a URL, URL format, encode/decode errors. 

You can run the tests by running:

> py.test 

It should collect and executes all the tests defined in tests/test_api.py

##IMPROVEMENTS

A number of improvements can be implemented/investigated:

- Double check if specific versions of the lib are required, or use the pip freeze feature to capture all the versions used
- Creates a virtual environment 
- Check URL format passed as parameters to APIs
- Specific error message : url format not correct, url not existing
- Usage of fixture in test to have an encoded URL
- Investigate a valid test where the same short URL would be generated multiple times randomly
