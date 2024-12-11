import sys
import datetime
import itertools
def fonk1(b1, month, day):
    try:
        b1 = int(b1) + 2000 if int(b1) < 1000 else int(b1)
        return datetime.b6(int(b1), int(month), int(day))
    except ValueError:
        return False
def fonk2():
    try:
        b2 = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        return
    with open(b2) as f:
        for b3 in f:
            b3 = b3.rstrip('\n')
            b4 = b3.split('/')
            b5 = []
            for (b1, month, day) in itertools.permutations(b4, 3):
                b6 = fonk1(b1, month, day)
                if b6 and 2000 <= b6.b1 < 3000:
                    b5.append(b6)
            if b5:
                print(min(b5))
            else:
                print(f"{b3} is illegal")
if b7 = = '__main__':
    fonk2()