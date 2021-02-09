# -*- coding: utf-8 -*-
# *Time*    : 2021/2/3 10:06
# *Author*  : wssf
# *File*    : 操作db离线脚本.py
# *Software*: PyCharm
"离线脚本，用来创建数据库，插入数据，可以在不启动flask程序的基础上"

from Flask_example import db
from Flask_example import create_app
from werkzeug.security import generate_password_hash  # 导入加密工具
from Flask_example import models
app = create_app()

with app.app_context():
    # db.create_all() #根据类创建所有表
    user = models.Users(
        username="liu",
        password=generate_password_hash("123456")
    )
    # 向数据库中增加数据
    db.session.add(user)
    # 提交数据
    db.session.commit()
