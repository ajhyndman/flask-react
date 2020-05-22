from flask import Flask

app = Flask(__name__)


@app.route("/")
def getRoot():
    return "Welcome!"


@app.route("/app/", defaults={"path": "index.html"})
@app.route("/app/<path:path>")
def getApp(path):
    return app.send_static_file(path)
