from app import app
import gevent

from gevent import Greenlet
from flask import g
from queues import add_to_task_queue


# @app.route("/hello", methods=["GET",])
# def hello_cb():
#     # gevent.spawn(hello_cb2)
#     bg = BackGroundTask()
#     bg.start()
#     print("hello World")

#     return "hello World"


# class BackGroundTask2(Greenlet):
#     def __init__(self, run=None, *args, **kwargs):
#         super().__init__(run=run, *args, **kwargs)

#     def _run(self):
#         gevent.sleep(9)
#         print(f"BackGroundTask2 m: Hello world i am late by 9")


# class BackGroundTask(Greenlet):
#     def __init__(self, run=None, *args, **kwargs):
#         super().__init__(run=run, *args, **kwargs)

#     def _run(self):
#         bg = BackGroundTask2()
#         bg.start()
#         # gevent.sleep(5)
#         print(f"BackGroundTask: Hello world i am late by 5")


# class BackGroundLoopTask(Greenlet):
#     def __init__(self, run=None, *args, **kwargs):
#         super().__init__(run=run, *args, **kwargs)
#         self._running = True

#     def _run(self):
#         while self._running:
#             task = g.task_queue.get()
#             print(f"I am working on task {task}")
#             gevent.sleep(0.1)


@app.route("/task/<id>", methods=["GET",])
def task_cb(id):
    add_to_task_queue(int(id))
    return f"Task Id {id}"
