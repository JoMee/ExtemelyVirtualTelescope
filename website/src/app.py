from flask import Flask, render_template, Response, request
import json
import requests

app = Flask(__name__)


@app.route("/")
def get_interface():
    return render_template("pages/telescope-state.html")

@app.route("/submit", methods = ['POST'])
def submit_form():
    json_response = request.get_json()

    
    url = 'http://state_api:5000/api_post'

    
    json_response['door_state'] = '0'
    json_response['door_open'] = False

    print(json_response)

    requests.post(url, data = json_response)

    return '', 204
