
import os
import sys
import datetime
from prime import is_day_prime
def increment_day(date):
    try:
        return date + datetime.timedelta(days=1)
    except ValueError:
        raise
def num_prime_days(start_date, num_years):
    num_days = 0
    current_date = start_date
    for _ in range(num_years):
        if is_day_prime(current_date):
            num_days += 1
        try:
            current_date = datetime.date(current_date.year + 1, current_date.month, current_date.day)
        except ValueError:
            if is_leap_year(current_date.year):
                current_date = datetime.date(current_date.year + 4, current_date.month, current_date.day)
            else:
                current_date = datetime.date(current_date.year + 1, current_date.month, current_date.day)
    write_file(start_date, num_days)
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def write_file(date, num_days):
    month = f'{date.month:02d}'
    day = f'{date.day:02d}'
    with open(file_name, 'a') as out_file:
        out_file.write(f'{month}-{day},{num_days}\n')
if __name__ == '__main__':
    file_name = 'all-days.csv'
    if os.path.exists(file_name):
        os.remove(file_name)
    year, month, day, num_years = map(int, sys.argv[1:5])
    start_date = datetime.date(year, month, day)
    while start_date.year == year:
        print(f'\rCurrent Date: {start_date}', end='')
        num_prime_days(start_date, num_years)
        if start_date.month == 2 and start_date.day == 27 and not is_leap_year(year):
            leap_year = year + (4 - year % 4)
            start_date = datetime.date(leap_year, 2, 29)
            print(f'\rCurrent Date: {start_date}', end='')
            num_prime_days(start_date, num_years)
            start_date = datetime.date(year, 2, 28)
        start_date = increment_day(start_date)
        while start_date.day % 2 == 0 or start_date.day % 5 == 0:
            start_date = increment_day(start_date)
    print()