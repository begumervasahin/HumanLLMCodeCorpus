import random
import time
from datetime import timedelta, datetime
def generate_random_date(start_date, end_date):
    start_time = time.mktime(time.strptime(start_date, '%Y-%m-%d'))
    end_time = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
    random_time = start_time + random.random() * (end_time - start_time)
    return time.strftime('%Y-%m-%d', time.localtime(random_time))
def generate_random_hot_date():
    return generate_random_date("2018-01-01", "2018-06-30")
def generate_random_cold_date():
    return generate_random_date("2018-07-01", "2018-12-31")
def generate_random_date_period(start_date, days):
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = start_date + timedelta(days=days)
    return generate_random_date(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
