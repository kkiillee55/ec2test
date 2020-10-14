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
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://ambrose:12345678@ec2testdb.cdl6fshxaa2x.us-east-2.rds.amazonaws.com/ec2schema'
db=SQLAlchemy(app)
# c_info={
#     'host':'ec2testdb.cdl6fshxaa2x.us-east-2.rds.amazonaws.com',
#     'user':'ambrose',
#     'password':'12345678',
#     'cursorclass':pymysql.cursors.DictCursor,
# }
# conn=pymysql.connect(**c_info)
# cur=conn.cursor()
# res=cur.execute('show databases;')
# res=cur.fetchall()
# print('database: ',json.dumps(res,indent=4,default=str))

@app.route('/')
def home():
    data=db.session.execute('select * from ec2demo;')
    return render_template('home.html',data=data)

if __name__=='__main__':
    app.run(debug=True)