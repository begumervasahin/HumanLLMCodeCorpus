import sys
import datetime
import itertools
def parse_date(year, month, day):
    try:
        year = int(year) + 2000 if int(year) < 1000 else int(year)
        return datetime.date(year, int(month), int(day))
    except ValueError:
        return False
def process_line(line):
    parts = line.split('/')
    dates = []
    for year, month, day in itertools.permutations(parts, 3):
        date = parse_date(year, month, day)
        if date and 2000 <= date.year < 3000:
            dates.append(date)
    if dates:
        return str(min(dates))
    else:
        return f"{line} is illegal"
def process_file(filename):
    try:
        with open(filename) as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)
    for line in lines:
        result = process_line(line)
        print(result)
def main():
    if len(sys.argv) < 2:
        print("Missing file name!")
        sys.exit(1)
    filename = sys.argv[1]
    process_file(filename)
if __name__ == '__main__':
    main()