# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     app
   Description :
   Author :       simplefly
   date：          2017/12/19
-------------------------------------------------
   Change Activity:
                   2017/12/19:
-------------------------------------------------
"""
__author__ = 'simplefly'

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Micro Blog</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    # 创建一个web服务器对象
    app = web.Application(loop=loop)
    # 通过router的指定的方法可以把请求的链接和对应的处理函数关联在一起
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
