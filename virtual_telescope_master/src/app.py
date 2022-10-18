from flask import Flask, render_template, Response, request
import json
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"

@app.route("/api_state_post", methods = ['POST'])
def api_state_get():
    json_response = request.get_json()
    url = 'http://state_api:5000/api_post'
    print(json_response, flush=True)
    requests.post(url, json = json_response)
    return '', 204
