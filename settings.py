# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 9:17
# *Author*  : wssf
# *File*    : settings.py
# *Software*: PyCharm

"flask的配置模块，将所有的配置信息放到这里-项目配置文件，配置整个项目运行环境"
from datetime import timedelta

class Config(object):
    DEBUG = True #是否调试
    TESTING = False #是否测试
    SECRET_KEY = "asdfghjkl" #跟sesssion有关，本质上是一个加密盐，可以防止csrf
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20) #配置session超时时间

class ProductionConfig(Config):
    "生产环境"
    ENV = "production"

class DevelopmentConfig(Config):
    "开发环境"
    ENV = "development"
    #SESSION_TYPE = 'redis'#session类型为redis。
    #SESSION_KEY_PREFIX = 'session'#保存到session中的值的前缀。
    #SESSION_PREMANENT = TRUE #如果设置为False，则关闭浏览器session就会失效。
    #SESSION_USE_SIGNER = Flase #是否对发送到浏览器上的session:cookie值进行加密。

    #用于连接的数据库 URI 。
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8"
    #数据库连接池的大小。默认是引擎默认值（通常 是 5 ）
    SQLALCHEMY_POOL_SIZE = 5
    #设定连接池的连接超时时间。默认是 10。
    SQLALCHEMY_POOL_TIMEOUT = 30
    #多少秒后自动回收连接。
    SQLALCHEMY_POOL_RECYCLE = -1
    #追踪对象的修改并且发送信号
    SQLALCHEMTY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    "测试环境"
    ENV = "testing"
