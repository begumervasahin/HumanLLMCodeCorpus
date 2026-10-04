import sys
import math
def is_prime(num, primes):
    sqrt_num = int(math.sqrt(num)) + 1
    for p in primes:
        if p <= sqrt_num:
            if num % p == 0:
                return False
    return True
def generate_minion_string(n):
    LEN = 5
    minion_string = "23"
    i = 5
    n = int(n)
    primes = [3]
    while True:
        if is_prime(i, primes):
            primes.append(i)
            minion_string += str(i)
            if len(minion_string) > n + LEN:
                return minion_string[n:n + LEN]
        i += 2
def main():
    if len(sys.argv) > 1:
        n = sys.argv[1]
        print(f"minion[{n}] = {generate_minion_string(n)}")
    else:
        print("Please provide an index as a command-line argument.")
if __name__ == "__main__":
    main()