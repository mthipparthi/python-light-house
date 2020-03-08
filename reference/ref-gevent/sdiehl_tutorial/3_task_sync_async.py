import gevent
import random


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2) * 0.01)
    print("Task %s done" % pid)


def sync_task():
    for i in range(5):
        task(i)


def async_task():
    gevent.joinall([gevent.spawn(task(i)) for i in range(5)])


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


if __name__ == "__main__":
    sync_task()
    async_task()

    print("Synchronous:")
    synchronous()

    print("Asynchronous:")
    asynchronous()
