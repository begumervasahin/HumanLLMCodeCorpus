import random
import time
from datetime import timedelta, datetime
def generate_random_date_in_range(start_date, end_date, proportion):
    start_time = time.mktime(time.strptime(start_date, '%Y-%m-%d'))
    end_time = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
    random_time = start_time + proportion * (end_time - start_time)
    return time.strftime('%Y-%m-%d', time.localtime(random_time))
def generate_random_hot_date():
    return generate_random_date_in_range("2018-01-01", "2018-06-30", random.random())
def generate_random_cold_date():
    return generate_random_date_in_range("2018-07-01", "2018-12-31", random.random())
def generate_random_date_within_delta(start_date, delta_days):
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = str(start_date_obj + timedelta(days=delta_days))
    return generate_random_date_in_range(start_date, end_date, random.random())
print("Random hot date:", generate_random_hot_date())
print("Random cold date:", generate_random_cold_date())
print("Random date with custom range and delta:", generate_random_date_within_delta("2023-01-01", 365))