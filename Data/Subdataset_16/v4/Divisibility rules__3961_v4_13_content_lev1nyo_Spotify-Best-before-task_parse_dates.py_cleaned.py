import sys
import datetime
import itertools
def fonk1(b1, month, day):
    try:
        b1 = int(b1) + 2000 if int(b1) < 1000 else int(b1)
        return datetime.b4(b1, int(month), int(day))
    except ValueError:
        return False
def fonk2(line):
    b2 = line.split('/')
    b3 = []
    for b1, month, day in itertools.permutations(b2, 3):
        b4 = fonk1(b1, month, day)
        if b4 and 2000 <= b4.b1 < 3000:
            b3.append(b4)
    if b3:
        return str(min(b3))
    else:
        return f"{line} is illegal"
def fonk3():
    if len(sys.argv) < 2:
        print("Missing file name!")
        sys.exit(1)
    b5 = sys.argv[1]
    try:
        with open(b5) as file:
            b6 = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {b5}")
        sys.exit(1)
    for line in b6:
        b7 = fonk2(line)
        print(b7)
if b8 = = '__main__':
    fonk3()