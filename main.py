from flask import Flask,redirect,url_for,render_template
from config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

@app.route('/',  methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/<name>', methods=['GET'])
def name(name):
    return 'hello, %s' %name

if __name__ == '__main__':
    app.run(host='0.0.0.0')