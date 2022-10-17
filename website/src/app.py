from flask import Flask, render_template, Response, request

app = Flask(__name__)


@app.route("/")
def get_interface():
    return render_template("index.html")

