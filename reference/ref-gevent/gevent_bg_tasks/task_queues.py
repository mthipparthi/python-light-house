import abc
import functools
import json
import logging
import time
import uuid
from datetime import datetime


from gevent import monkey

monkey.patch_all()
import pytz

import gevent
from gevent.lock import Semaphore
from gevent.queue import Queue

from gevent import Greenlet


class TaskManager(object):

    # This contains details of worker type
    # worker, num of workers, and its queue
    WORKER_QUEUES = {}
    RUNNING_TASKS_BY_WORKER_TYPE = {}

    def add_worker(self, worker_type, worker, worker_task_queue, num_of_workers=2):
        self.WORKER_QUEUES[worker_type] = (worker, worker_task_queue, num_of_workers)

    def start_all(self):
        for worker_type, value in self.WORKER_QUEUES.items():
            worker, _, num_of_workers = value
            gls = [worker() for i in range(num_of_workers)]
            self.RUNNING_TASKS_BY_WORKER_TYPE[worker_type] = gls
            # for gl in gls:
            #     gl.start()

            #     # breakpoint()

            _ = [gl.start() for gl in gls]

    def start_by_group(self, worker_type):
        worker, _, num_of_workers = self.WORKER_QUEUES.get(
            worker_type, (None, None, None)
        )
        if worker and num_of_workers:
            gls = [worker() for i in range(num_of_workers)]
            self.RUNNING_TASKS_BY_WORKER_TYPE[worker_type] = gls
            _ = [gl.start() for gl in gls]

    def stop_all(self):
        for worker_type, v in self.RUNNING_TASKS_BY_WORKER_TYPE.items():
            self._wait_to_finish(worker_type)
            gevent.killall(v)

        self.RUNNING_TASKS_BY_WORKER_TYPE.clear()

    def stop_by_group(self, worker_type):
        _tasks = self.RUNNING_TASKS_BY_WORKER_TYPE.get(worker_type, [])
        if _tasks:
            self._wait_to_finish(worker_type)
            gevent.killall(_tasks)
            del self.RUNNING_TASKS_BY_WORKER_TYPE[worker_type]

    def _wait_to_finish(self, worker_type):
        _, _queue, _ = self.WORKER_QUEUES.get(worker_type, (None, None, None))
        if _queue:
            while not _queue().empty():
                gevent.sleep(seconds=1)

    @classmethod
    def add_task(cls, worker_type, messages):
        # Every worker must have its own queue
        # tasks must be added to respective queue

        _, _queue, _ = cls.WORKER_QUEUES.get(worker_type, (None, None, None))
        if _queue:
            if isinstance(messages, list):
                _queue().mput(messages)
            else:
                _queue().put(messages)


class TaskQueue(object):
    _queue = Queue()
    _wlock = Semaphore()
    _rlock = Semaphore()

    def __init__(self):
        pass

    def put(self, message):
        with self._wlock:
            self._queue.put(message)

    def mput(self, messages):
        with self._wlock:
            for message in messages:
                self._queue.put(message)

    def get(self):
        return self._queue.get()

    def mget(self, num):
        # breakpoint()
        with self._rlock:
            # print(f"{id(self)} -- in q")
            print(f"Reamining  ... {self._queue.qsize()}")
            print(f"Reamining  ... {self._queue}")
            rv2 = [self._queue.get() for i in range(num)]

            return rv2

    def qsize(self):
        return self._queue.qsize()

    def empty(self):
        return self._queue.empty()


class StatsTaskQueue(TaskQueue):
    pass


import requests


class StatisticsDispatchTaskV2(Greenlet):

    running = True

    def __init__(self):
        Greenlet.__init__(self)
        self.stat_event_list = []
        self.task_queue = StatsTaskQueue()

    def dispatch(self, msg):
        response = requests.post("https://httpbin.org/post", json={"msg": msg})
        if not response.ok:
            raise Exception("No good")
        print("Successs")

    def _run(self):
        # breakpoint()
        while self.running:
            try:
                # print(self)
                # print()
                messages = self.task_queue.mget(2)
                if messages:
                    print(f"{id(self)} - {messages}")
                    self.dispatch(msg=messages)
                    # gevent.sleep(seconds=1)
                else:
                    print(f"{id(self)} - I am sleeping")
                    gevent.sleep(seconds=2)
            except Exception as ex:
                print(ex)
                self.task_queue.mput(messages)

    def task_name(self):
        return "statistics-dispatching"


import gevent
from gevent import Greenlet


class ItemGenerator(Greenlet):
    def __init__(self):
        Greenlet.__init__(self)

    def _run(self):
        _task_manager = TaskManager()
        for i in range(1, 2000):
            items = random.randint(220, 300)
            _task_manager.add_task("WORKER_TYPE_GROUP_STATS", [items])


class WelcomeGenerator(Greenlet):
    def __init__(self):
        Greenlet.__init__(self)

    def _run(self):
        num2 = 100
        while True:
            print("Hello world")
            gevent.sleep(1)

            num = random.randint(1, 10)
            if num >= 5:
                num2 += 1
                print(f"Adding number {num2}")
                _task_manager = TaskManager()
                _task_manager.add_task("WORKER_TYPE_GROUP_STATS", [num2])


def start_tasks():
    _task_manager = TaskManager()
    _task_manager.add_worker(
        "WORKER_TYPE_GROUP_STATS", StatisticsDispatchTaskV2, StatsTaskQueue, 3,
    )
    _task_manager.start_all()


import random
import time


def main():
    start_tasks()
    g = ItemGenerator()
    # w = WelcomeGenerator()
    # w.start()
    g.start()
    g.join()
    # w.join()

    time.sleep(100)


if __name__ == "__main__":
    main()
