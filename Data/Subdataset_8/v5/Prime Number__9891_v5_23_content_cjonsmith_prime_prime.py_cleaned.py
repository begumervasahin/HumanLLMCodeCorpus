import sys
from datetime import date
from math import sqrt
from itertools import count
def is_prime(num):
    return num > 1 and all(num % i for i in range(2, int(sqrt(num)) + 1))
def is_prime_day(day):
    numerical_day = int(day.strftime('%Y%m%d'))
    return is_prime(numerical_day)
def prime_factors(num):
    factors = set()
    for i in range(2, int(sqrt(num)) + 1):
        while num % i == 0:
            factors.add(i)
            num
    if num > 1:
        factors.add(num)
    return factors
def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
def generate_prime_days(start_date=date.today()):
    while True:
        if is_prime_day(start_date):
            yield start_date
        start_date = start_date.replace(day=start_date.day + 1)
        if start_date.month == 1 and start_date.day == 1:
            start_date = start_date.replace(year=start_date.year + 1)
def generate_prime_birthdays(year, month, day):
    current_year = date.today().year
    while True:
        try:
            birthday = date(current_year, month, day)
            if is_prime_day(birthday):
                yield f'Your {current_year - year} birthday is a prime year!'
            current_year += 1
        except ValueError:
            print('Year cannot exceed 9999')
            break
if __name__ == '__main__':
    num_days = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    prime_day_generator = generate_prime_days()
    for _ in range(num_days):
        print(next(prime_day_generator))