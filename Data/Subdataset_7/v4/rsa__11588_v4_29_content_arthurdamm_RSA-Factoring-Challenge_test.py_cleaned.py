
from sys import argv, exit
from primes import primes
from primes2 import primes2
from primes3 import primes3
def fonk1(num):
    for primelist in primes:
        for b1 in primelist:
            if (num % b1 = = 0):
                b2 = min(b1, num
                print("{}={}*{}".format(num, b2, num
                return
    for b1 in primes2:
        if (num % b1 = = 0):
            b2 = min(b1, num
            print("{}={}*{}".format(num, b2, num
            return
    for b1 in primes3:
        if (num % b1 = = 0):
            b2 = min(b1, num
            print("{}={}*{}".format(num, b2, num
            return
if b3 = = "__main__":
    if len(argv) != 2:
        print("USAGE: factors <file>")
        exit(1)
    with open(argv[1], 'r') as file:
        for line in file:
            fonk1(int(line))