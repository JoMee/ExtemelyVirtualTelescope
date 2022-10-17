from flask import Flask, render_template, Response, request
import cv2
import os
import json

app = Flask(__name__)

def gen_video():
    while True:

        os.system("xvfb-run -a blender --background imagegen.blend --python ./imagegen.py -- ./")
        frame = cv2.imread('./images/output.jpg', 0)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route("/video_feed")
def video_feed_server():
    return Response(gen_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame') 

