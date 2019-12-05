#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
app = Flask(__name__)
import pymysql

@app.route('/sign', methods=['POST'])

def sign():
    # read the posted values from the UI
    # req_data = request.get_json()
    # name = req_data['name']
    # return name
    #if request.method == 'POST':
        #print(request.form.get('name'))
        #return jsonify(request.form.get('name'))
    # data = jsonify(request.data)
    # print(data)
    # data = json.loads(str(request.data))
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')

    cur = conn.cursor()
    cur.execute("SELECT * FROM `members`")
    for row in cur:
        print(row)
    data = request.data.decode('utf8')
    print(data)
    data = json.loads(data)
    print(data['user_id'])

    return request.data


@app.route('/login/', methods=["POST"])
def login():
    return request
