# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 8:57
# *Author*  : wssf
# *File*    : __init__.py.py
# *Software*: PyCharm
"初始化文件，初始化整个Flask对象，以及Flask所用的各种插件"

from flask import Flask ,session
from flask_sqlalchemy import SQLAlchemy
from ext.auth import Auth
#包含了SQLAlchemy相关的所有操作
db = SQLAlchemy()

from .views import account
from .views import home

def create_app():
    """将创建app的过程封装成函数，放到__init__.py中，是为了防止run.py（启动文件）代码太多
    （因为app是核心对象，所有的东西都会围绕app来做，有很多第三方组件都要注册到app中，蓝图之类的也是。）
    """
    app = Flask(__name__)  # 核心对象
    #导入配置第一种方式
    app.config.from_object("settings.DevelopmentConfig")
    #导入配置第二种方式
    # from settings import DevelopmentConfig
    # app.config.from_object(DevelopmentConfig)

    #第一种将app注册到db中的方式，在init_app就会读取app.config配置中的东西，帮助Sqlalchemy做链接
    # db = SQLAlchemy(app)
    # 第二种将app注册到db中的方式，在init_app就会读取app.config配置中的东西
    db.init_app(app)

    #验证是否登录：两种方式
    #第一种：将app传入init_app方法
    # auth = Auth()
    # auth.init_app(app)
    #第二种：直接将app当做参数传给Auth类
    Auth(app)

    #注册蓝图
    app.register_blueprint(account.ac)
    app.register_blueprint(home.hm)
    return app