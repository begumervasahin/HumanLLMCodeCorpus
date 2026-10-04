import sys
import datetime
import itertools
def fonk1(b1, month, day):
    try:
        b1 = int(b1) + 2000 if int(b1) < 1000 else int(b1)
        return datetime.b5(b1, int(month), int(day))
    except ValueError:
        return False
def fonk2(b6):
    try:
        with open(b6) as file:
            b2 = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {b6}")
        sys.exit(1)
    for line in b2:
        b3 = line.split('/')
        b4 = []
        for b1, month, day in itertools.permutations(b3, 3):
            b5 = fonk1(b1, month, day)
            if b5 and 2000 <= b5.b1 < 3000:
                b4.append(b5)
        if b4:
            print(min(b4))
        else:
            print(f"{line} is illegal")
def fonk3():
    if len(sys.argv) < 2:
        print("Missing file name!")
        sys.exit(1)
    b6 = sys.argv[1]
    fonk2(b6)
if b7 = = '__main__':
    fonk3()