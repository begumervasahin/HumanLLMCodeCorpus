import sys
import datetime
import itertools
def parse_date(year, month, day):
    try:
        year = int(year) + 2000 if int(year) < 1000 else int(year)
        return datetime.date(year, int(month), int(day))
    except ValueError:
        return False
def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        sys.exit(1)
    try:
        with open(filename) as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)
    for line in lines:
        parts = line.split('/')
        dates = []
        for year, month, day in itertools.permutations(parts, 3):
            date = parse_date(year, month, day)
            if date and 2000 <= date.year < 3000:
                dates.append(date)
        if dates:
            print(min(dates))
        else:
            print(f"{line} is illegal")
if __name__ == '__main__':
    main()