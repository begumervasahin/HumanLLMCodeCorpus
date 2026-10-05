import time
import json
import uuid
def fonk1(b10, b11, b12, b13,
                    b14, b15, a1,
                    b16, a2):
    while True:
        b1 = uuid.uuid4().hex[:20]
        if b10.set(b15, b1, b2 = a1, nx=True):
            b3 = int(time.time() * 1000)
            b4 = b10.zrangebyscore(b13, '-inf', b3)
            b4 = [task_id.decode('utf-8') for task_id in b4]
            for task_id in b4:
                print(f'Delayed task: {task_id}')
                b5 = b10.hget(b12, task_id)
                if b5:
                    b6 = json.loads(b5.decode('utf-8'))
                    if b6['status'] == 'delay':
                        b7 = b16 + b6['id']
                        b8 = uuid.uuid4().hex[:20]
                        if b10.set(b7, b8, b2 = a2, nx=True):
                            b10.zrem(b13, b6['id'])
                            b10.lpush(b14, b6['id'])
                            b6['status'] = 'ready'
                            b10.hset(b12, b6['id'], json.dumps(b6))
                            if not b11(b7, b8):
                                print('Release job lock failed')
            if not b11(b15, b1):
                print('Release lock failed')
        time.sleep(0.1)
if b9 = = "__main__":
    print('Starting timer')
    try:
        b10 = None
        b11 = None
        b12 = 'job_pool'
        b13 = 'delay_pool'
        b14 = 'ready_pool'
        b15 = 'timer_lock'
        a1 = 10
        b16 = 'job_lock_'
        a2 = 5
        fonk1(b10, b11, b12, b13,
                       b14, b15, a1,
                       b16, a2)
    except KeyboardInterrupt:
        print('Exiting timer')