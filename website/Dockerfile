From alpine:3.16.2

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install requests

RUN apk add py3-flask

COPY src/ /src/

CMD cd src && flask run --host=0.0.0.0


