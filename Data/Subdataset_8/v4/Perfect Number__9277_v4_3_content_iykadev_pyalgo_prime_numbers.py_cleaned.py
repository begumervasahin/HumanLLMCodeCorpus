import sys
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
def prime_numbers(low, high):
    sys.stdout.write("Prime Numbers in range (%s, %s): " % (low, high))
    for i in range(low, high):
        if is_prime(i):
            print(i, end=' ')
def prime_numbers_main():
    prime_numbers(2, 100000)
prime_numbers_main()