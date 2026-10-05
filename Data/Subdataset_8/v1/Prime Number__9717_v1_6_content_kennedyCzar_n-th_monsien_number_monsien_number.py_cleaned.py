import random
def nth_prime(n):
    number = 10
    p = 2
    while p < n:
        if all(number % i != 0 for i in range(2, number)):
            p += 1
        number += 1
    return number - 1
def is_prime(num):
    return all(num % i != 0 for i in range(2, num))
def find_monisen(n):
    prime_count = 0
    number = 10
    while prime_count < n:
        if is_prime(number):
            m = 2 ** number - 1
            if is_prime(m):
                prime_count += 1
        number += 1
    return m
def generate_monisen_file(n):
    monisen = find_monisen(n)
    with open(f'monisen_{n}.txt', 'w') as file:
        file.write(str(monisen))
def foo(num, base):
    if num >= base:
        foo(num
    print(num % base, end=' ')
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print("6th prime number:", nth_prime(6))
    print("6th Monisen number:", find_monisen(6))
    generate_monisen_file(6)
    numA = int(input("Enter the first number: "))
    numB = int(input("Enter the base: "))
    foo(numA, numB)