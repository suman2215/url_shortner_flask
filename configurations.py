from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
import logging

# Setting Up the Logger
logging.basicConfig(filename="url-shortner.log", level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

# Setting Up the Flask App
LOGGER.debug("Creating Flask App for URL Shortner")
app = Flask(__name__)

# Setting Up the API
LOGGER.debug("Creating Flask Restful API")
api = Api(app)

# Setting Up the MongoDB
LOGGER.debug("Creating PyMongo Instance")
MONGODB_URI = "mongodb+srv://rajat:RajatGupta@sports-management.ihvhhwb.mongodb.net/url_shortner"
app.config["MONGO_URI"] = MONGODB_URI

MONGODB_DB = "url_shortner"
app.config["MONGO_DBNAME"] = MONGODB_DB

mongo = PyMongo(app)


# Setting Up the CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')
    return response
