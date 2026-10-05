import os
import sys
import datetime
from prime import is_day_prime
def increment_day(date):
    return date + datetime.timedelta(days=1)
def num_prime_days(date, num_years):
    num_days = 0
    for _ in range(num_years):
        if is_day_prime(date):
            num_days += 1
        try:
            date = date.replace(year=date.year + 1)
        except ValueError:
            if date.year % 4 == 0 and (date.year % 100 != 0 or date.year % 400 == 0):
                date = date.replace(year=date.year + 4)
            else:
                date = date.replace(year=date.year + 1)
    write_file(date, num_days)
def write_file(date, num_days):
    month = date.strftime('%m')
    day = date.strftime('%d')
    with open('all-days.csv', 'a+') as out_file:
        out_file.write(f'{month}-{day},{num_days}\n')
if __name__ == '__main__':
    file_name = 'all-days.csv'
    if os.path.exists(file_name):
        os.remove(file_name)
    year, month, day = map(int, sys.argv[1:4])
    num_years = int(sys.argv[4])
    date = datetime.date(year, month, day)
    while date.year == year:
        print(f'Current Date: {date}', end='\r')
        num_prime_days(date, num_years)
        if date.month == 2 and date.day == 27 and year % 4 != 0:
            tmp_year = year + 4 - (year % 4)
            date = datetime.date(tmp_year, 2, 29)
            print(f'Current Date: {date}', end='\r')
            num_prime_days(date, num_years)
            date = datetime.date(year, 2, 28)
        date = increment_day(date)
        while date.day % 2 == 0 or date.day % 5 == 0:
            date = increment_day(date)
    print()
