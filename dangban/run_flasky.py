#!/usr/bin/env python
#encoding:utf-8

from flask import Flask
from flask import abort
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/')
def index(): 
    return '{"error_code": 0, "msg": "yes, it is ture"}'


@app.route('/<name>')
def hello(name):
    return '<h1>Hello %s!</h1>' % name


@app.route('/user/<name>')
def sayHello(name):
    return '<h1>Hellos %s!</h1>' % name
	

@app.route('/iboxpay-credit/nciicQuery.htm',methods=[ 'POST'])
def get_identify_by_id():
	
    if request.form['id'] == 440981198810023753 and request.form['name'] == 'lijiale':
        return '{"result":0}'
    else:
        return '{"result":1}'
		

'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
'''
@app.route('/id/<idno>')
def get_info_by_no(idno):
    if int(idno) == 28394984004:
        return '{"error_code": 0, "msg": "id is true"}'
    else:
        return '{"error_code": 404, "msg": "id is not found"}'
    
    
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')