import random
import string
import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# 2 dictinnaries: one with long urls as key, the other one with sort urls as key to decode a url
encodeDic = {}
decodeDic = {}
shortlinkBase = 'http://short.est/'

def encode(longUrl):
    ''' Encodes a long URL'''

    lettersDigits = string.ascii_lowercase + string.ascii_uppercase + '0123456789'

    #Check the long URL does not already exist
    if longUrl not in encodeDic:

        #We might generate a random code that is already assigned to a long URL. We loop until we generate a new code not existing
        while longUrl not in encodeDic:
            
            # 6 random caracters
            newCode = random.choices (lettersDigits, k=6)
            encodedUrl = shortlinkBase + "".join(newCode)

            # If the shortened URL is not already used       
            if encodedUrl not in decodeDic:

                #Populate both dictionaries to be able to decode too
                encodeDic[longUrl] = encodedUrl
                decodeDic[encodedUrl] = longUrl
    
    return encodeDic[longUrl]

def decode (shortUrl):
    ''' Returns the original URL from an encoded URL '''

    return decodeDic[shortUrl]

class DecodeUrlAPI(Resource):
    ''' API decoding a URL received as url parameter in GET request  '''
    
    #Used to decode url
    def get(self):

        data = {}
        
        try:
            shorturl = request.args.get('shorturl')
            data['decodedUrl'] = decode(shorturl)
            return (json.dumps(data))

        except:
            data['decodedUrl'] = 'decodingError' # Might be an URL not existing
            return (json.dumps(data))
        
class EncodeUrlAPI(Resource):
    ''' API encocoding a long URL received as parameter in PUT request  '''

    #Encode long url
    def put(self, long_url):

        data = {}

        try:
            long_url = str(request.form['long_url']).lower()
            data['encodedUrl'] = encode(long_url)
            return (json.dumps(data))
        
        except:
            data['encodedUrl'] = 'encodingError'
            return (json.dumps(data))

#Resources
api.add_resource(DecodeUrlAPI, "/decode")
api.add_resource(EncodeUrlAPI, "/encode/<string:long_url>")

if __name__ == '__main__':
    
    app.run(debug=False)
    