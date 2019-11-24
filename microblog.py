# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:50:56 2019

@author: qxz0ga0
"""
from app import app, db
from app.models import User, Post, Device


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Device': Device}