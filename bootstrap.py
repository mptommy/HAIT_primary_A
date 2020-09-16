# coding: utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/boot')
def index():
    return render_template('bootstrap.html')


if __name__ == '__main__':
    app.run()
