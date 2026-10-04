import sys
import math
def is_prime(num, primes):
    sqt = int(math.sqrt(num)) + 1
    for i in primes:
        if i <= sqt:
            if num % i == 0:
                return False
    return True
def answer(n):
    LEN = 5
    minion = "23"
    i = 5
    nn = int(n)
    primes = [3]
    while True:
        if is_prime(i, primes):
            primes.append(i)
            minion += str(i)
            if len(minion) > nn + LEN:
                return minion[nn:nn + LEN]
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
    print(f"minion[{index}] = {answer(index)}")
if __name__ == "__main__":
    main()