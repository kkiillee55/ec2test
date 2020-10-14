from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://ambrose:12345678@ec2testdb.cdl6fshxaa2x.us-east-2.rds.amazonaws.com/ec2schema'
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
    app.run(host='0.0.0.0',debug=True)