# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 9:50
# *Author*  : wssf
# *File*    : home.py
# *Software*: PyCharm
"登陆后的处理模块"
from flask import Blueprint,render_template,session

hm = Blueprint("home",__name__)

@hm.route("/index",methods=['GET'])
def index():

    # print(session.get("user"))

    return render_template("home.html")