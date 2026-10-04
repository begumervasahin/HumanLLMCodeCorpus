
import os
import sys
import datetime
from prime import is_day_prime
def increment_day(date):
    year, month, day = date.year, date.month, date.day
    try:
        return datetime.date(year, month, day + 1)
    except ValueError:
        try:
            return datetime.date(year, month + 1, 1)
        except ValueError:
            return datetime.date(year + 1, 1, 1)
def num_prime_days(start_date, num_years):
    num_days = 0
    count = 0
    start_year = start_date.year
    while count < num_years:
        if is_day_prime(start_date):
            num_days += 1
        try:
            start_date = datetime.date(start_year + count + 1, start_date.month, start_date.day)
        except ValueError:
            if (start_year + count) % 4 == 0:
                if (start_year + count + 4) % 100 == 0 and (start_year + count + 4) % 400 != 0:
                    start_date = datetime.date(start_year + count + 8, start_date.month, start_date.day)
                    count += 7
                else:
                    start_date = datetime.date(start_year + count + 4, start_date.month, start_date.day)
                    count += 3
        count += 1
    write_file(start_date, num_days)
def write_file(date, num_days):
    with open(file_name, 'a+') as out_file:
        out_file.write(f'{date.month:02d}-{date.day:02d},{num_days}\n')
if __name__ == '__main__':
    file_name = 'all-days.csv'
    if os.path.exists(file_name):
        os.remove(file_name)
    year, month, day = map(int, sys.argv[1:4])
    num_years = int(sys.argv[4])
    start_date = datetime.date(year, month, day)
    while start_date.year == year:
        sys.stdout.write(f'\rCurrent Date: {start_date}')
        sys.stdout.flush()
        num_prime_days(start_date, num_years)
        if start_date.month == 2 and start_date.day == 27 and year % 4 != 0:
            tmp_year = year + 4 - (year % 4)
            leap_date = datetime.date(tmp_year, 2, 29)
            sys.stdout.write(f'\rCurrent Date: {leap_date}')
            sys.stdout.flush()
            num_prime_days(leap_date, num_years)
            start_date = datetime.date(year, 2, 28)
        start_date = increment_day(start_date)
        while start_date.day % 2 == 0 or start_date.day % 5 == 0:
            start_date = increment_day(start_date)
    print()