from flask_restful import Resource
from flask import redirect, make_response
import http
from configurations import LOGGER, mongo
from bson import json_util


class Redirect(Resource):
    def get(self, short_url):
        LOGGER.debug("Redirect API Called")
        data = mongo.db.urls.find_one({"short_url": short_url})
        if data is not None:
            return redirect(data["long_url"], code=http.HTTPStatus.FOUND)
        else:
            return make_response(json_util.dumps({
                "Error": "Short URL not found"
            }), http.HTTPStatus.NOT_FOUND)
