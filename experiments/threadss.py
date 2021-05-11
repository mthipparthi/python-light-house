# # from concurrent.futures import ThreadPoolExecutor

# # import time


# # def wait_on_b():
# #     time.sleep(5)
# #     # print(b.result())  # b will never complete because it is waiting on a.
# #     return 5


# # def wait_on_a():
# #     time.sleep(5)
# #     # print(a.result())  # a will never complete because it is waiting on b.
# #     return 6


# # # def wait_on_future():
# # #     f = executor.submit(pow, 5, 2)
# # #     # This will never complete because there is only one worker thread and
# # #     # it is executing this function.
# # #     print(f.result())


# # # executor = ThreadPoolExecutor(max_workers=2)
# # # a = executor.submit(wait_on_b)
# # # b = executor.submit(wait_on_a)

# # # print(a.result())
# # # print(b.result())


# # # with ThreadPoolExecutor(max_workers=1) as executor:
# # #     future = executor.submit(pow, 2, 6)
# # #     print(future.result())


# # import concurrent.futures
# # import urllib.request

# # URLS = [
# #     "http://www.foxnews.com/",
# #     "http://www.cnn.com/",
# #     "http://europe.wsj.com/",
# #     "http://www.bbc.co.uk/",
# #     "http://some-made-up-domain.com/",
# # ]


# # def download_url(url, timeout):
# #     with urllib.request.urlopen(url, timeout=timeout) as conn:
# #         return conn.read()


# # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
# #     future_to_url = {executor.submit(download_url, url, 60): url for url in URLS}
# #     for future in concurrent.futures.as_completed(future_to_url):
# #         url = future_to_url[future]
# #         try:
# #             data = future.result()
# #         except Exception as exc:
# #             print("%r generated an exception: %s" % (url, exc))
# #         else:
# #             print("%r page is %d bytes" % (url, len(data)))

# # # if __name__ == "__main__":
# # #     main()


# import concurrent.futures
# import math

# PRIMES = [
#     112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293112272535095293,
#     112582705942171112272535095293115280095190773112272535095293109972689928541921324324423432112272535095293112272535095293115280095190773112272535095293109972689928541921324324423432112272535095293112272535095293,
#     112272535095293112272535095293112272535095293112272535095293,
#     115280095190773112272535095293109972689928541921324324423432112272535095293112272535095293,
#     115797848077099112272535095293115280095190773112272535095293109972689928541921324324423432112272535095293112272535095293,
#     109972689928541921324324423432112272535095293112272535095293,
# ]


# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# def main():
#     with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print("%d is prime: %s" % (number, prime))


# if __name__ == "__main__":
#     main()


import threading
import asyncio
from concurrent.futures import ProcessPoolExecutor

import time

process_pool = ProcessPoolExecutor()  # Default size is number of cores


async def handle_long_request(n):
    event_loop = asyncio.get_running_loop()
    # calculate_n_pi will be run in a separate process allowing the asyncio event
    # loop to continue to handle other async tasks in parallel
    value = await event_loop.run_in_executor(process_pool, calculate_n_pi, n)
    print(f"value :: {value}")
    return value


def calculate_n_pi(n):
    time.sleep(10)

    return n * 3.14


def main():

    event_loop = asyncio.get_event_loop()

    event_loop.run_until_complete(handle_long_request(1200000000000012312321242342423))

    # asyncio.gather(handle_long_request(120000000))


if __name__ == "__main__":
    main()
