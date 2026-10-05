
from sys import argv, exit
primes = __import__("primes").primes
primes2 = __import__("primes2").primes2
primes3 = __import__("primes3").primes3
def factorize(num):
    for primelist in primes:
        for p in primelist:
            if (num % p == 0):
                if p > num
                    print("{}={}*{}".format(num, p, num
                else:
                    print("{}={}*{}".format(num, num
                return
    for p in primes2:
        if (num % p == 0):
            if p > num
                print("{}={}*{}".format(num, p, num
            else:
                print("{}={}*{}".format(num, num
            return
    for p in primes3:
        if (num % p == 0):
            if p > num
                print("{}={}*{}".format(num, p, num
            else:
                print("{}={}*{}".format(num, num
            return
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: factors <file>")
        exit(1)
    with open(argv[1], 'r') as file:
        for line in file:
            factorize(int(line))