#!/usr/bin/python3
# coding: utf-8
from app import app, db
from app.models import User, Post

@app.shell_context_processor  # flask shell 提前 import 的东西
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
