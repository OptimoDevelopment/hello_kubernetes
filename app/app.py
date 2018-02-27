import argparse
import datetime
import os
import socket

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    name = name or os.getenv('NAME', 'world')
    current_time = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')

    return render_template('hello.html', name=name, hostname=socket.gethostname(), current_time=current_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=80)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)
