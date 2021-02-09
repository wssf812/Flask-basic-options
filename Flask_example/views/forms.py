# -*- coding: utf-8 -*-
# *Time*    : 2021/2/2 13:09
# *Author*  : wssf
# *File*    : forms.py
# *Software*: PyCharm

"表单标签生成以及表单验证模块"
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(
        label="用户名:",
        description="用户名",
        validators=[
            DataRequired("请输入用户名！")
        ],
        #体现在html表单控件里面，给html表单加上属性的！
        render_kw={
            'class':'form-control',
            "placeholder": "请输入密码！" ,# 占位符
            #"required": False
        }

    )

    password = PasswordField(
        label="密码:",
        description="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        render_kw={
            'class': 'form-control',
            "placeholder": "请输入密码！",  # 占位符
            #"required": False
        }
    )

    submit = SubmitField("提交")