
from sys import argv, exit
from primes import primes
from primes2 import primes2
from primes3 import primes3
def factorize(num):
    for primelist in primes:
        for p in primelist:
            if (num % p == 0):
                smaller_divisor = min(p, num
                print("{}={}*{}".format(num, smaller_divisor, num
                return
    for p in primes2:
        if (num % p == 0):
            smaller_divisor = min(p, num
            print("{}={}*{}".format(num, smaller_divisor, num
            return
    for p in primes3:
        if (num % p == 0):
            smaller_divisor = min(p, num
            print("{}={}*{}".format(num, smaller_divisor, num
            return
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: factors <file>")
        exit(1)
    with open(argv[1], 'r') as file:
        for line in file:
            factorize(int(line))