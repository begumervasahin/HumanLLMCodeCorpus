import sys
import math
from datetime import date, timedelta
from functools import reduce
from itertools import count, islice
def is_prime(num):
    if num <= 1:
        return False
    for i in islice(count(2), int(math.sqrt(num) - 1)):
        if num % i == 0:
            return False
    return True
def is_day_prime(day):
    return is_prime(int(day.strftime("%Y%m%d")))
def prime_factors(num):
    if is_prime(num):
        return (num,)
    factors = ()
    for val in range(2, num
        if num % val == 0:
            result = num
            if val not in factors and is_prime(val):
                factors += (val,)
            else:
                factors += prime_factors(val)
            if result not in factors and is_prime(result):
                factors += (result,)
            else:
                factors += prime_factors(result)
            if reduce(lambda x, y: x * y, factors) == num:
                break
    return factors
def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
def prime_day_generator(start_date=date.today()):
    while True:
        if is_day_prime(start_date):
            yield start_date
        start_date += timedelta(days=1)
def prime_birthday_generator(year, month, day):
    start_year = date.today().year
    while True:
        try:
            birthday = date(start_year, month, day)
            if is_day_prime(birthday):
                yield f'Your {start_year - year} birthday is a prime year!'
            start_year += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if __name__ == '__main__':
    num_next_prime_days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for i, prime_day in enumerate(prime_day_generator()):
        if i >= num_next_prime_days:
            break
        print(prime_day)