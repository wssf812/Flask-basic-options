# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 9:17
# *Author*  : wssf
# *File*    : ext.py
# *Software*: PyCharm
"""
    用作登录时的验证模块--项目扩展库/第三方扩展库打包处理
"""
from flask import request,session,redirect

class Auth(object):
    "登录验证插件-验证用户是否登录"
    def __init__(self,app=None):
        "初始化函数"
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self,app):

        app.auth_manager = self #给当前app增加auth_manager属性，赋值为当前auth对象

        #相当于@app.before_request --再请求之前执行验证操作
        app.before_request(self.check_login)

        # 也是一个特殊的装饰器，等价于@app.context_processor
        app.context_processor(self.context_processor)

    def check_login(self):
        "验证用户是否登录"
        if request.path == "/":
            return
        else:
            #获取用户sesssion
            user = session.get("user")
            print("user:",user)
            #不存在时，返回登录页
            if not user:
               return redirect("/")

    def context_processor(self):
        "获取当前登录用户"
        """
          @app.context_processor 作为一个装饰器修饰一个函数
          函数的返回结果必须是dict, 然后其key将会作为变量在所有模板中可见

          当你的很多视图函数中需要回传一个相同的变量的时候，这个时候就可以考虑使用context_processor了
        """

        return dict(current_user = session.get("user"))

    def login(self,data):
        "保存登录时的session"
        session["user"] = data

    def loginout(self):
        "清除保存的session"

        #通过 del 语句删除不在使用的变量
        del session["user"] #del(session["user"])也可以,一种时语句的形式，一种时函数的形式