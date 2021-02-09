# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 9:23
# *Author*  : wssf
# *File*    : models.py
# *Software*: PyCharm
"flask的数据模块（与数据库建立映射的模块）-模型，定义模型结构，获取数据库中的表的映射关系。"

from Flask_example import db #当前目录下的db,也就是__init__中声明的db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),unique=True) #用户名唯一
    password = db.Column(db.String(100)) #保存数据的时候要变成加密格式


    # 自定义输出实例化对象时的信息
    def __repr__(self):
        return "<Users %r>" % self.id # %r会重现所表达的对象(会将后面给的参数原样打印出来)

    # 验证哈希密码
    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash  # 专门用来验证哈希密码
        return check_password_hash(self.password, pwd)

