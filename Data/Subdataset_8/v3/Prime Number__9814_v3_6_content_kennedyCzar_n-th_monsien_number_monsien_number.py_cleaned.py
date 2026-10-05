import random
def nth_prime(n):
    number = 2
    primes_found = 0
    while primes_found < n:
        if is_prime(number):
            primes_found += 1
        number += 1
    return number - 1
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_monisen(n):
    prime_count = 0
    number = 2
    while True:
        if is_prime(number):
            m = 2 ** number - 1
            if is_prime(m):
                prime_count += 1
                if prime_count == n:
                    return m
        number += 1
def generate_monisen_file(n):
    monisen = find_monisen(n)
    with open(f'monisen_{n}.txt', 'w') as file:
        file.write(str(monisen))
def convert_to_base(num, base):
    if num >= base:
        convert_to_base(num
    print(num % base, end=' ')
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print("6th prime number:", nth_prime(6))
    print("6th Monisen number:", find_monisen(6))
    generate_monisen_file(6)
    numA = int(input("Enter the first number: "))
    numB = int(input("Enter the base: "))
    convert_to_base(numA, numB)