
from sys import argv, exit
from primes import primes
from primes2 import primes2
from primes3 import primes3
def factorize(num):
    for prime_list in (primes, primes2, primes3):
        for p in prime_list:
            if num % p == 0:
                smaller_divisor = min(p, num
                print(f"{num}={smaller_divisor}*{num
                return
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: factors <file>")
        exit(1)
    with open(argv[1], 'r') as file:
        for line in file:
            factorize(int(line))