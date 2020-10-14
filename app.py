from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
import os
'''
for windows: 
set username=your username
set password=your password
set dbserver=your dbserver

for linux
change set to export
'''
username=os.environ['username']
password=os.environ['password']
dbserver=os.environ['dbserver']
print('mysql+pymysql://{}:{}@{}'.format(username,password,dbserver))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://{}:{}@{}'.format(username,password,dbserver)

db=SQLAlchemy(app)


@app.route('/')
def home():
    data=db.session.execute('select * from ec2demo;')
    return render_template('home.html',data=data)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)