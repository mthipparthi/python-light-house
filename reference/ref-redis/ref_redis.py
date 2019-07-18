import redis

import random
import json


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


if __name__ == "__main__":
    bit_main()


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
