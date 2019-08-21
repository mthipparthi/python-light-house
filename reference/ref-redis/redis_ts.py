import redis

import random
import json
from redis_timeseries import TimeSeries
from datetime import datetime
import time
import calendar
import functools
import operator
from collections import OrderedDict
from datetime import datetime

seconds = lambda i: i
minutes = lambda i: i * seconds(60)
hours = lambda i: i * minutes(60)
days = lambda i: i * hours(24)
weeks = lambda i: i * days(7)
months = lambda i: i * weeks(4)


def get_grans():
    return OrderedDict(
        [
            ("1minute", {"duration": minutes(1), "ttl": days(120)}),
            # ("5minute", {"duration": minutes(5), "ttl": hours(6)}),
            # ("10minute", {"duration": minutes(10), "ttl": hours(12)}),
            ("1hour", {"duration": hours(1), "ttl": days(120)}),
            ("1day", {"duration": days(1), "ttl": days(120)}),
            ("1week", {"duration": weeks(1), "ttl": days(120)}),
        ]
    )


from datetime import datetime


def get_data():
    pass


def main():
    # r = redis.Redis(host="192.168.99.100", port=6379, db=0)
    key = "peakalert_savesearch_index"

    client = redis.Redis(host="192.168.99.100", port=6379, db=0)

    ts = TimeSeries(client, base_key="peakalert_ts_db", granularities=get_grans())

    ts.record_hit("event:123")

    # time.sleep(10)

    # ts.record_hit("event:123")
    # time.sleep(10)
    # ts.record_hit("event:123")
    # time.sleep(10)

    print(ts.get_hits("event:123", "1day", 30))
    print(days(7))


if __name__ == "__main__":
    main()
