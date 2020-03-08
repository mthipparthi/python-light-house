import gevent
import gevent.monkey
import gevent

gevent.monkey.patch_socket()


import requests


def fetch(url):
    resp = requests.get(url)
    if resp.ok:
        print(resp)
        print(resp.text)


def main():
    urls = [f"http://127.0.0.1:8888/task/{task}" for task in range(22200, 22300)]
    gevent.joinall([gevent.spawn(fetch, url) for url in urls])


if __name__ == "__main__":
    main()
