from flask import Flask, render_template, Response, request
import os, sys
import json
from datetime import datetime
import statecontrol as statecontrol


app = Flask(__name__)


def get_state_file():
    f = open('./state.json')
    state_file = json.load(f)
    f.close()
    
    return state_file

@app.route("/api_get")
def get_dict():
    return statecontrol.compute_current_state(get_state_file())

@app.route("/api_post", methods = ['POST'])
def set_state():
    json_response = request.get_json()
    state_file = get_state_file()
    

    new_state = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
            "altitude": float(json_response['altitude']), 
            "azimuth": float(json_response['azimuth']),
            "door_state": float(json_response['door_state']),
            "door_open": False,
            }

    new_state_file = statecontrol.update_state(state_file, new_state)

    with open("./state.json", "w") as outfile:
        outfile.write(json.dumps(new_state_file, indent = 4))
     
    return '', 204



@app.route("/telescope_interface")
def get_interface():
    return render_template("interface.html")
