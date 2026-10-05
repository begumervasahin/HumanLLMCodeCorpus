import sys
import datetime
import itertools
def parse_date(year, month, day):
    try:
        year = int(year) + 2000 if int(year) < 1000 else int(year)
        return datetime.date(int(year), int(month), int(day))
    except ValueError:
        return False
def process_file(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split('/')
            dates = [parse_date(*perm) for perm in itertools.permutations(parts, 3)]
            valid_dates = [date for date in dates if date and 2000 <= date.year < 3000]
            if valid_dates:
                print(min(valid_dates))
            else:
                print(f"{line} is illegal")
def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        return
    process_file(filename)
if __name__ == '__main__':
    main()