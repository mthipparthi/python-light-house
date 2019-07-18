```
 ~/work/projects  docker exec -it 9a2d33eedf05 bash
root@default:/data# ls -ltr
total 28
-rw-r--r-- 1 redis redis 24774 Jul 17 07:11 appendonly.aof
root@default:/data# redis-cli
127.0.0.1:6379> set users:leto '{"name": "leto", "planet": "dune", "likes": ["spice"]}'
OK
127.0.0.1:6379> SET users:leto '{"name": "leto", "planet": "dune", "likes": ["spice"]}'
OK
127.0.0.1:6379> get users:leto
"{\"name\": \"leto\", \"planet\": \"dune\", \"likes\": [\"spice\"]}"
127.0.0.1:6379> SET users:leto1 '{"name": "leto", "planet": "dune", "likes": ["spice"]}'
OK
127.0.0.1:6379> SET users:leto2 '{"name": "leto", "planet": "dune", "likes": ["spice"]}'
OK
127.0.0.1:6379> get users:leto
"{\"name\": \"leto\", \"planet\": \"dune\", \"likes\": [\"spice\"]}"
127.0.0.1:6379> get users:leto*
(nil)
127.0.0.1:6379> get users:leto\d
(nil)
127.0.0.1:6379> set users:leto '{"name": leto, "planet": dune, "likes": ["spice"]}'
OK
127.0.0.1:6379> set users:leto '{"name": leto, "planet": dune, "likes": ["spice"]}' EX 40
OK
127.0.0.1:6379> get users:leto
"{\"name\": leto, \"planet\": dune, \"likes\": [\"spice\"]}"
127.0.0.1:6379> get users:leto
"{\"name\": leto, \"planet\": dune, \"likes\": [\"spice\"]}"
127.0.0.1:6379> get users:leto
(nil)
127.0.0.1:6379> get users:leto
(nil)
127.0.0.1:6379> set users:leto '{"name": leto, "planet": dune, "likes": ["spice"]}' EX 5
OK
127.0.0.1:6379> get users:leto
"{\"name\": leto, \"planet\": dune, \"likes\": [\"spice\"]}"
127.0.0.1:6379> get users:leto
"{\"name\": leto, \"planet\": dune, \"likes\": [\"spice\"]}"
127.0.0.1:6379> get users:leto
"{\"name\": leto, \"planet\": dune, \"likes\": [\"spice\"]}"
127.0.0.1:6379> get users:leto
(nil)
127.0.0.1:6379> getrange users:leto 31 48
""
127.0.0.1:6379> set users:leto '{"name": leto, "planet": dune, "likes": ["spice"]}' EX 5
OK
127.0.0.1:6379> getrange users:leto 31 48
"\"likes\": [\"spice\"]"
127.0.0.1:6379> getrange users:leto 31 48 
root@default:/data# ^C
root@default:/data# ^C
root@default:/data# set users:leto '{"name": leto, "planet": dune, "likes": ["spice"]}'
root@default:/data# ^C
root@default:/data# getrange users:leto 31 48
bash: getrange: command not found
root@default:/data# redis-cli
127.0.0.1:6379> set users:leto '{"name": leto, "planet": dune, "likes": ["spice"]}'
OK
127.0.0.1:6379> getrange users:leto 31 48
"\"likes\": [\"spice\"]"
127.0.0.1:6379> strlen users:leto
(integer) 50
127.0.0.1:6379> append users:leto " OVER 9000!!"
(integer) 62
127.0.0.1:6379> getrange users:leto 50 56
" OVER 9"
127.0.0.1:6379> getrange users:leto 70 79
""
127.0.0.1:6379> incr stats:page:about
(integer) 1
127.0.0.1:6379> incr stats:page:about
(integer) 2
127.0.0.1:6379> incrby ratings:video:12333 5
(integer) 5
127.0.0.1:6379> incrby ratings:video:12333 3
(integer) 8
127.0.0.1:6379> incrby users:leto 23
(error) ERR value is not an integer or out of range
127.0.0.1:6379> hset users:goku powerlevel 9000
(integer) 1
127.0.0.1:6379> hget users:goku powerlevel
"9000"
127.0.0.1:6379> hmset users:goku race saiyan age 737
OK
127.0.0.1:6379> hmget users:goku race powerlevel
1) "saiyan"
2) "9000"
127.0.0.1:6379> hgetall users:goku
1) "powerlevel"
2) "9000"
3) "race"
4) "saiyan"
5) "age"
6) "737"
127.0.0.1:6379> hkeys users:goku
1) "powerlevel"
2) "race"
3) "age"
127.0.0.1:6379> hdel users:goku age
(integer) 1
127.0.0.1:6379> hkeys users:goku
1) "powerlevel"
2) "race"
127.0.0.1:6379> lpush newusers goku
(integer) 1
127.0.0.1:6379> lget newusers
(error) ERR unknown command `lget`, with args beginning with: `newusers`, 
127.0.0.1:6379> get newusers
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> llen newusers
(integer) 1
127.0.0.1:6379> lpop newusers
"goku"
127.0.0.1:6379> lpush newusers goku
(integer) 1
127.0.0.1:6379> lpush newusers gokur
(integer) 2
127.0.0.1:6379> lpush newusers gokur45
(integer) 3
127.0.0.1:6379> lpop newusers
"gokur45"
127.0.0.1:6379> lpop newusers
"gokur"
127.0.0.1:6379> lpop newusers
"goku"
127.0.0.1:6379> sadd friends:leto ghanima paul chani jessica
(integer) 4
127.0.0.1:6379> sadd friends:duncan paul jessica alia
(integer) 3
127.0.0.1:6379> sismember friends:leto jessica
(integer) 1
127.0.0.1:6379> sismember friends:leto alia
(integer) 0
127.0.0.1:6379> sinter friends:leto friends:duncan
1) "paul"
2) "jessica"
127.0.0.1:6379> sinterstore friends:leto_duncan friends:leto friends:duncan
(integer) 2
127.0.0.1:6379> sismember duncan paul
(integer) 0
127.0.0.1:6379> sismember leto_duncan paul
(integer) 0
127.0.0.1:6379> sinter friends:leto friends:duncan
1) "paul"
2) "jessica"
127.0.0.1:6379> sinterstore friends:leto_duncan friends:leto friends:duncan
(integer) 2
127.0.0.1:6379> sismember friends:leto_duncan paul
(integer) 1
127.0.0.1:6379> sismember friends:leto_duncan alais
(integer) 0
127.0.0.1:6379> zadd friends:duncan 70 ghanima 95 paul 95 chani 75 jessica 1 vladimir
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> zadd friends:duncan 70 ghanima 95 paul 95 chani 75 jessica 1 vladimir [NX|XX] [CH] [INCR] score member [score member ...]
root@default:/data# zadd friends duncan:70
bash: zadd: command not found
root@default:/data# redis-cli
127.0.0.1:6379> zadd friends duncan:70
(error) ERR wrong number of arguments for 'zadd' command
127.0.0.1:6379> zadd friends duncan:70 [NX|XX] [CH] [INCR] score member [score member ...]
root@default:/data# zadd friends:duncan 70 ghanima
bash: zadd: command not found
root@default:/data# redis-cli
127.0.0.1:6379> zadd friends:duncan 70 ghanima
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> ZADD anotherindex 0 ghanima
(integer) 1
127.0.0.1:6379> zadd friends:duncan 0 ghanima
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> zadd friendsd 0 ghanima
(integer) 1
127.0.0.1:6379> zadd friendsd 0 ghanima 8 dsfds
(integer) 1
127.0.0.1:6379> zadd friendsd 0 ghanima 8 dsfds 435435 gfhg
(integer) 1
127.0.0.1:6379> zadd friendsd 0 ghanima 8 dsfds 435435 gfhg 435345
(error) ERR syntax error
127.0.0.1:6379> zadd friendsd 0 ghanima 8 dsfds 435435 gfhg 4353
(error) ERR syntax error
127.0.0.1:6379> zadd friendsd 0 ghanima 8 dsfds 435435 gfhg 4353 sdfdfsdf
(integer) 1
127.0.0.1:6379> zcount friendsd 100 1000000
(integer) 2
127.0.0.1:6379> zrevrank friendsd ghanima
(integer) 3
127.0.0.1:6379> zrevrank friendsd gfhg
(integer) 0
127.0.0.1:6379> zrevrank friendsd sdfdfsdf
(integer) 1
127.0.0.1:6379> zrevrank friendsd dsfds
(integer) 2
127.0.0.1:6379> zadd friends:duncan 70 ghanima
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> zadd friends1:duncan 70 ghanima
(integer) 1
127.0.0.1:6379> zadd friends1:duncan 70 ghanima 95 paul 95 chani 75 jessica 1 vladimir
(integer) 4
127.0.0.1:6379> zcount friends1:duncan 90 100
(integer) 2
127.0.0.1:6379> zrevrank friends1:duncan chani
(integer) 1
127.0.0.1:6379> zrevrank friends1:duncan vladimir
(integer) 4
127.0.0.1:6379> set users:leto@dune.gov '{"id": 9001, "email": "leto@dune.gov", ...}'
OK
127.0.0.1:6379> set users:9001 '{"id": 9001, "email": "leto@dune.gov", ...}'
OK
127.0.0.1:6379> set users:9001 '{"id": 9001, "email": "leto@dune.gov", ...}'
OK
127.0.0.1:6379> hset users:lookup:email leto@dune.gov 9001
(integer) 1
127.0.0.1:6379> get users:9001
"{\"id\": 9001, \"email\": \"leto@dune.gov\", ...}"
127.0.0.1:6379> hset bugs:1233 1 '{"id":1, "account": 1233, "subject": "..."}'
(integer) 1
127.0.0.1:6379> hset bugs:1233 2 '{"id":2, "account": 1233, "subject": "..."}'
(integer) 1
127.0.0.1:6379> hkeys bugs:1233
1) "1"
2) "2"
127.0.0.1:6379> expire pages:about 30
(integer) 0
127.0.0.1:6379> get pages:about
(nil)
127.0.0.1:6379> expire pages:about 30
(integer) 0
127.0.0.1:6379> get pages:about
(nil)
127.0.0.1:6379> get pages
(nil)
127.0.0.1:6379> expire pages:about 30
(integer) 0
127.0.0.1:6379> get pages
(nil)
127.0.0.1:6379> ttl pages:about
(integer) -2
127.0.0.1:6379> get pages
(nil)
127.0.0.1:6379> expire pages:about 30
(integer) 0
127.0.0.1:6379> get pages
(nil)
127.0.0.1:6379> ttl pages:about
(integer) -2
127.0.0.1:6379> expire pages:about 30
(integer) 0
127.0.0.1:6379> ttl pages:about
(integer) -2
127.0.0.1:6379> expire pages:about 30
(integer) 0
127.0.0.1:6379> ttl pages:about
(integer) -2
127.0.0.1:6379> 
127.0.0.1:6379> persist pages:about
(integer) 0
127.0.0.1:6379> expire pages:about 30setex pages:about 30 '<h1>about us</h1>....' 
root@default:/data# setex pages:about 30 '<h1>about us</h1>....'
bash: setex: command not found
root@default:/data# redis-cli
127.0.0.1:6379> setex pages:about 30 '<h1>about us</h1>....'
OK
127.0.0.1:6379> get pages:about
"<h1>about us</h1>...."
127.0.0.1:6379> get pages:about
"<h1>about us</h1>...."
127.0.0.1:6379> ttl ages:about
(integer) -2
127.0.0.1:6379> rpush users:leto:guesses 5 9 10 2 4 10 19 2
(integer) 8
127.0.0.1:6379> sort users:leto:guesses
1) "2"
2) "2"
3) "4"
4) "5"
5) "9"
6) "10"
7) "10"
8) "19"
127.0.0.1:6379> sadd friends:ghanima leto paul chani jessica alia duncan
(integer) 6
127.0.0.1:6379> sort friends:ghanima limit 0 3 desc alpha
1) "paul"
2) "leto"
3) "jessica"
127.0.0.1:6379> sort friends:ghanima limit desc alpha
(error) ERR value is not an integer or out of range
127.0.0.1:6379> sort friends:ghanima limit 0 3 desc
(error) ERR One or more scores can't be converted into double
127.0.0.1:6379> sort friends:ghanima limit 0 3 desc alpha
1) "paul"
2) "leto"
3) "jessica"
127.0.0.1:6379> sort friends:ghanima limit 0 12 desc alpha
1) "paul"
2) "leto"
3) "jessica"
4) "duncan"
5) "chani"
6) "alia"
127.0.0.1:6379> sort friends:ghanima limit 0 12 asc alpha
1) "alia"
2) "chani"
3) "duncan"
4) "jessica"
5) "leto"
6) "paul"
127.0.0.1:6379> sadd watch:leto 12339 1382 338 9338
(integer) 4
127.0.0.1:6379> set severity:12339 3
OK
127.0.0.1:6379> set severity:1382 2
OK
127.0.0.1:6379> set severity:338 5
OK
127.0.0.1:6379> set severity:9338 4
OK
127.0.0.1:6379> sort watch:leto by severity:* desc
1) "338"
2) "9338"
3) "12339"
4) "1382"
127.0.0.1:6379> hset users:goku powerlevel 9000
(integer) 0
127.0.0.1:6379> hget users:goku powerlevel
"9000"
127.0.0.1:6379> hset users:goku powerlevel 9000 level 8999
(integer) 1
127.0.0.1:6379> hget users:goku powerlevel
"9000"
127.0.0.1:6379> hget users:goku level
"8999"
127.0.0.1:6379> hmget users:goku
(error) ERR wrong number of arguments for 'hmget' command
127.0.0.1:6379>  hmset users:goku race saiyan age 737
OK
127.0.0.1:6379> hmget users:goku
(error) ERR wrong number of arguments for 'hmget' command
127.0.0.1:6379> hmget users:goku race
1) "saiyan"
127.0.0.1:6379> hmget users:goku race age
1) "saiyan"
2) "737"
127.0.0.1:6379>  hmset users:goku race saiyan age 737
OK
127.0.0.1:6379> hmget users:goku race age
1) "saiyan"
2) "737"
127.0.0.1:6379> hmget users:goku race age [field ...]
root@default:/data# redis-cli
127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
(integer) 0
127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
(integer) 0
127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014227:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
(integer) 0
127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014226:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
(integer) 1
127.0.0.1:6379> ZADD anotherindex 0 '2GB:20181214:014225:{"location:"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"}'
(integer) 1
127.0.0.1:6379> ZRANGEBYLEX anotherindex [2GB:20181214:014200 [2GB:20181214:014250:\xff
 1) "2GB:20181214:014220:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
 2) "2GB:20181214:014221:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
 3) "2GB:20181214:014222:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
 4) "2GB:20181214:014222:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
 5) "2GB:20181214:014223:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
 6) "2GB:20181214:014224:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
 7) "2GB:20181214:014225:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
 8) "2GB:20181214:014225:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
 9) "2GB:20181214:014226:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
10) "2GB:20181214:014226:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
11) "2GB:20181214:014227"
12) "2GB:20181214:014227:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
13) "2GB:20181214:014227:{\"location:\"https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts\"}"
14) "2GB:20181214:014228:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
15) "2GB:20181214:014229:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
16) "2GB:20181214:014230:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
17) "2GB:20181214:014231:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
18) "2GB:20181214:014232:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
19) "2GB:20181214:014233:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
20) "2GB:20181214:014234:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
21) "2GB:20181214:014235:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
22) "2GB:20181214:014236:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
23) "2GB:20181214:014237:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
24) "2GB:20181214:014238:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"
25) "2GB:20181214:014239:https://console.cloud.google.com/storage/browser/_details/isentia-streams-prod/2gb/segment_20181214_014227_21335.ts"

127.0.0.1:6379> KEYS *
 1) "anotherindex1"
 2) "friends:duncan"
 3) "Maheshhhhh"
 4) "20181214"
 5) "bugs:1233"
 6) "foo"
 7) "users:leto:guesses"
 8) "watch:leto"
 9) "users:leto@dune.gov"
10) "stats:page:about"
11) "friends:leto_duncan"
12) "a"
13) "anotherindex"
14) "ratings:video:12333"
15) "users:lookup:email"
16) "users:leto2"
17) "friends:ghanima"
18) "2GB:20181214:014227"
19) "severity:338"
20) "users:leto1"
21) "severity:9338"
22) "anotherindex100"
23) "severity:1382"
24) "friends1:duncan"
25) "severity:12339"
26) "users:9001"
27) "users:goku"
28) "sdfdsfdsf"
29) "friendsd"
30) "users:leto"
31) "friends:leto"
127.0.0.1:6379> KEYS 20181214
1) "20181214"
127.0.0.1:6379> MEMORY USAGE 20181214
(integer) 28548637
127.0.0.1:6379> 
```


https://www.openmymind.net/redis.pdf
https://blog.getspool.com/2011/11/29/fast-easy-realtime-metrics-using-redis-bitmaps/