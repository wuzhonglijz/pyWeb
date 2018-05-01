from flask import Flask, redirect, url_for, render_template, request
from config import DevConfig,Config,DatabaseConfig,ProdConfig
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config.from_object(DevConfig)
app.config.from_object(DatabaseConfig)
#app.config.from_object(ProdConfig)

db = SQLAlchemy(app)

class record(db.Model):
    name = db.Column(db.String(10), primary_key=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    go = db.Column(db.String(5), nullable=False)
    back = db.Column(db.String(5), nullable=False)
    where = db.Column(db.String(50), nullable=False)

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        all_data = record.query.all()
        return render_template('index.html', data= all_data)

    if request.method == 'POST':
        name = request.form.get('phone')
        data = json.loads(request.data)
        stu = record(name= data['name'], phone= int(data['phone']), go= data['go'],
                     back= data['back'], where= data['where'])
        db.session.add(stu)
        db.session.commit()
        print(stu)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        pass

@app.route('/<name>', methods=['GET'])
def name(name):
    return 'hello, %s' %name

@app.route('/ip', methods=['GET'])
def getip():
    return request.remote_addr

if __name__ == '__main__':
    app.run(host='0.0.0.0')