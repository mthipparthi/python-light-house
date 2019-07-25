import time
import sys
import schedule
from flask import Flask, escape, request

from collections import deque
import threading

app = Flask(__name__)
import logging

q = deque()
# logging.basicConfig(format="%(threadName)s:%(message)s")
logging.basicConfig(format="%(thread)d %(threadName)s:%(message)s")


def job(message="Hello"):
    print(f"I'm working...{message}")


@app.route("/")
def hello():
    logging.error(f"Endpoint hello: {threading.get_ident()} ")
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"


@app.route("/qadd/<int:val>")
def add(val):
    print(f"Adding val {val}")
    q.append(val)
    return f"Value, {escape(val)}!"


# @app.route("/start_sch/{<int:kill>}")
@app.route("/start_sch/<int:kill>")
def start(kill):
    # print(sys.get)

    logging.error(f"Endpoint start_sch: {threading.get_ident()}")

    schedule.every(1).minutes.do(job, message="EVery minute")
    schedule.every(2).minutes.do(job, message="EVery 10 minute")
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every(5).to(10).minutes.do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().minute.at(":17").do(job)

@app.before_first_request
def process_queue():
    print(f"process_queue ")

    def job():
        while True:
                val = q.pop() if q else None
                if val:
                    print(f"Processing {val}")
                else:
                    time.sleep(1)

    thread = threading.Thread(target=job)
    thread.start()
    return


def main():
    # app.before_first_request(process_queue)
    app.run(debug=True)


# if __name__ == "__main__":
#     main()


# # app.before_first_request(process_queue)
# # process_queue()


# import threading
# import time
# from flask import Flask

# app = Flask(__name__)
# from collections import deque

# q = deque()


# @app.before_first_request
# def activate_job():
#     def run_job():
#         print(f"STARTTTTTT task ")
#         while True:
#             val = q.pop() if q else None
#             if val:
#                 print(f"Run recurring task {val}")
#             else:
#                 time.sleep(3)

#     thread = threading.Thread(target=run_job)
#     thread.start()


# @app.route("/")
# def hello():
#     return "Hello World!"


# @app.route("/add/<int:val>")
# def add(val):
#     q.append(val)
#     return f"val added{val}"


if __name__ == "__main__":
    app.run(debug=True)
