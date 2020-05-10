from flask import Flask, request, Response
from requests import get
from os import environ

app = Flask(__name__, static_folder=None)

WEBPACK_DEV_SERVER = 'http://localhost:3000/'

def proxy(path):
    response = get(f'{WEBPACK_DEV_SERVER}{path}')
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in response.raw.headers.items() if name.lower() not in excluded_headers]
    return Response(response.content, response.status_code, headers)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def reactApp(path):
    if environ['FLASK_ENV'] == 'development':
        return proxy(request.path)
    else:
        # return static dir
        pass
