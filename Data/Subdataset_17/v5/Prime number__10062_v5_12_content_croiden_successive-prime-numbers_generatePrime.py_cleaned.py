import sys
import math
def is_prime(num, primes):
    sqrt_num = int(math.sqrt(num)) + 1
    for p in primes:
        if p > sqrt_num:
            break
        if num % p == 0:
            return False
    return True
def generate_minion_string(n):
    SUBSTRING_LENGTH = 5
    minion_string = "23"
    i = 5
    n = int(n)
    primes = [3]
    while len(minion_string) <= n + SUBSTRING_LENGTH:
        if is_prime(i, primes):
            primes.append(i)
            minion_string += str(i)
        i += 2
    return minion_string[n:n + SUBSTRING_LENGTH]
def main():
    if len(sys.argv) > 1:
        n = sys.argv[1]
        result = generate_minion_string(n)
        print(f"minion[{n}] = {result}")
    else:
        print("Please provide an index as a command-line argument.")
if __name__ == "__main__":
    main()