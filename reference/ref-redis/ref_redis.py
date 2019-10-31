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
    # r.set("foo", "bar")
    # i = '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'

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


def update(r):
    itemid = "NEXTUP:2GB11"
    index = "MY2GBINDEX11"

    with r.pipeline() as pipe:
        pipe.watch(index)
        val = pipe.get(itemid)
        print(f"Before {val}")
        pipe.incrby(itemid, 1)
        val = pipe.get(itemid)
        print(f"Afterr {val}")
        val = val.decode("utf-8")
        index_str = f"2GB:segment_20191016_0000{val}.ts:{val}"

        pipe.zadd(index, index_str, 0)
        print(index_str)

        op = pipe.zrangebylex(index, "[2GB:segment_20191016_000000", "[2GB:segment_20191016_000030")

        print(op)
        # member = member + ":" + str(incr)

        pipe.unwatch()


import threading

read_lock = threading.RLock()


import random


def update_redis_index(ts_file_name):
    try:

        channel_index = "channel:index:gs:{}".format("4BC")
        channel_nextup_index = "channel:nextup:gs:{}".format("4BC")

        read_lock.acquire()

        r = redis.Redis(host="127.0.0.1", port=6379, db=0, socket_timeout=5, retry_on_timeout=True)

        with r.pipeline() as pipe:

            pipe.watch(channel_nextup_index)
            pipe.incrby(channel_nextup_index, 1)

            nextup_val = pipe.get(channel_nextup_index)
            nextup_val = nextup_val.decode("utf-8")

            absolute_url = "https://storage.googleapis.com/{}/{}/{}".format(
                "target_bucket", "2GB", ts_file_name
            )

            index_str = "{};{};{};{}".format(ts_file_name, nextup_val, "2gb", absolute_url)

            # pipe.zadd(channel_index, 0, index_str)
            # pipe.zadd(channel_index, index_str=0)
            print("****" * 10)
            print(index_str)
            print("####" * 10)

            mapping = {index_str: 0}

            # pl = {}
            # pl[index_str] = 0

            key = "maheshhhhh{}".format(random.randint(1, 10))

            pipe.zadd(channel_index, {index_str: 0})

            pipe.zadd("z", {"z1": 1})

            # pipe.zadd(channel_index, {index_str: 0})

            print("Updated Redis Index with  {} for channel".format(index_str))

            # result = pipe.zrangebylex(
            #     channel_index, "[segment_20191016_100002000", "[segment_20191016_100003000"
            # )

            op = pipe.zrangebylex(
                channel_index, "[segment_20191030_000010", "[segment_20191030_000020"
            )

            # op = pipe.zrangebylex(channel_index, "[maheshhhhh0", "[maheshhhhh10")

            print("OUTPUT *** ")

            print(op)

            # op = pipe.zremrangebylex(
            #     channel_index, "[segment_20191030_000010", "[segment_20191030_000020"
            # )

            # print(op)

            pipe.unwatch()

        read_lock.release()

    except Exception as ex:
        print("Failed to Update Redis for channel {} - {}".format("2GB", ex))


import threading

if __name__ == "__main__":
    # r = redis.Redis(host="127.0.0.1", port=6379, db=0)
    threads = []
    for i in range(5):
        # threading.Thread(update)
        index_str = f"segment_20191030_00001{i}.ts"
        t = threading.Thread(target=update_redis_index, args=(index_str,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


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
