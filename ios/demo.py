# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo
   Description :
   Author :       simplefly
   date：          2017/12/20
-------------------------------------------------
   Change Activity:
                   2017/12/20:
-------------------------------------------------
"""
__author__ = 'simplefly'

import requests
import re
import pymysql

conn = pymysql.connect(
    host='',
    port=3306,
    user='',
    passwd='',
    db=''
)


url = 'http://www.quanshuwang.com/list/1_1.html'
def getSortNovelList():
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)"'
    novelUrlList = re.findall(reg, result)
    return novelUrlList

def getNovelInfo(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    print(result)

for novelName,novelUrl in getSortNovelList():
    print(novelName, novelUrl)