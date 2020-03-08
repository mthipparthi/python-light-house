# Thread Locals
# Gevent also allows you to specify data which is local to the greenlet context. Internally, this is implemented as a global lookup which addresses a private namespace keyed by the greenlet's getcurrent() value.


import gevent
from gevent.local import local
from gevent import getcurrent


def thread_local():

    stash = local()

    def f1():
        stash.x = 1
        print(stash.x)
        print(getcurrent())

    def f2():
        stash.y = 2
        print(stash.y)
        print(getcurrent())

        try:
            stash.x
        except AttributeError:
            print("x is not local to f2")

    g1 = gevent.spawn(f1)
    g2 = gevent.spawn(f2)

    gevent.joinall([g1, g2])


# Many web frameworks that use gevent store HTTP session objects inside gevent thread locals. For example, using the Werkzeug utility library and its proxy object we can create Flask-style request objects.


# Flask's system is a bit more sophisticated than this example, but the idea of using thread locals as local session storage is nonetheless the same.

from gevent.local import local
from werkzeug.local import LocalProxy
from werkzeug.wrappers import Request
from contextlib import contextmanager


# from gevent.wsgi import WSGIServer
from gevent.pywsgi import WSGIServer

_requests = local()
request = LocalProxy(lambda: _requests.request)
import pysnooper


@contextmanager
def sessionmanager(environ):
    _requests.request = Request(environ)
    yield
    _requests.request = None


def logic():
    return "Hello " + request.remote_addr + "\n"


from werkzeug.wrappers import Response


@pysnooper.snoop()
def application(environ, start_response):

    with sessionmanager(environ):
        body = logic()
    response = Response(body, mimetype="text/plain")
    return response(environ, start_response)


if __name__ == "__main__":

    WSGIServer(("127.0.0.1", 8088), application).serve_forever()

