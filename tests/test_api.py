import json
import requests
import validators

#If you use a customized port for Flask server, replace 5000 by your port
BASE = "http://127.0.0.1:5000/"

def test_decoding():

    #encode long url
    short_url_response = requests.put(BASE + "encode/longUrl", {"long_url": "https://github.com/marketplace?category=api-management&query=&type=&verification="}).json()
    short_url_response = json.loads(short_url_response)
    encodedUrl = short_url_response["encodedUrl"]

    #decode the short url
    response = requests.get(BASE + "decode?shorturl=" + encodedUrl ).json()
    response = json.loads(response)
    decodedUrl = response["decodedUrl"]
    
    #test the decoded url is the original url
    assert decodedUrl == "https://github.com/marketplace?category=api-management&query=&type=&verification="


def test_encoding():

    #encode long url
    short_url_response = requests.put(BASE + "encode/longUrl", {"long_url": "https://youtube.com/skfjsldkjsd758609/"}).json()
    short_url_response = json.loads(short_url_response)
    encodedUrl = short_url_response["encodedUrl"]

    # encoded url has a valid url format + length + base url
    assert validators.url(encodedUrl)
    assert str(encodedUrl).startswith("http://small.url/")
    assert len(encodedUrl) == 23

def test_decoding_error():

    #submit a decoded url which was not encoded by the service
    response = requests.get(BASE + "decode?shorturl=http://notencodedurl.com/123456" ).json()
    response = json.loads(response)
    message = response['decodedUrl']
    
    assert message == 'decodingError'

def test_encoding_error() :

    #Encoding error, wrong parmeter name
    short_url_response = requests.put(BASE + "encode/longUrl", {"long_urlWRONG": "http://youtube.com/ejkgtjer905853"}).json()
    response = json.loads(short_url_response)
    message = response['encodedUrl']

    assert message == 'encodingError'

def test_decoding_existing_url():

    #encode long url
    short_url_response = requests.put(BASE + "encode/longUrl", {"long_url": "https://urltobeencoded.twice/dgjghfd57394"}).json()
    short_url_response = json.loads(short_url_response)
    encodedUrl1 = short_url_response["encodedUrl"]

    #Encode the same url again
    short_url_response = requests.put(BASE + "encode/longUrl", {"long_url": "https://urltobeencoded.twice/dgjghfd57394"}).json()
    short_url_response = json.loads(short_url_response)
    encodedUrl2 = short_url_response["encodedUrl"]

    #The same encoded url should be returned
    assert encodedUrl1 == encodedUrl2

