#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import pymysql
from Backend.Flask.db import mysql_connect

app = Flask(__name__)


@app.route('/register/', methods=['POST'])
def register():
    data = request.data.decode('utf8')
    # print(data)
    data = json.loads(data)
    # print(data['username'])


    db_instance = mysql_connect('localhost',3306,'root','','fal')
    print(db_instance.getUsers(data['username']))


    #
    # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM `members`")
    # #
    # # print(cur)
    # for row in cur:
    #     print(row)
    # INSERT
    # INTO
    # `members`(`id`, `username`, `email`, `password`, `banned`, `created_at`, `updated_at`)
    # VALUES(NULL, 'deneme3', 'deneme3@gmail.com', '123456', '0', '2019-12-06 00:00:00', '2019-12-06 00:00:00');


    return request.data


@app.route('/login/', methods=["POST"])
def login():
    return request
