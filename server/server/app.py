from flask import Flask, request, Response
from requests import get
from os import environ

DEVELOPMENT = environ["FLASK_ENV"] == "development"
WEBPACK_DEV_SERVER = "http://localhost:3000/"

app = Flask(__name__, static_folder=None if DEVELOPMENT else "static")


def proxy(path):
    response = get(f"{WEBPACK_DEV_SERVER}{path}")
    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    ]
    headers = [
        (name, value)
        for (name, value) in response.raw.headers.items()
        if name.lower() not in excluded_headers
    ]
    return (response.content, response.status_code, headers)


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>", methods=["GET"])
def reactApp(path):
    if DEVELOPMENT:
        return proxy(request.path)
    return app.send_static_file(path)
