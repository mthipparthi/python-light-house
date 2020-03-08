import gevent
import sys
import time


def foo():
    print("Running in foo", file=sys.stderr)
    gevent.sleep(10)
    print("Explicit context switch to foo again", file=sys.stderr)


def bar():
    print("Explicit context to bar", file=sys.stderr)
    gevent.sleep(0)


if __name__ == "__main__":
    gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
