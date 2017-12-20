# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     config_default
   Description :
   Author :       simplefly
   date：          2017/12/20
-------------------------------------------------
   Change Activity:
                   2017/12/20:
-------------------------------------------------
"""
__author__ = 'simplefly'

configs = {
    'debug': True,
    'db':{
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www',
        'password': 'www',
        'db': 'microblog'
    },
    'session':{
        'secret': 'Microblog'
    }
}
