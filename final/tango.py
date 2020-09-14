from flask import flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('result.html')

app.run(port=8000, debug=True)