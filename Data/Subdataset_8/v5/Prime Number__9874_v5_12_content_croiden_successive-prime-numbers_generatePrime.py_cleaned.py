import sys
import math
def is_prime(num, primes):
    sqrt_num = int(math.sqrt(num)) + 1
    for prime in primes:
        if prime <= sqrt_num:
            if num
                return False
    return True
def find_nth_minion_digit(n):
    digit_count = 5
    minion_sequence = "23"
    num = 5
    n = int(n)
    primes = [3]
    while True:
        if is_prime(num, primes):
            primes.append(num)
            minion_sequence += str(num)
            if len(minion_sequence) > n + digit_count:
                return minion_sequence[n: n + digit_count]
        num += 2
def main():
    if len(sys.argv) < 2:
        print("Usage: python filename.py [n]")
        return
    n = sys.argv[1]
    minion_digit = find_nth_minion_digit(n)
    print(f"minion[{n}] = {minion_digit}")
if __name__ == "__main__":
    main()