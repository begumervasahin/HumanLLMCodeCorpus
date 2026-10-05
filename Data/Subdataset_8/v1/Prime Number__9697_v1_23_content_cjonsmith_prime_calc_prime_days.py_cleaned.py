import os
import sys
import datetime
from prime import is_day_prime
def increment_day(date):
    year, month, day = (date.year, date.month, date.day)
    try:
        day += 1
        return datetime.date(year, month, day)
    except ValueError:
        try:
            month += 1
            day = 1
            return datetime.date(year, month, day)
        except ValueError:
            try:
                year += 1
                month = 1
                day = 1
                return datetime.date(year, month, day)
            except ValueError:
                raise
def num_prime_days(date, num_years):
    num_days = 0
    count = 0
    while count < num_years:
        if is_day_prime(date):
            num_days += 1
        try:
            date = datetime.date(date.year + 1, date.month, date.day)
        except ValueError:
            if date.year % 4 == 0:
                if (date.year + 4) % 100 == 0 and (date.year + 4) % 400 != 0:
                    date = datetime.date(date.year + 8, date.month, date.day)
                    count += 7
                else:
                    date = datetime.date(date.year + 4, date.month, date.day)
                    count += 3
        count += 1
    write_file(date, num_days)
def write_file(date, num_days):
    month = '{0:02d}'.format(date.month)
    day = '{0:02d}'.format(date.day)
    with open(file_name, 'a+') as out_file:
        out_file.write('{}-{},{}\n'.format(month, day, num_days))
if __name__ == '__main__':
    file_name = 'all-days.csv'
    if os.path.exists(file_name):
        os.remove(file_name)
    year, month, day = [int(x) for x in sys.argv[1:4]]
    num_years = int(sys.argv[4])
    date = datetime.date(year, month, day)
    while date.year == year:
        sys.stdout.write('\rCurrent Date: {}'.format(date))
        sys.stdout.flush()
        num_prime_days(date, num_years)
        if date.month == 2 and date.day == 27 and year % 4 != 0:
            tmp_year = year + 4 - (year % 4)
            date = datetime.date(tmp_year, 2, 29)
            sys.stdout.write('\rCurrent Date: {}'.format(date))
            sys.stdout.flush()
            num_prime_days(date, num_years)
            date = datetime.date(year, 2, 28)
        date = increment_day(date)
        while date.day % 2 == 0 or date.day % 5 == 0:
            date = increment_day(date)
    print()