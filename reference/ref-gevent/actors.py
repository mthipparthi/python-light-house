import gevent
from gevent.queue import Queue


class Actor(gevent.Greenlet):
    def __init__(self):
        super().__init__()
        self.inbox = Queue()

    def receive(self, message):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        self.running = True

        while self.running:
            message = self.inbox.get()
            self.receive(message)


import gevent
from gevent.queue import Queue
from gevent import Greenlet


class Pinger(Actor):
    def receive(self, message):
        print(message)
        pong.inbox.put("ping")
        gevent.sleep(1)


class Ponger(Actor):
    def receive(self, message):
        print(message)
        print("Hello from pong Greenlet %s" % id(getcurrent()))
        ping.inbox.put("pong")
        gevent.sleep(2)


ping = Pinger()
pong = Ponger()

ping.start()
pong.start()

ping.inbox.put("start")
gevent.joinall([ping, pong])


# class Pinger(Actor):
#     def receive(self, message):
#         print(message)
#         print("Hello from ping Greenlet %s" % id(getcurrent()))
#         pong.inbox.put("ping")
#         gevent.sleep(10)


# class Ponger(Actor):
#     def receive(self, message):
#         print(message)
#         print("Hello from pong Greenlet %s" % id(getcurrent()))
#         ping.inbox.put("pong")
#         gevent.sleep(10)


# ping = Pinger()
# pong = Ponger()

# ping.start()
# pong.start()

# ping.inbox.put("start")
# gevent.joinall([ping, pong])
