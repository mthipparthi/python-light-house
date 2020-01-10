import gevent
from gevent import Timeout


def wait():
    gevent.sleep(2)


timer = Timeout(1).start()
thread1 = gevent.spawn(wait)

try:
    thread1.join(timeout=timer)
except Timeout:
    print("Thread 1 timed out")

print("thread1")
# --

timer = Timeout.start_new(1)
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer)
except Timeout:
    print("Thread 2 timed out")

print("thread2")
# --

try:
    gevent.with_timeout(1, wait)
    gevent.joinall()
except Timeout:
    print("Thread 3 timed out")

print("thread3")

