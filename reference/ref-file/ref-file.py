import sys
import time
import functools
import sys
import multiprocessing
import os


def timeit(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = fn(*args, **kwargs)
        end = time.time()
        print(f" EXECUTION Time {end-start}")
        return rv

    return wrapper


@timeit
def read_file():
    print(f"File size {os.path.getsize(sys.stdin)}")
    for line in sys.stdin:
        pass


@timeit
def main():
    print(read_file.__name__)
    read_file()


from multiprocessing import Process


from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, "hello"])


# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())  # prints "[42, None, 'hello']"
#     p.join()

if __name__ == "__main__":
    main()
