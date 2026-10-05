import sys
from datetime import date
from math import sqrt
from itertools import count, islice
def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))
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
            if result * val == num:
                break
    return factors
def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
def get_prime_days(start_date=date.today()):
    current_date = start_date
    while True:
        if is_day_prime(current_date):
            yield current_date
        current_date = current_date.replace(day=current_date.day + 1)
        if current_date.day == 1:
            current_date = current_date.replace(month=current_date.month + 1)
            if current_date.month == 1:
                current_date = current_date.replace(year=current_date.year + 1)
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
    prime_days_generator = get_prime_days()
    prime_days = islice(prime_days_generator, num_prime_days)
    for prime_day in prime_days:
        print(prime_day)