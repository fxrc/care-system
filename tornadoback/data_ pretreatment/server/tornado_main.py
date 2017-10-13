# -*- coding:utf-8 -*-
import tornadoback.options
import tornadoback.httpserver
import tornadoback.ioloop
from tornadoback.options import options,define
from server.url import MyApplication
define("port",default=8002,help="跑在8002",type=int)


def tornado_main():
    print('start')
    tornadoback.options.parse_command_line()
    app=MyApplication()
    # app.listen(options.port)
    http_server = tornadoback.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(1)    #如果为0,则根据cpu自己创建一定舒服的fork，如果是大于等于1的，则创建对应数目的fork
    tornadoback.ioloop.IOLoop.instance().start()


