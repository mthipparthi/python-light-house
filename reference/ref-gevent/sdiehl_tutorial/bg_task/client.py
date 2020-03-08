from cutils import *

from queues import TaskQueue


if __name__ == "__main__":
    tq = TaskQueue()
    tq.put("heello1")
    print(tq.get())

    tq1 = TaskQueue()
    tq1.put("heello21")
    print(tq1.get())
