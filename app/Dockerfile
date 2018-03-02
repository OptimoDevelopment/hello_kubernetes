FROM resin/raspberrypi3-alpine-python:3.6

ENV NAME 'K8S Demo'

ADD . /app

WORKDIR /app

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python", "app.py"]
