import redis

# producing queue
with redis.Redis(host='192.168.42.80', port='6379', db=0) as rc:
    for i in range(6):
        rc.lpush('queue', i)

    print(rc.get('queue'))
