from tornado.ioloop import IOLoop
import tornado.web
import cPickle as pickle
from tornado.web import RequestHandler, StaticFileHandler
import color
import pdb
import base64

class BackdoorApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/set', SetHandler),
            (r'/get', GetHandler),
            (r'/exec', ExecuteHandler),
        ]
        settings = dict(
            xsrf_cookies= False, # turn off cross-site forgery cookies.
            template_path = 'experiment/templates', # if you use tornado templates, store them in here
            # xsrf_cookies = True, # prevent xsrf bugs (see http://tornado.readthedocs.org/en/latest/guide/security.html )
            debug = True, # leave this true for much easier debugging
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class SetHandler(RequestHandler):
    def post(self):
        try:
            data = pickle.loads(self.request.body)
            assert(type(data) == dict)
            globals().update(data)
            self.write(pickle.dumps({'response': 'OK'}))
            color.msg_ok('[SET]', str(data))
        except Exception as e:
            color.msg_err('[ERROR]', e.message)
            self.write(pickle.dumps({'response', e.message}))

class GetHandler(RequestHandler):
    def post(self):
        try:
            data = pickle.loads(self.request.body)
            assert(hasattr(type(data), '__iter__'))
            resp = dict({key: globals()[key] for key in data})
            self.write(pickle.dumps(resp))
            color.msg_ok('[GET]', str(resp))
        except Exception as e:
            color.msg_err('[ERROR]', e.message)
            self.write(pickle.dumps({}))

class ExecuteHandler(RequestHandler):
    def post(self):
        try:
            cmds = pickle.loads(self.request.body)
            for cmd in cmds:
                color.blue()
                print '[RUN]', cmd
                color.end()
                exec cmd in globals()
            self.write(pickle.dumps({'response': 'OK'}))
            color.msg_ok('[EXEC]', 'done')
        except Exception as e:
            color.msg_err('[ERROR]', e.message)
            self.write(pickle.dumps({'response', e.message}))

if __name__ == '__main__':
    backdoor = BackdoorApp()
    backdoor.listen(port=8899)
    IOLoop.instance().start()