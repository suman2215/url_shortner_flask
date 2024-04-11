import http
import string
import random

from flask import make_response, request
from flask_restful import Resource
from configurations import LOGGER, mongo
from bson import json_util


class Shorten(Resource):
    def post(self):
        LOGGER.debug("Shorten API Called")
        # Case 0: If short_url already exists for the long_url
        body = request.get_json()
        data = mongo.db.urls.find_one({"long_url": body["long_url"]})
        if data is not None:
            # Return Already Existing Short URL
            return make_response(json_util.dumps({
                "Short URL": "http://0.0.0.0/"+data["short_url"]
            }), http.HTTPStatus.CREATED)
        else:
            # Case 1: long_url and alias both in request and alias is available/unavailable
            if body["alias"] != "":
                data = mongo.db.urls.find_one({"short_url": body["alias"]})
                if data is not None:
                    return make_response(json_util.dumps({
                        "Error": "Requested Alias is Not Available, Try with some different alias"
                    }), http.HTTPStatus.INTERNAL_SERVER_ERROR)
                else:
                    mongo.db.urls.insert_one({
                        "long_url": body["long_url"],
                        "short_url": body["alias"]
                    })
                    return make_response(json_util.dumps({
                        "Short URL: ": "http://0.0.0.0/"+body["alias"]
                    }), http.HTTPStatus.CREATED)

            # Case 2: long_url in request and short_url will be random
            else:
                chars = string.ascii_letters + string.digits
                # chars = "abcd....xyzABC....XYZ0123456789"
                length = 8
                short_url = ''.join(random.choice(chars) for _ in range(length))
                mongo.db.urls.insert_one({
                    "long_url": body["long_url"],
                    "short_url": short_url
                })
                return make_response(json_util.dumps({
                        "Short URL: ": "http://0.0.0.0/"+short_url
                    }), http.HTTPStatus.CREATED)
