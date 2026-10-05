import sys
import datetime
import itertools
def parse_date(year, month, day):
    try:
        year = int(year) + 2000 if int(year) < 1000 else int(year)
        return datetime.date(int(year), int(month), int(day))
    except ValueError:
        return False
def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        return
    with open(filename) as file:
        for line in map(str.strip, file):
            parts = line.split('/')
            valid_dates = []
            for perm in itertools.permutations(parts, 3):
                date = parse_date(*perm)
                if date and 2000 <= date.year < 3000:
                    valid_dates.append(date)
            if valid_dates:
                print(min(valid_dates))
            else:
                print(f"{line} is illegal")
if __name__ == '__main__':
    main()