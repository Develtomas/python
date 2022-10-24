import time
import redis

with redis.Redis(host='192.168.42.80', port='6379', db=0) as rc:
    rc.set('counter', 1)

    print('-----------------autocounter---------------')
    while True:
        rc.incr('counter')
        time.sleep(1)
        if int(rc.get('counter')) > 60:
            # decrease via incrby
            rc.incrby('counter', -5)
            print('end iteration')
            break

    # find keys with mask
    print(rc.keys('*oun*'))

    # get k,v from generator
    for i in rc.scan_iter('*'):
        print(i, rc.get(i))

    print('-----------------list append---------------')
    # create list
    for i in range(3000):
        rc.lpush('list1', i)
    # show
    rc.lrange('list1', 1, 3000)
    # list length
    rc.llen('list1')
    # find with index
    rc.lindex('list1', 23)
    # insert
    rc.linsert('list1', 'BEFORE', 3, 'hi')

