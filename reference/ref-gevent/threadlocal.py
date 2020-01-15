from gevent.local import local
from werkzeug.local import LocalProxy
from werkzeug.wrappers import Request
from contextlib import contextmanager
import pysnooper


# from gevent.wsgi import WSGIServer
from gevent.pywsgi import WSGIServer

_requests = local()
request = LocalProxy(lambda: _requests.request)


@contextmanager
def sessionmanager(environ):
    _requests.request = Request(environ)
    yield
    _requests.request = None


def logic():
    return "Hello " + request.remote_addr + "\n"


# @pysnooper.snoop()
# def application(environ, start_response):
#     status = "200 OK"

#     with sessionmanager(environ):
#         body = logic()

#     headers = [("Content-Type", "text/html")]

#     # status = status.encode()

#     start_response(status, headers)
#     return [body]


from werkzeug.wrappers import Response


def application(environ, start_response):

    with sessionmanager(environ):
        body = logic()
    response = Response(body, mimetype="text/plain")
    return response(environ, start_response)


if __name__ == "__main__":

    WSGIServer(("127.0.0.1", 8088), application).serve_forever()

