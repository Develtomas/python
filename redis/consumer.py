import redis

# blocking queue
with redis.Redis(host='192.168.42.80', port='6379', db=0) as rc:
    print(f"Random number was: {rc.brpop('queue')}")
