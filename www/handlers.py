# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     handlers
   Description :
   Author :       simplefly
   date：          2017/12/21
-------------------------------------------------
   Change Activity:
                   2017/12/21:
-------------------------------------------------
"""
__author__ = 'simplefly'

import re, time, json, logging, hashlib, base64, asyncio
from www.coreweb import get, post
from www.models import User,Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'index.html',
        'users': users
    }
