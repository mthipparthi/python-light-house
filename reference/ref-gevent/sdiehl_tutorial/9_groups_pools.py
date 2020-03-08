# Groups and Pools
# A group is a collection of running greenlets which are managed and scheduled together as group. It also doubles as parallel dispatcher that mirrors the Python multiprocessing library.
import gevent
from gevent.pool import Group


def groups_and_pools():
    def talk(msg):
        for i in range(3):
            print(msg)

    g1 = gevent.spawn(talk, "bar")
    g2 = gevent.spawn(talk, "foo")
    g3 = gevent.spawn(talk, "fizz")

    group = Group()
    group.add(g1)
    group.add(g2)
    group.join()

    group.add(g3)
    group.join()


# This is very useful for managing groups of asynchronous tasks.

# As mentioned above, Group also provides an API for dispatching jobs to grouped greenlets and collecting their results in various ways.
import gevent
from gevent import getcurrent
from gevent.pool import Group


def group_parallelism():
    group = Group()

    def hello_from(n):
        print("Size of group %s" % len(group))
        print("Hello from Greenlet %s" % id(getcurrent()))

    group.map(hello_from, range(3))

    def intensive(n):
        gevent.sleep(3 - n)
        return "task", n

    print("Ordered")

    ogroup = Group()
    for i in ogroup.imap(intensive, range(3)):
        print(i)

    print("Unordered")

    igroup = Group()
    for i in igroup.imap_unordered(intensive, range(3)):
        print(i)


# A pool is a structure designed for handling dynamic numbers of greenlets which need to be concurrency-limited. This is often desirable in cases where one wants to do many network or IO bound tasks in parallel.
import gevent
from gevent.pool import Pool


def pool_parallelism():

    pool = Pool(2)

    def hello_from(n):
        print("Size of pool %s" % len(pool))

    pool.map(hello_from, range(3))


class SocketPool(object):
    def __init__(self):
        self.pool = Pool(1000)
        self.pool.start()

    def listen(self, socket):
        while True:
            socket.recv()

    def add_handler(self, socket):
        if self.pool.full():
            raise Exception("At maximum pool size")
        else:
            self.pool.spawn(self.listen, socket)

    def shutdown(self):
        self.pool.kill()


if __name__ == "__main__":
    # groups_and_pools()
    # group_parallelism()
    pool_parallelism()
