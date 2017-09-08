#!/usr/bin/env python
#encoding:utf-8

from flask import Flask, request, g, jsonify
from flask import abort
from flask import redirect
import json

app = Flask(__name__)

@app.route('/')
def index(): 
    return '{"error_code": 0, "msg": "yes, it is ture"}'


@app.route('/<name>')
def hello(name):
    return '<h1>Hello %s!</h1>' % name


@app.route('/user/<name>')
def sayHello(name):
    return '<h1>Hello %s!</h1>' % name


@app.route('/id/<idno>')
def get_info_by_no(idno):
    if int(idno) == 28394984004:
        return '{"error_code": 0, "msg": "id is true"}'
    else:
        return '{"error_code": 404, "msg": "id is not found"}'

@app.route('/get/args', methods=['GET'])
def get_get_args():
    """获取get请求参数"""
    key = request.args.get("key") 
    username = request.args.get("username") 
    response = {"key": key, "username": username}
    return jsonify(response)
    
        
@app.route('/post/form', methods=['POST'])
def post_form_data():
    """
    @desc: 本实例演示如何从post的form表单里获取数据
    """
    key = request.form.get('key')
    username = request.form.get("username")
    password = request.form.get("password")
    response = {"key": key, 
                "username": username,
                "password": password
                }
    return jsonify(response)


@app.route('/post/json', methods=['POST'])
def post_json_data():
    key = json.loads(request.get_data())
    return jsonify(key)
    

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0')