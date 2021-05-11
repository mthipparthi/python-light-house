import threading
import time
import heapq
from collections import deque


def count_up(stop):
    i = 0
    while i < stop:
        i += 1
        print(f"UP {i}")
        time.sleep(1)


def count_down(stop):
    i = stop
    while i > 0:
        i -= 1
        print(f"Down {i}")
        time.sleep(1)


class Scheduler:
    def __init__(self) -> None:
        self.ready = deque()
        self.sleeping = []
        self.sequence = 0

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))

    def run(self):
        while self.ready or self.sleeping:

            if not self.ready:
                deadline, _, func = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta <= 0:
                    self.ready.append(func)

            while self.ready:
                func = self.ready.popleft()
                func()


sch = Scheduler()


def countup(stop, i=0):
    if i < stop:
        i += 1
        print(f"UP {i}")
        time.sleep(1)
        # sch.call_soon(lambda: countup(stop, i))
        sch.call_later(4, lambda: countup(stop, i))


def countdown(stop):
    if stop >= 0:
        stop -= 1
        print(f"DOWN {stop}")
        time.sleep(1)
        # sch.call_soon(lambda: countdown(stop))
        sch.call_later(0, lambda: countdown(stop))


def countup_itr(stop):
    def _run(x):
        if x < stop:
            print(f"UP ITR {x}")
            time.sleep(1)
            # sch.call_soon(lambda: _run(x + 1))
            sch.call_later(1, lambda: _run(x + 1))

    _run(0)


import queue


class AsyncQueue:
    def __init__(self) -> None:
        self.items = deque()
        self.waiting = deque()

    def put(self, item):
        self.items.append(item)
        if self.waiting:
            func = self.waiting.popleft()
            sch.call_soon(func)

    def get(self, callback):
        if self.items:
            callback(self.items.popleft())
        else:
            self.waiting.append(lambda: self.get(callback))


def producer(q, count):
    # for i in range(count):
    #     print("Producing ", i)
    #     time.sleep(1)
    #     q.put(i)

    # q.put(None)

    def _run(n):
        if n < count:
            print("Producing ", n)
            q.put(n)
            sch.call_later(0, lambda: _run(n + 1))
        else:
            print("Producing Done")
            q.put(None)

    _run(0)


# def producer(q, count):
#     def _run(n):
#         if n < count:
#             print("Producing", n)
#             q.put(n)
#             sch.call_later(0, lambda: _run(n + 1))
#         else:
#             print("Producer done")
#             q.put(None)

#     _run(0)


# def consumer(q):
#     def _consume(item):
#         if item is None:
#             print("Consumer done")
#         else:
#             print("Consuming", item)
#             sch.call_soon(lambda: consumer(q))

#     q.get(callback=_consume)


def consumer(q):
    # while True:
    #     item = q.get()
    #     if item is None:
    #         break
    #     print("Consuming ", item)

    def _consume(item):
        if item is None:
            print("Consuming Done")
        else:
            print("Consuming", item)
            sch.call_soon(lambda: consumer(q))

    q.get(callback=_consume)


q = AsyncQueue()
# sched = Scheduler()


class Result:
    def __init__(self, value=None, exc=None) -> None:
        self.val = value
        self.exc = exc

    def result(self):
        if self.exc:
            raise self.exc

        return self.val


def main():
    # Sequential execution
    # count_up(10)
    # count_down(10)

    # Threads execution\
    # threading.Thread(target=count_up, args=(10,)).start()
    # threading.Thread(target=count_down, args=(10,)).start()

    # Achievning concurrency without threads.

    # sch = Scheduler()
    # sch.call_soon(lambda: countup_itr(5))
    # sch.call_soon(lambda: countdown(5))
    # sch.run()
    # q = queue.Queue()
    # producer(q, 20)
    # consumer(q)
    # threading.Thread(target=producer, args=(q, 20)).start()
    # threading.Thread(target=consumer, args=(q,)).start()

    # q = AsyncQueue()
    # sch = Scheduler()
    # sch.call_soon(lambda: producer(q, 100))
    # sch.call_soon(lambda: consumer(q))
    # sch.run()

    q = AsyncQueue()
    # sched = Scheduler()
    sch.call_soon(lambda: producer(q, 10))
    sch.call_soon(lambda: consumer(q,))
    sch.run()


if __name__ == "__main__":
    main()

