from flask import Flask, render_template, Response, request
import json
import requests

import sqlite3

app = Flask(__name__)




@app.route("/")
def index():
    return "hello world"

