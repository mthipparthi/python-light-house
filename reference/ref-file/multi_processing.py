import functools
import multiprocessing
import os
import random
import string
import sys
import time
import sympy


# 200 for Id, 1024 for chars
BLOCK_SIZE = 48 * 1024 * 1024


def timeit(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = fn(*args, **kwargs)
        end = time.time()
        print(f"\nEXECUTION Time {end-start} \n")
        return rv

    return wrapper


def validate(chunk):
    rv = []
    for line in chunk.split("\n"):
        line = line.split(",")
        if len(line) >= 2:
            record_id = int(line[0])
            if record_id < 200 and sympy.isprime(int(record_id)):
                continue
            rv.append(line[0])
    return "\n".join(rv)


def read_file():
    with sys.stdin as f:
        while True:
            buffer = f.read(BLOCK_SIZE)
            if buffer:
                yield buffer
            else:
                return


@timeit
def main():
    with multiprocessing.Pool() as pool:
        result = pool.map(validate, read_file())
        sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    main()
