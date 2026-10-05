import time
import json
import uuid
def timer_function():
    while True:
        lock_value = uuid.uuid4().hex[:20]
        if redis_client.set(TIMER_LOCK_KEY, lock_value, ex=TIMER_LOCK_EXP_TIME, nx=True):
            current_time_ms = int(time.time() * 1000)
            task_id_list = redis_client.zrangebyscore(DELAY_POOL_KEY, '-inf', current_time_ms)
            task_id_list = [task_id.decode('utf-8') for task_id in task_id_list]
            for task_id in task_id_list:
                print(f'Delayed task: {task_id}')
                task_dict_raw = redis_client.hget(JOB_POOL_KEY, task_id)
                if task_dict_raw:
                    task_dict = json.loads(task_dict_raw.decode('utf-8'))
                    if task_dict['status'] == 'delay':
                        job_lock_key = JOB_LOCK_KEY_PREFIX + task_dict['id']
                        job_lock_value = uuid.uuid4().hex[:20]
                        if redis_client.set(job_lock_key, job_lock_value, ex=JOB_LOCK_EXP_TIME, nx=True):
                            redis_client.zrem(DELAY_POOL_KEY, task_dict['id'])
                            redis_client.lpush(READY_POOL_KEY, task_dict['id'])
                            task_dict['status'] = 'ready'
                            redis_client.hset(JOB_POOL_KEY, task_dict['id'], json.dumps(task_dict))
                            if not release_redis_lock(job_lock_key, job_lock_value):
                                print('Release job lock failed')
            if not release_redis_lock(TIMER_LOCK_KEY, lock_value):
                print('Release lock failed')
        time.sleep(0.1)
if __name__ == "__main__":
    print('Starting timer')
    try:
        timer_function()
    except KeyboardInterrupt:
        print('Exiting timer')