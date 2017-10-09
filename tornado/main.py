import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/common")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import tornado.ioloop
import tornado.web
import tornado.httpserver
import traceback
import views
import urls
from multiprocessing import Manager, freeze_support

port = 8006

def main(first, app, num = 1):
    if str(first) == 'duo':
        freeze_support()
        print ("Quit the server with CONTROL-C.")
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.bind(port)
        http_server.start(num_processes = num) # tornado将按照cpu核数来fork进程
        tornado.ioloop.IOLoop.instance().start()
    elif str(first) == 'dan':
        app.listen(port)
        print ("Starting development server at http://127.0.0.1:" + str(port) )
        print ("Quit the server with CONTROL-C.")
        tornado.ioloop.IOLoop.instance().start()
    else:
        pass

if __name__ == "__main__":
    app = urls.application
    try:
        main("dan", app)
        #main("duo", app, 10)
    except:
        error_info = traceback.format_exc()
        print (error_info)
        main("dan", app)
