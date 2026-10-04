import time
import json
import uuid
from delay_queue.utils import redis_client, release_redis_lock
from delay_queue.config import JOB_POOL_KEY, DELAY_POOL_KEY, \
    READY_POOL_KEY, TIMER_LOCK_KEY, TIMER_LOCK_EXP_TIME, JOB_LOCK_KEY_PREFIX, JOB_LOCK_EXP_TIME
def fonk1():
    while True:
        b1 = uuid.uuid4().hex[:20]
        if redis_client.set(TIMER_LOCK_KEY, b1, b2 = TIMER_LOCK_EXP_TIME, nx=True):
            b3 = int(time.time() * 1000)
            b4 = redis_client.zrangebyscore(DELAY_POOL_KEY, '-inf', b3)
            b4 = [i.decode('utf-8') for i in b4]
            for task_id in b4:
                print(f'delay task: {task_id}')
                b5 = redis_client.hget(JOB_POOL_KEY, task_id)
                if b5:
                    b6 = json.loads(b5.decode('utf-8'))
                    if b6['status'] == 'delay':
                        b7 = JOB_LOCK_KEY_PREFIX + b6['id']
                        b8 = uuid.uuid4().hex[:20]
                        if redis_client.set(b7, b8, b2 = JOB_LOCK_EXP_TIME, nx=True):
                            redis_client.zrem(DELAY_POOL_KEY, b6['id'])
                            redis_client.lpush(READY_POOL_KEY, b6['id'])
                            b6['status'] = 'ready'
                            redis_client.hset(JOB_POOL_KEY, b6['id'], json.dumps(b6))
                            if not release_redis_lock(b7, b8):
                                print('release job lock fail')
            if not release_redis_lock(TIMER_LOCK_KEY, b1):
                print('release lock fail')
        time.sleep(0.1)
if b9 = = "__main__":
    print('start timer')
    try:
        fonk1()
    except KeyboardInterrupt:
        print('exit timer')
        exit(0)