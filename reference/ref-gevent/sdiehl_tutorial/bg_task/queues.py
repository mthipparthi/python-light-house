import gevent

from gevent import Greenlet
from gevent.queue import Queue
from gevent.lock import Semaphore

# https://gist.github.com/ls0f/2bf398b70e359f3ecf36


class TaskQueue:
    _queue = Queue()
    _lock = Semaphore()

    def __init__(self):
        pass

    def put(self, message):
        with self._lock:
            self._queue.put(message)

    def get(self):
        return self._queue.get()


class BackGroundLoopTask(Greenlet):
    def __init__(self, run=None, *args, **kwargs):
        self._num = kwargs.pop("num", None)
        self._running = True
        self._task_queue = kwargs.pop("task_queue", TaskQueue())
        super().__init__(run=run, *args, **kwargs)

    def _run(self):
        while self._running:
            message = self._task_queue.get()
            print(f"Thread {self._num} working on task {message}")
            gevent.sleep(0.1)

    def stop(self):
        self._running = False


def add_to_task_queue(message):
    TaskQueue().put(message)
