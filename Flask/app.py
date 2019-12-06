#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import pymysql
from Backend.Flask.db import mysql_connect
from datetime import datetime




# print(secrets.token_urlsafe(10))


current_time = datetime.now()
app = Flask(__name__)
hata_dict = {"Hata": "Kullanıcı adı önceden kayıtlı Başka bir kullanıcı adı seçiniz!"}
hata_dict2 = {"Hata": "Email Önceden kayıtlı"}
hata_dict3 = {"Hata": "Tekrar Deneyiniz !"}
onay_dict = {"Onay": "Kayıt Başarılı  !","token": ""}
hata_dict4 = {"Hata": "Lütfen Tüm alanları doldurunuz !"}
hata_dict5 = {"Hata": "Lüften geçerli bir email giriniz !"}
db_instance = mysql_connect('localhost',3306,'root','','fal')
@app.route('/register/', methods=['POST'])
def register():
    data = request.data.decode('utf8')
    data = json.loads(data)
    # print(data['username'])
    username = data['username']
    email = data['email']
    password = data['password']
    create_time = str(current_time)


    if len(username) < 1 or len(email) < 1 or len(password) < 1:
        return hata_dict4
    if not "@" in email:
        return hata_dict5
    if db_instance.getUsers(username):
        return hata_dict
    elif db_instance.getUsersFromMail(email):
        return hata_dict2
    else:
        if db_instance.createUser(username, email, password, create_time) == 1:
            token = db_instance.createToken(username,create_time)
            print(token)
            onay_dict['token'] = str(token)
            return onay_dict
        else: return  hata_dict3

@app.route('/login/', methods=["POST"])
def login():
    return request
