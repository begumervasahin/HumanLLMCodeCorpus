import time
import json
import uuid
from delay_queue.utils import redis_client, release_redis_lock
from delay_queue.config import (
    JOB_POOL_KEY,
    DELAY_POOL_KEY,
    READY_POOL_KEY,
    TIMER_LOCK_KEY,
    TIMER_LOCK_EXP_TIME,
    JOB_LOCK_KEY_PREFIX,
    JOB_LOCK_EXP_TIME,
)
def timer_func():
    while True:
        lock_value = uuid.uuid4().hex[:20]
        if redis_client.set(TIMER_LOCK_KEY, lock_value, ex=TIMER_LOCK_EXP_TIME, nx=True):
            current_time_ms = int(time.time() * 1000)
            task_id_list = redis_client.zrangebyscore(DELAY_POOL_KEY, '-inf', current_time_ms)
            task_id_list = [task_id.decode('utf-8') for task_id in task_id_list]
            for task_id in task_id_list:
                print(f'Delayed task: {task_id}')
                task_data_raw = redis_client.hget(JOB_POOL_KEY, task_id)
                if task_data_raw:
                    task_data = json.loads(task_data_raw.decode('utf-8'))
                    if task_data['status'] == 'delay':
                        job_lock_key = JOB_LOCK_KEY_PREFIX + task_data['id']
                        job_lock_value = uuid.uuid4().hex[:20]
                        if redis_client.set(job_lock_key, job_lock_value, ex=JOB_LOCK_EXP_TIME, nx=True):
                            process_task(task_data, job_lock_key, job_lock_value)
            release_timer_lock(lock_value)
        time.sleep(0.1)
def process_task(task_data, job_lock_key, job_lock_value):
    redis_client.zrem(DELAY_POOL_KEY, task_data['id'])
    redis_client.lpush(READY_POOL_KEY, task_data['id'])
    task_data['status'] = 'ready'
    redis_client.hset(JOB_POOL_KEY, task_data['id'], json.dumps(task_data))
    if not release_redis_lock(job_lock_key, job_lock_value):
        print(f'Failed to release job lock: {job_lock_key}')
def release_timer_lock(lock_value):
    if not release_redis_lock(TIMER_LOCK_KEY, lock_value):
        print(f'Failed to release timer lock: {TIMER_LOCK_KEY}')
if __name__ == "__main__":
    print('Starting timer...')
    try:
        timer_func()
    except KeyboardInterrupt:
        print('Exiting timer...')
        exit(0)