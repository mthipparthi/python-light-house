import gevent
from gevent import Greenlet


def spanning_threads():
    def foo(message, n):
        """
        Each thread will be passed the message, and n arguments
        in its initialization.
        """
        gevent.sleep(n)
        print(message)

    # Initialize a new Greenlet instance running the named function
    # foo
    thread1 = Greenlet.spawn(foo, "Hello", 1)

    # Wrapper for creating and running a new Greenlet from the named
    # function foo, with the passed arguments
    thread2 = gevent.spawn(foo, "I live!", 2)

    # Lambda expressions
    thread3 = gevent.spawn(lambda x: (x + 1), 2)

    threads = [thread1, thread2, thread3]

    # Block until all threads complete.
    gevent.joinall(threads)


import gevent


#  Greenlet State


def spanning_threads_catching_exception_within_greenlet():

    #  Greenlet State
    # Like any other segment of code, Greenlets can fail in various ways. A greenlet may fail to throw an exception, fail to halt or consume too many system resources.

    # The internal state of a greenlet is generally a time-dependent parameter. There are a number of flags on greenlets which let you monitor the state of the thread:

    # started -- Boolean, indicates whether the Greenlet has been started
    # ready() -- Boolean, indicates whether the Greenlet has halted
    # successful() -- Boolean, indicates whether the Greenlet has halted and not thrown an exception
    # value -- arbitrary, the value returned by the Greenlet
    # exception -- exception, uncaught exception instance thrown inside the greenlet

    def win():
        return "You win!"

    def fail():
        raise Exception("You fail at failing.")

    winner = gevent.spawn(win)
    loser = gevent.spawn(fail)

    print(winner.started)  # True
    print(loser.started)  # True

    # Exceptions raised in the Greenlet, stay inside the Greenlet.
    try:
        gevent.joinall([winner, loser])
    except Exception as e:
        print("This will never be reached")

    print(winner.value)  # 'You win!'
    print(loser.value)  # None

    print(winner.ready())  # True
    print(loser.ready())  # True

    print(winner.successful())  # True
    print(loser.successful())  # False

    # The exception raised in fail, will not propagate outside the
    # greenlet. A stack trace will be printed to stdout but it
    # will not unwind the stack of the parent.

    print(loser.exception)


import signal


def program_shutdown():
    def run_forever():
        gevent.sleep(1000)

    gevent.signal(signal.SIGQUIT, gevent.kill)

    thread = gevent.spawn(run_forever)
    thread.join()


import gevent
from gevent import Timeout


def thread_timeout():

    seconds = 10
    timeout = Timeout(seconds)
    timeout.start()

    def wait():
        gevent.sleep(10)

    try:

        wait_gt = gevent.spawn(wait)
        gevent.joinall([wait_gt])
        print(wait_gt.exception)
    except Timeout:
        print("Could not complete")


if __name__ == "__main__":
    # spanning_threads()
    # spanning_threads_catching_exception_within_greenlet()
    # program_shutdown()
    thread_timeout()

