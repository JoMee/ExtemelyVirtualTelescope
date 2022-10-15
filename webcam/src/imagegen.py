import bpy, sys, os
import math
import time
import json
import requests

# Assume the last argument is image path
imagePath = sys.argv[-1]

if os.path.exists(imagePath):

    obj = bpy.context.scene.objects.get('telescope')

    f = requests.get('http://state_api:5000/api_get')
    
    current_state = json.loads(f.text)


    altitude = current_state['altitude']

    obj.rotation_euler[0] = math.radians(altitude - 90)

    obj2 = bpy.context.scene.objects.get('housing')
    obj2.rotation_euler[2] = math.radians(current_state['azimuth'])

    imageBaseName = bpy.path.basename(imagePath)
    bpy.context.scene.render.filepath += 'output' + imageBaseName

    bpy.ops.render.render(write_still=True)
