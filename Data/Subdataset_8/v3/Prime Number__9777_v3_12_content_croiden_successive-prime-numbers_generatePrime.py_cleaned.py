import sys
import math
def is_prime(num, primes):
    sqrt_num = int(math.sqrt(num)) + 1
    for prime in primes:
        if prime <= sqrt_num:
            if num % prime == 0:
                return False
    return True
def find_nth_substring(n):
    length = 5
    minion = "23"
    i = 5
    nn = int(n)
    primes = [3]
    while True:
        if is_prime(i, primes):
            primes.append(i)
            minion += str(i)
            if len(minion) > nn + length:
                return minion[nn: nn + length]
        i += 2
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py [n]")
        return
    n = sys.argv[1]
    result = find_nth_substring(n)
    print(f"minion[{n}] = {result}")
if __name__ == "__main__":
    main()