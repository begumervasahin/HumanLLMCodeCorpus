import sys
import math
def is_prime(num, primes):
    sqt = int(math.sqrt(num)) + 1
    for prime in primes:
        if prime > sqt:
            break
        if num % prime == 0:
            return False
    return True
def generate_prime_substring(index):
    SUBSTRING_LENGTH = 5
    concatenated_primes = "23"
    i = 5
    primes = [3]
    while True:
        if is_prime(i, primes):
            primes.append(i)
            concatenated_primes += str(i)
            if len(concatenated_primes) > index + SUBSTRING_LENGTH:
                return concatenated_primes[index:index + SUBSTRING_LENGTH]
        i += 2
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <index>")
        return
    try:
        index = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer index.")
        return
    result = generate_prime_substring(index)
    print(f"minion[{index}] = {result}")
if __name__ == "__main__":
    main()