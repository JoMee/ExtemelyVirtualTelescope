FROM ubuntu 
RUN apt-get update && apt-get upgrade
RUN apt-get install -y xvfb
RUN apt-get install -y blender 
RUN apt-get install -y python3-pip

RUN pip3 install opencv-python
RUN pip3 install flask
RUN pip3 install requests


COPY ./src /src/
COPY ./startup.py /

CMD python3 startup.py 
