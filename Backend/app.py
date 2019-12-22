#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import pymysql
from datetime import datetime
# from FlaskApp.db import mysql_connect
from db import mysql_connect
# print(secrets.token_urlsafe(10))
from apscheduler.schedulers.background import BackgroundScheduler


current_time = datetime.now()
app = Flask(__name__)
hata_dict = {"Hata": "Kullanıcı adı önceden kayıtlı Başka bir kullanıcı adı seçiniz!"}
hata_dict2 = {"Hata": "Email Önceden kayıtlı"}
hata_dict3 = {"Hata": "Tekrar Deneyiniz !"}
hata_dict4 = {"Hata": "Lütfen Tüm alanları doldurunuz !"}
hata_dict5 = {"Hata": "Lüften geçerli bir email giriniz !"}
hata_dict6 = {"Hata": "Giriş Başarısız . Tekrar Deneyiniz !"}
hata_dict7 = {"Hata": "Çıkış Başarısız !"}
hata_dict8 = {"Hata": "Fal Gönderilirken hata oluştu !"}


onay_dict = {"Onay": "Kayıt Başarılı  !","token": ""}
onay_dict2 = {"Onay": "Giriş Başarılı !"}
onay_dict3 = {"Onay": "Giriş Başarılı  !","token": ""}
onay_dict4 = {"Onay": "Çıkış Başarılı !"}

onay_dict5 = {"Onay": "Fal Gönderildi  !"}



# db_instance = mysql_connect('89.19.30.126',3306,'u8279158_fal','CAneren93049304','u8279158_fal')

class connection_db():
    def __init__(self):
        self.db_instance = mysql_connect('89.19.30.126', 3306, 'u8279158_fal', 'u8279158_fal', 'CAneren93049304')



@app.route('/')
def hello():
    return render_template('hello.html')

# print(db_instance.checkDB())

@app.route('/register/', methods=['POST'])
def register():
    db_instance = connection_db().db_instance

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
    db_instance = connection_db().db_instance

    data = request.data.decode('utf8')
    data = json.loads(data)
    email = data['email']
    password = data['password']
    try:
        result = db_instance.LoginUser(email,password)
        if result == 1:
            token = db_instance.createToken(email, str(current_time))
            onay_dict3['token'] = str(token)
            return onay_dict3
        else:
            return hata_dict6
    except:
        return hata_dict6


@app.route('/logout/', methods=["POST"])
def logout():
    data = request.data.decode('utf8')
    data = json.loads(data)
    username = data['username']
    try:
        db_instance = connection_db().db_instance
        result = db_instance.LogoutUser(username)
        return  onay_dict4
    except:
        return hata_dict7
    # print(result)

@app.route('/sendfortune/', methods=["POST"])
def sendfortune():
    # print("################")
    # db_instance = mysql_connect('89.19.30.126', 3306, 'u8279158_fal', 'u8279158_fal', 'CAneren93049304')
    db_instance = connection_db().db_instance

    data = request.data.decode('utf8')
    data = json.loads(data)
    token = data['token']
    image1 = data['image1']
    image2 = data['image2']
    image3 = data['image3']
    created_at = str(current_time)
    id = db_instance.getUserID(token)
    if id == 0:
        return hata_dict8
    sending = db_instance.sendFortune(id,image1,image2,image3,created_at)
    if sending == 0:
        return hata_dict8
    return onay_dict5


def checkWaiting():
    print("Bekleyen")
    db_instance = connection_db().db_instance
    db_instance.sendFortune()
    # print(db_instance.sendFortune())
    # print(db_instance.getWaitings())
def test():
    print("q")

scheduler = BackgroundScheduler()
scheduler.add_job(func=test(), trigger="interval", seconds=1)
scheduler.start()
