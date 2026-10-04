import time
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num * 0.5 + 1)):
        if num % i == 0:
            return False
    return True
def main():
    start_time = time.time()
    primes = []
    for i in range(10000):
        if is_prime(i):
            primes.append(i)
    print(primes)
    for prime in primes:
        mersenne_number = 2 ** prime - 1
        if is_prime(mersenne_number):
            elapsed_time = time.time() - start_time
            print(elapsed_time)
            print(2 ** (prime - 1) * mersenne_number)
if __name__ == '__main__':
    main()