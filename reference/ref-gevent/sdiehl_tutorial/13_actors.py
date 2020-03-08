# Actors
# The actor model is a higher level concurrency model popularized by the language Erlang. In short the main idea is that you have a collection of independent Actors which have an inbox from which they receive messages from other Actors. The main loop inside the Actor iterates through its messages and takes action according to its desired behavior.

# Gevent does not have a primitive Actor type, but we can define one very simply using a Queue inside of a subclassed Greenlet.

import gevent
from gevent.queue import Queue


class Actor(gevent.Greenlet):
    def __init__(self):
        Greenlet.__init__(self)
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
        gevent.sleep(0)


class Ponger(Actor):
    def receive(self, message):
        print(message)
        ping.inbox.put("pong")
        gevent.sleep(0)


ping = Pinger()
pong = Ponger()

ping.start()
pong.start()

ping.inbox.put("start")
gevent.joinall([ping, pong])
