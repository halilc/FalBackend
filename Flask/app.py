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
hata_dict4 = {"Hata": "Lütfen Tüm alanları doldurunuz !"}
hata_dict5 = {"Hata": "Lüften geçerli bir email giriniz !"}
hata_dict6 = {"Hata": "Giriş Başarısız . Tekrar Deneyiniz !"}
hata_dict7 = {"Hata": "Çıkış Başarısız !"}



onay_dict = {"Onay": "Kayıt Başarılı  !","token": ""}
onay_dict2 = {"Onay": "Giriş Başarılı !"}
onay_dict3 = {"Onay": "Giriş Başarılı  !","token": ""}
onay_dict4 = {"Onay": "Çıkış Başarılı !"}

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
    if db_instance.getUser(username):
        return hata_dict
    elif db_instance.getUsersFromMail(email):
        return hata_dict2
    else:
        if db_instance.createUser(username, email, password, create_time) == 1:
            token = db_instance.createToken(email,create_time)
            print(token)
            onay_dict['token'] = str(token)
            return onay_dict
        else: return  hata_dict3


@app.route('/login/', methods=["POST"])
def login():
    data = request.data.decode('utf8')
    data = json.loads(data)
    email = data['email']
    password = data['password']
    result = db_instance.LoginUser(email,password)
    if result == 1:
        token = db_instance.createToken(email, str(current_time))
        onay_dict3['token'] = str(token)
        return onay_dict3
    else: return hata_dict6

@app.route('/logout/', methods=["POST"])
def logout():
    data = request.data.decode('utf8')
    data = json.loads(data)
    username = data['username']
    try:
        result = db_instance.LogoutUser(username)
        return  onay_dict4
    except:
        return hata_dict7
    # print(result)
