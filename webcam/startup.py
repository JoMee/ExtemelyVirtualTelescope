import os
import subprocess
import sys

os.system("Xvfb :1 &")
os.environ['DISPLAY'] = ":1" # visible in this process + all children

os.system("cd src && flask run --host=0.0.0.0")
