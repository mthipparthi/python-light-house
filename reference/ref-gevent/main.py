import gevent


def foo():
    print("Running in foo")
    gevent.sleep(1)
    print("Explicit context switch to foo again")


def bar():
    print("Explicit context to bar")
    gevent.sleep(0)
    print("Implicit context switch back to bar")


import time
import gevent
from gevent import select

start = time.time()
tic = lambda: "at %1.1f seconds" % (time.time() - start)


def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print("Started Polling: %s" % tic())
    select.select([], [], [], 2)
    print("Ended Polling: %s" % tic())


def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print("Started Polling: %s" % tic())
    select.select([], [], [], 2)
    print("Ended Polling: %s" % tic())


def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)


import gevent
import random


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2) * 0.001)
    print("Task %s done" % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


import gevent.monkey

gevent.monkey.patch_socket()

import gevent
import urllib3
import json


def fetch(pid):
    # response = urllib3.urlopen("http://json-time.appspot.com/time.json")
    http = urllib3.PoolManager()
    # response = http.open("http://json-time.appspot.com/time.json")
    response = http.request("GET", "http://httpbin.org/ip")
    # result = response.read()
    json_result = json.loads(response.data.decode("utf-8"))
    datetime = json_result["origin"]

    print("Process %s: %s" % (pid, datetime))
    return json_result["origin"]


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


import gevent
from gevent import Greenlet


def foo1(message, n):
    """
    Each thread will be passed the message, and n arguments
    in its initialization.
    """
    gevent.sleep(n)
    print(message)


import gevent
from gevent import Greenlet
import pysnooper

@pysnooper.snoop()
class MyGreenlet(Greenlet):
    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


import gevent
import signal


def run_forever():
    gevent.sleep(1000)


if __name__ == "__main__":
    # gevent.joinall(
    #     [gevent.spawn(foo), gevent.spawn(bar),]
    # )

    # gevent.joinall(
    #     [gevent.spawn(gr1), gevent.spawn(gr2), gevent.spawn(gr3),]
    # )

    # print("Synchronous:")
    # synchronous()

    # print("Asynchronous:")
    # asynchronous()

    # Initialize a new Greenlet instance running the named function
    # # foo
    # thread1 = Greenlet.spawn(foo1, "Hello", 1)

    # # Wrapper for creating and running a new Greenlet from the named
    # # function foo, with the passed arguments
    # thread2 = gevent.spawn(foo1, "I live!", 2)

    # # Lambda expressions
    # thread3 = gevent.spawn(lambda x: (x + 1), 2)

    # threads = [thread1, thread2, thread3]

    # # Block until all threads complete.
    # gevent.joinall(threads)

    g = MyGreenlet("Hi there!", 3)
    g.start()
    g.join()

    # gevent.signal(signal.SIGQUIT, gevent.kill)
    # thread = gevent.spawn(run_forever)
    # thread.join()
