# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request
from config import DevConfig,Config,DatabaseConfig,ProdConfig
from flask_sqlalchemy import SQLAlchemy
import json
import time

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
    all_data = record.query.all()
    if request.method == 'GET':
        return render_template('index.html', data= all_data)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = json.loads(request.data)
        try:
            name = data['name']
            phone = int(data['phone'])
            go = data['go']
            back = data['back']
            where = data['where']
            if (go=='' or back=='' or where==''):
                raise ValueError
            stu = record(name=name, phone=phone, go=go, back=back, where=where)
            db.session.add(stu)
        except ValueError:
            return '输入有误, 请检查一下哪里出错了'
        db.session.commit()
        db.session.close()
        print('committed!')
        return ''


@app.route('/ip', methods=['GET'])
def getip():
    return request.remote_addr

@app.route('/del', methods=['POST', 'GET'])
def dl():
    if request.method == 'GET':
        all_data = record.query.all()
        for i in range(1, 20):
            try:
                x = record.query.filter_by(name='wzl' + str(i)).one()
                db.session.delete(x)
            except:
                pass
            db.session.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')