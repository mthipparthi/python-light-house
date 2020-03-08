# Locks and Semaphores
# A semaphore is a low level synchronization primitive that allows greenlets to coordinate and limit concurrent access or execution. A semaphore exposes two methods, acquire and release The difference between the number of times a semaphore has been acquired and released is called the bound of the semaphore. If a semaphore bound reaches 0 it will block until another greenlet releases its acquisition.

from gevent import sleep
from gevent.pool import Pool
from gevent.lock import BoundedSemaphore


def semaphore_test():

    sem = BoundedSemaphore(2)

    def worker1(n):
        sem.acquire()
        print("Worker %i acquired semaphore" % n)
        sleep(0)
        sem.release()
        print("Worker %i released semaphore" % n)

    def worker2(n):
        with sem:
            print("Worker %i acquired semaphore" % n)
            sleep(0)
        print("Worker %i released semaphore" % n)

    pool = Pool()
    pool.map(worker1, range(0, 2))
    pool.map(worker2, range(3, 6))


# A semaphore with bound of 1 is known as a Lock. it provides exclusive execution to one greenlet. They are often used to ensure that resources are only in use at one time in the context of a program.

if __name__ == "__main__":
    semaphore_test()
