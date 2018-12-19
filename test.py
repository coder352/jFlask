#!/usr/bin/python3
# coding: utf-8
from app.models import User, Post
from app import db
# 上面这些在 flask shell 中不用输入
# @app.shell_context_processor  # flask shell 提前 import 的东西
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}
##################################################################
## 添加用户
u = User(username='susan', email='susan@example.com')
u.set_password('cat')
db.session.add(u)
db.session.commit()
