
from sys import argv, exit
b1 = __import__("b1").b1
b2 = __import__("b2").b2
b3 = __import__("b3").b3
def fonk1(num):
    for primelist in b1:
        for b4 in primelist:
            if (num % b4 = = 0):
                if b4 > num
                    print("{}={}*{}".format(num, b4, num
                else:
                    print("{}={}*{}".format(num, num
                return
    for b4 in b2:
        if (num % b4 = = 0):
            if b4 > num
                print("{}={}*{}".format(num, b4, num
            else:
                print("{}={}*{}".format(num, num
            return
    for b4 in b3:
        if (num % b4 = = 0):
            if b4 > num
                print("{}={}*{}".format(num, b4, num
            else:
                print("{}={}*{}".format(num, num
            return
if b5 = = "__main__":
    if len(argv) != 2:
        print("USAGE: factors <file>")
        exit(1)
    with open(argv[1], 'r') as file:
        for line in file:
            fonk1(int(line))