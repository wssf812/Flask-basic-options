# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 9:46
# *Author*  : wssf
# *File*    : account.py
# *Software*: PyCharm
"登录退出账号相关模块-视图函数，处理业务逻辑，协调模板和模型之间的关系"

# render_template是模板渲染，例如在开发flask项目中，我们会有一个templates文件夹，里面存放一些html文件，这些文件会在视图函数中被渲染，此时就会用到render_template包
from flask import Blueprint,render_template,request,redirect,session,flash,url_for,current_app
from Flask_example.views.forms import LoginForm
from Flask_example import db
from Flask_example.models import Users
ac = Blueprint("account",__name__)

# @ac.before_request
# def bf():
#     "在视图函数之前执行"
#     print("before requests")


@ac.route("/",methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method =="GET":
        return render_template("login.html",form = form)
    else:
        #调用validte_on_submit方法，可以一次性执行完所有的验证函数的逻辑。
        if form.validate_on_submit():
            data = form.data  # 请求的数据
            print("dwdwdwdw",data)
            username = data["username"]
            password = data["password"]

            #去数据库中查询，存在时返回一个对象
            #第一种,将model.User类传入到session.query中
            # userobj = db.session.query(Users).filter(Users.username == username，Users.password = password).first()
            # 后续要是在没有数据库操作，把连接去掉。
            # db.session.remove()

            #第二种，直接使用User类进行操作(两种方式)
            users = Users.query.filter(Users.username==username).first()
            # users = Users.query.filter_by(username= username).first()
            print(users)

            #验证账号是否错误
            if not users:
                flash("账号错误！")
                return redirect(url_for("account.login"))

            #验证密码是否错误（验证哈希密码）
            if not users.check_pwd(password):
                flash("密码错误！")
                return redirect(url_for("account.login"))

            #当成功的时候保存session并且重定向到index页面.
            #第一种方式直接保存session
            # session["user"] = username
            #第二种方式将保存session的过程放到auth自己写的插件中。这样更整齐，防止session的key不同产生错误

            #从当前app中获取auth中的为app增加的属性。
            current_app.auth_manager.login(username)

            return redirect("/index")

@ac.route("/loginout",methods=["GET"])
def loginout():
    current_app.auth_manager.loginout()
    return redirect(url_for("account.login"))