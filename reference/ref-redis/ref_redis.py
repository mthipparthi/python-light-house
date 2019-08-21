import redis

import random
import json

# from rediscluster import StrictRedisCluster


def pl():
    v = {}
    v[
        "location"
    ] = "https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"

    k = "2GB:20181214:0142{}".format(random.randint(20, 40))

    d = {}
    d[k] = v
    return json.dumps(d)


def zrange_main():
    r = redis.Redis(host="192.168.99.100", port=6379, db=0)
    r.set("foo", "bar")
    i = '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'

    # r.zadd("anotherindex1", {i: 0})

    for i in range(10, 30):
        val = pl()
        # print(val)
        r.zadd("anotherindex100", {val: 0})

    for i in r.zrangebylex(
        "anotherindex100", '[{"2GB:20181214:014235', '[{"2GB:20181214:014237:\xff'
    ):
        # print(i)
        print(json.loads(i))


def bit_main():
    r = redis.Redis(host="192.168.99.100", port=6379, db=0)
    key = "20181214"
    r.setbit(key, 20000000, 1)
    r.setbit(key, 2, 1)
    r.setbit(key, 220000000, 1)

    print(r.getbit(key, 20000000))
    print(r.memory_usage(key))
    # print(r.get(key))


def my_main():
    host = "ds-peakalerts.ukl672.clustercfg.apse2.cache.amazonaws.com"
    # port = 6379
    # r = redis.Redis()
    key = "20181214"
    r = redis.Redis(host=host, port=6379, db=0)
    # nodes = [{"host": host, "port": 6379}]
    # r = redis.StrictRedisCluster(startup_nodes=nodes, skip_full_coverage_check=True)

    r.setbit(key, 20000000, 1)
    r.setbit(key, 2, 1)
    r.setbit(key, 220000000, 1)

    print(r.getbit(key, 20000000))
    print(r.memory_usage(key))


import random


def create_memeber(r, member):
    key = "peakalert_savesearch_index"

    incr = r.incrby(member)
    previous_member = member + ":" + str(incr - 1)
    member = member + ":" + str(incr)

    r.zrem(key, previous_member)
    r.zadd(key, member, 0)


def peak_alert_index():
    r = redis.Redis(host="192.168.99.100", port=6379, db=0)
    key = "peakalert_savesearch_index"
    for i in range(1, 100):
        member = f"201909{i}:alert2001"
        # print(member)
        incr = r.incrby(member)
        # print(incr)
        # print(incr)
        previous_member = member + ":" + str(incr - 1)
        member = member + ":" + str(incr)

        # key = f"{key}"
        # print(f"key: {key} val: {val}")
        r.zrem(key, previous_member)
        r.zadd(key, member, 0)

        # r.zincrby(key, member, incr)

        # ZINCRBY key increment member

    rslt = None
    start = "[20190985:alert2001"
    end = "(20190999:alert2001"
    rslt = r.zrangebylex(key, start, end)
    print(rslt)
    rslt = r.zlexcount(key, start, end)
    print(rslt)

    print(r.zscore(key, "alert2001:20190910"))


def event_id():
    r = redis.Redis(host="192.168.99.100", port=6379, db=0)
    id = r.incr("event:id")
    event = {}
    event["id"] = id
    event_key = "event:{id}".format(id=id)
    print(event_key)


# ZRANGEBYLEX anotherindex [2GB:20181214:014200 [2GB:20181214:014250:\xff


def record_event(conn, event):
    id = conn.incr("event:id")
    event["id"] = id
    event_key = f"event:{id}"

    pipe = conn.pipeline(True)
    pipe.hmset(event_key, event)
    pipe.zadd("events", **{str(id): event["timestamp"]})
    pipe.execute()


def test_re():
    from datetime import datetime

    conn = redis.Redis(host="192.168.99.100", port=6379, db=0)
    timestamp = int(datetime.now().timestamp())
    event = {}
    event["timestamp"] = timestamp
    record_event(conn, event)


if __name__ == "__main__":
    peak_alert_index()


# Redis Notes
#  https://stackoverflow.com/questions/40917622/get-redis-values-while-scanning
#  Hierchic indexes...
# 127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
# (integer) 1
# 127.0.0.1:6379>
# 127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
# (integer) 0
# 127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014222:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
# (integer) 1
# 127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014232:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
# (integer) 1
# 127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014242:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
# (integer) 1
# 127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014225:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
# (integer) 1
# 127.0.0.1:6379> ZRANGEBYLEX anotherindex [2GB:20181214:014200 [2GB:20181214:014250:\xff
# 1) "2GB:20181214:014222:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 2) "2GB:20181214:014225:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 3) "2GB:20181214:014227:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 4) "2GB:20181214:014232:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 5) "2GB:20181214:014242:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 127.0.0.1:6379> ZRANGEBYLEX anotherindex [2GB:20181214:014200 [2GB:20181214:014230:\xff
# 1) "2GB:20181214:014222:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 2) "2GB:20181214:014225:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
# 3) "2GB:20181214:014227:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}" */


# https://stackoverflow.com/questions/54150125/get-a-python-docker-container-to-interact-with-a-redis-docker-container

# docker run --network=host --name some-redis_2 -d redis redis-server --appendonly yes --port 6379:6379
# --network=host   -- very important
