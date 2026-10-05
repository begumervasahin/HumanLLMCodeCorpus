import sys
from datetime import date
from math import sqrt
from itertools import count, islice
def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))
def is_day_prime(day):
    return is_prime(int(day.strftime('%Y%m%d')))
def prime_factors(num):
    factors = ()
    if is_prime(num):
        return (num,)
    for val in range(2, num
        if num % val == 0:
            result = num
            if result in factors or val in factors:
                continue
            factors += prime_factors(val) if not is_prime(val) else (val,)
            factors += prime_factors(result) if not is_prime(result) else (result,)
            if reduce(lambda x, y: x * y, factors) == num:
                break
    return factors
def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
def get_prime_days(my_date=date.today()):
    while True:
        if is_day_prime(my_date):
            yield my_date
        my_date = my_date.replace(day=my_date.day + 1)
        if my_date.day == 1:
            my_date = my_date.replace(month=my_date.month + 1)
            if my_date.month == 1:
                my_date = my_date.replace(year=my_date.year + 1)
def get_prime_birthdays(year, month, day):
    start_year = date.today().year
    while True:
        try:
            birthday = date(start_year, month, day)
            if is_day_prime(birthday):
                yield 'Your {} birthday is a prime day!'.format(start_year - year)
            start_year += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if __name__ == '__main__':
    num_prime_days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for prime_day in islice(get_prime_days(), num_prime_days):
        print(prime_day)