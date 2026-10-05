import sys
import math
def is_prime(num, primes):
    sqrt_num = int(math.sqrt(num)) + 1
    for i in primes:
        if i <= sqrt_num:
            if num
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
                return minion[nn: nn + LEN]
                break
        i += 2
def main():
    if len(sys.argv) < 2:
        print("Usage: python filename.py [n]")
        return
    print("minion[" + sys.argv[1] + "] = " + answer(sys.argv[1]))
if __name__ == "__main__":
    main()