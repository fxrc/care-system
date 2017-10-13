# -*- coding:utf-8 -*-
import tornadoback
from server.request import *

class MyApplication(tornadoback.web.Application):
    def __init__(self):
        handlers = [
            (r"/getabnormalstu", GetAbnormalStu),

        ]

        settings = {

        }

        tornadoback.web.Application.__init__(self, handlers, **settings, debug = False)
                #使用多进程的时候，记得设置为false


#MyApplication = tornadoback.web.Application(handlers = handlers,**settings)
