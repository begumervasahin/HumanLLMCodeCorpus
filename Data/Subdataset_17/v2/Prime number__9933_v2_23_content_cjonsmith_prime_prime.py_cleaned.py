import sys
import math
from datetime import date
from functools import reduce
from math import sqrt
from itertools import count, islice
def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)) + 1))
def is_day_prime(day):
    return is_prime(int(day.strftime('%Y%m%d')))
def prime_factors(num):
    factors = ()
    if is_prime(num):
        return (num,)
    mid = num
    for val in range(2, mid + 1):
        if num % val == 0:
            result = num
            if result in factors or val in factors:
                continue
            if is_prime(val):
                factors += (val,)
            else:
                factors += prime_factors(val)
            if is_prime(result):
                factors += (result,)
            else:
                factors += prime_factors(result)
            if reduce(lambda x, y: x * y, factors) == num:
                break
    return factors
def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
def get_prime_days(start_date=date.today()):
    while True:
        if is_day_prime(start_date):
            yield start_date
        try:
            start_date = start_date.replace(day=start_date.day + 1)
        except ValueError:
            try:
                start_date = start_date.replace(month=start_date.month + 1, day=1)
            except ValueError:
                start_date = start_date.replace(year=start_date.year + 1, month=1, day=1)
def get_prime_birthdays(year, month, day):
    start_year = date.today().year
    while True:
        try:
            birthday = date(start_year, month, day)
            if is_day_prime(birthday):
                yield f'Your {start_year - year}th birthday is a prime year!'
            start_year += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if __name__ == '__main__':
    start = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    for i, prime_day in enumerate(get_prime_days()):
        if i >= start:
            break
        print(prime_day)