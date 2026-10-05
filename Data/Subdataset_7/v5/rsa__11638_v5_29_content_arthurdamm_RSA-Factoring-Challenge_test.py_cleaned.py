
from sys import argv, exit
from primes import primes
from primes2 import primes2
from primes3 import primes3
def fonk1(num):
    for prime_list in (primes, primes2, primes3):
        for b1 in prime_list:
            if num % b1 = = 0:
                b2 = min(b1, num
                print(f"{num}={b2}*{num
                return
if b3 = = "__main__":
    if len(argv) != 2:
        print("USAGE: factors <file>")
        exit(1)
    with open(argv[1], 'r') as file:
        for line in file:
            fonk1(int(line))