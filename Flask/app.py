#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import pymysql
from db import mysql_connect

app = Flask(__name__)


@app.route('/register/', methods=['POST'])
def register():
    data = request.data.decode('utf8')
    data = json.loads(data)
    print(data['username'])
    db_instance = mysql_connect('localhost',3306,'root','','fal')

    hata_dict = {"Hata": "Kullanıcı adı önceden kayıtlı Başka bir kullanıcı adı seçiniz!"}
    hata_dict2 = {"Hata": "Email Önceden kayıtlı"}

    if db_instance.getUsers(data['username']):
        return hata_dict
    elif db_instance.getUsersFromMail(data['email']):
        return hata_dict2
    else:
        pass
    # INSERT
    # INTO
    # `members`(`id`, `username`, `email`, `password`, `banned`, `created_at`, `updated_at`)
    # VALUES(NULL, 'deneme3', 'deneme3@gmail.com', '123456', '0', '2019-12-06 00:00:00', '2019-12-06 00:00:00');


    return request.data


@app.route('/login/', methods=["POST"])
def login():
    return request
