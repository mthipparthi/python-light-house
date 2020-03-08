# Queues
# Queues are ordered sets of data that have the usual put / get operations but are written in a way such that they can be safely manipulated across Greenlets.

# For example if one Greenlet grabs an item off of the queue, the same item will not be grabbed by another Greenlet executing simultaneously.
import gevent


from gevent import monkey, sleep

monkey.patch_all()
from gevent.queue import Queue


def gevent_queues():
    tasks = Queue()

    def worker(n):
        while True:
            task = tasks.get()
            print("Worker %s got task %s" % (n, task))
            gevent.sleep(1)

        print("Quitting time!")

    def boss():
        for i in range(1, 25):
            tasks.put_nowait(i)

    gevent.spawn(boss).join()

    gevent.joinall(
        [
            gevent.spawn(worker, "steve"),
            gevent.spawn(worker, "john"),
            gevent.spawn(worker, "nancy"),
        ]
    )


if __name__ == "__main__":
    gevent_queues()

