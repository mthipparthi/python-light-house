# Apply patches to stuff that blocks to enable gevent magic.
from gevent import monkey
from gevent.queue import Queue
import gevent

from gevent import Greenlet
import gevent

# from views import BackGroundLoopTask


monkey.patch_all()

from queues import *

from flask import g

import sys

sys.stdout = sys.stderr  # Redirect output to stderr.

from app import app  # Flask app, whatever...

# from views import BackGroundLoopTask

# gevent.spawn(BackGroundLoopTask)


from flask import g


# def get_task_queue():
#     if "task_queue" not in g:
#         g.task_queue = Queue()

#     return g.task_queue
# tasks = None


# class TaskQueue:
#     _queue = Queue()

#     def __init__(self):
#         pass

#     def pur(self, message):
#         self._queue.put(message)

#     def get(self, message):
#         return self._queue.get(message)


# def create_task_queue():
#     global tasks
#     if not tasks:
#         print("First time ....")
#         tasks = Queue()
#     return tasks


# class BackGroundLoopTask(Greenlet):
#     def __init__(self, run=None, *args, **kwargs):
#         super().__init__(run=run, *args, **kwargs)
#         self._running = True

#     def _run(self):
#         # task_queue = get_task_queue()
#         while self._running:
#             task = tasks.get()
#             print(f"I am working on task {task}")
#             gevent.sleep(0.1)


# @app.route("/task/<id>", methods=["GET",])
# def task_cb(id):
#     # gevent.spawn(hello_cb2)
#     tasks.put(int(id))
#     return f"Task Id {id}"


@app.before_first_request
def trigger_group_stats_bg_tasks():
    print("This function will run once")
    # from queues import BackGroundLoopTask

    # create_task_queue()
    # BackGroundLoopTask().start()
    with app.app_context():
        result = [BackGroundLoopTask(num=i).start() for i in range(10)]


from views import *
from gevent.pywsgi import WSGIServer

WSGIServer(("127.0.0.1", 8888), app).serve_forever()

