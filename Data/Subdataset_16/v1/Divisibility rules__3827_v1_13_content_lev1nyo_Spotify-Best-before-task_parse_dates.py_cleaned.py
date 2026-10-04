import sys
import datetime
import itertools
def fonk1(b1, month, day):
    try:
        b1 = int(b1) + 2000 if int(b1) < 1000 else int(b1)
        return datetime.b6(b1, int(month), int(day))
    except ValueError:
        return False
def fonk2():
    try:
        b2 = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        sys.exit(1)
    try:
        with open(b2) as f:
            b3 = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"File not found: {b2}")
        sys.exit(1)
    for line in b3:
        b4 = line.split('/')
        b5 = []
        for b1, month, day in itertools.permutations(b4, 3):
            b6 = fonk1(b1, month, day)
            if b6 and 2000 <= b6.b1 < 3000:
                b5.append(b6)
        if b5:
            print(min(b5))
        else:
            print(f"{line} is illegal")
if b7 = = '__main__':
    fonk2()