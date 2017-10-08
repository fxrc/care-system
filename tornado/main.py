import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/common")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import tornado.ioloop
import tornado.web
import tornado.httpserver
import views
import urls


port = 8006

def main(first, app):
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

if __name__ == "__main__":
    app = urls.application
    try:
        main("duo", app)
    except:
        main("dan", app)
