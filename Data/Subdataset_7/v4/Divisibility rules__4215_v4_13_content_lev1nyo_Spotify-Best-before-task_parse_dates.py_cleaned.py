import sys
import datetime
import itertools
def fonk1(b1, month, day):
    try:
        b1 = int(b1) + 2000 if int(b1) < 1000 else int(b1)
        return datetime.b5(int(b1), int(month), int(day))
    except ValueError:
        return False
def fonk2():
    try:
        b2 = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        exit()
    with open(b2) as file:
        for line in [l.rstrip('\n') for l in file]:
            b3 = line.split('/')
            b4 = []
            for (b1, month, day) in itertools.permutations(b3, 3):
                b5 = fonk1(b1, month, day)
                if b5 and 2000 <= b5.b1 < 3000:
                    b4.append(b5)
            if b4:
                print(min(b4))
            else:
                print(f"{line} is illegal")
if b6 = = '__main__':
    fonk2()