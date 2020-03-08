# Events
# Events are a form of asynchronous communication between Greenlets.


import gevent
from gevent.event import Event

"""
Illustrates the use of events
"""


def async_communication_through_events():
    evt = Event()

    def setter():
        """After 3 seconds, wake all threads waiting on the value of evt"""
        print("A: Hey wait for me, I have to do something")
        gevent.sleep(3)
        print("Ok, I'm done")
        evt.set()

    def waiter():
        """After 3 seconds the get call will unblock"""
        print("I'll wait for you")
        evt.wait()  # blocking
        print("It's about time")

    gevent.joinall(
        [
            gevent.spawn(setter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
            gevent.spawn(waiter),
        ]
    )


# AsyncResult
# An extension of the Event object is the AsyncResult which allows you to send a value along with the wakeup call. This is sometimes called a future or a deferred, since it holds a reference to a future value that can be set on an arbitrary time schedule.


import gevent
from gevent.event import AsyncResult

a = AsyncResult()


def async_communication_through_async_results():
    a = AsyncResult()

    def setter():
        """
        After 3 seconds set the result of a.
        """
        gevent.sleep(3)
        a.set("Hello!")

    def waiter():
        """
        After 3 seconds the get call will unblock after the setter
        puts a value into the AsyncResult.
        """
        print(a.get())

    gevent.joinall(
        [gevent.spawn(setter), gevent.spawn(waiter),]
    )


# Queues

# Queues are ordered sets of data that have the usual put / get operations but are written in a way such that they can be safely manipulated across Greenlets.

# For example if one Greenlet grabs an item off of the queue, the same item will not be grabbed by another Greenlet executing simultaneously.

if __name__ == "__main__":
    # async_communication_through_events()
    async_communication_through_async_results()

