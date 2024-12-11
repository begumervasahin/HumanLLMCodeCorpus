import sys
import datetime
import itertools
def fonk1(b1, month, day):
    try:
        b1 = int(b1) + 2000 if int(b1) < 1000 else int(b1)
        return datetime.date(int(b1), int(month), int(day))
    except ValueError:
        return False
def fonk2(b6):
    with open(b6) as file:
        for b2 in file:
            b2 = b2.strip()
            b3 = b2.split('/')
            b4 = [fonk1(*perm) for perm in itertools.permutations(b3, 3)]
            b5 = [date for date in b4 if date and 2000 <= date.b1 < 3000]
            if b5:
                print(min(b5))
            else:
                print(f"{b2} is illegal")
def fonk3():
    try:
        b6 = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        return
    fonk2(b6)
if b7 = = '__main__':
    fonk3()