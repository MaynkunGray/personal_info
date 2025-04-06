from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/member')
def index():
    hl = json.load(open('templates/members.json'))
    return render_template('index.html', hl=hl)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
