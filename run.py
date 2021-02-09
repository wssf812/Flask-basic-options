# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 9:15
# *Author*  : wssf
# *File*    : run.py
# *Software*: PyCharm

"flask的启动模块--用来控制程序"
from Flask_example import create_app,db
from flask_script import Manager #flask-script的作用是可以通过命令行的形式来操作Flask
from flask_migrate import Migrate,MigrateCommand #做数据库迁移。

app = create_app() #实例化一个app对象
manager = Manager(app) #实例化一个manager对象

Migrate(app,db=db) #绑定 数据库与app,建立关系

#MigrateCommand中是一个类，其中有一个option函数，他会将命令行参数拿到，返回给相应的方法中。
"""
    例如：
        python run.py db init -d xx --multidb xxx
        
        @MigrateCommand.option('-d', '--directory', dest='directory', default=None,
                           help=("Migration script directory (default is "
                                 "'migrations')"))
        @MigrateCommand.option('--multidb', dest='multidb', action='store_true',
                       default=False,
                       help=("Multiple databases migraton (default is "
                             "False)"))
        @catch_errors
        def init(directory=None, multidb=False):

"""
manager.add_command('db',MigrateCommand) #这条语句在flask-Script中添加一个db命令

if __name__ == '__main__':
    # app.run()
    # print(app.url_map)
    manager.run()
    """
    Map([<Rule '/home' (POST, GET, OPTIONS, HEAD) -> home.index>,
          <Rule '/' (OPTIONS, GET, HEAD) -> account.login>,
          <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
          
    其中：
          '/home' 
          '/' 路由在程序中使用 蓝图.route 修饰器定义 
          ‘/static/<filename>’ 路由是Flask 添加的特殊路由，用于访问静态文件。
          URL 映射中的 HEAD、Options、GET 是请求方法，由路由进行处理。HEAD 和 OPTIONS 方法由 Flask 自动处理。
          Flask 为每个路由都指定了请求方法，这样不同的请求方法发送到相同的 URL 上时，会使用不同的视图函数进行处理。
    """