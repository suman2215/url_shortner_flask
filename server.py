from configurations import app, api, LOGGER
from apis.Shorten import Shorten
from apis.Redirect import Redirect

api.add_resource(Shorten, "/shorten")
api.add_resource(Redirect, "/<string:short_url>")

if __name__ == '__main__':
    LOGGER.debug("Starting the Flask App")
    app.run(debug=True, port=5000, host="0.0.0.0")