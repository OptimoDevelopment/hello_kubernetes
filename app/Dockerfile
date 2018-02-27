FROM resin/raspberrypi3-alpine-python:3.6

ARG APP_PORT=8077

ENV APP_PORT $APP_PORT
ENV NAME 'K8S Demo'

ADD . /app

WORKDIR /app

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE $APP_PORT

CMD "python" "app.py" "-p" $APP_PORT
