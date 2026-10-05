import sys
from datetime import date
from math import sqrt
from functools import reduce
from itertools import count, islice
def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))
def is_day_prime(day):
    return is_prime(int(str(day).replace('-', '')))
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
def get_prime_days(my_date=date.today()):
    day = my_date.day
    month = my_date.month
    year = my_date.year
    while True:
        if is_day_prime(my_date):
            yield my_date
        try:
            day += 1
            my_date = date(year, month, day)
        except ValueError:
            try:
                day = 1
                month += 1
                my_date = date(year, month, day)
            except ValueError:
                month = 1
                year += 1
                my_date = date(year, month, day)
                if year > 9999:
                    print('Exceeded year 9999')
                    break
def get_prime_birthdays(year, month, day):
    start_year = date.today().year
    while True:
        try:
            birthday = date(start_year, month, day)
            if is_day_prime(birthday):
                yield 'Your {} birthday is a prime year!'.format(start_year - year)
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