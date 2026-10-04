import random
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def find_nth_monisen(n):
    count = 0
    p = 2
    while count < n:
        if is_prime(p):
            m = 2**p - 1
            if is_prime(m):
                count += 1
                if count == n:
                    return m, p
        p += 1
    return None, None
n = 6
monisen, prime_p = find_nth_monisen(n)
if monisen is not None:
    with open("monisen_number.txt", "w") as file:
        file.write(f"The {n}-th Monisen number is: {monisen}\n")
        file.write(f"The corresponding prime number P is: {prime_p}\n")
    print(f"The {n}-th Monisen number is: {monisen}")
    print(f"The corresponding prime number P is: {prime_p}")
else:
    print("Couldn't find the Monisen number.")
d = [i + 1 for i in range(10) if i % 2 == 0]
print(d)
sumA = 0
i = 1
while True:
    sumA += i
    i += 1
    if sumA > 10:
        break
print('i={}, sum={}'.format(i, sumA))
i = 1
while i % 3 != 0:
    print(i, end=' ')
    if i >= 10:
        break
    i += 1
print()
def foo(num, base):
    if num >= base:
        foo(num
    print(num % base, end=' ')
numA = int(input("Enter the number: "))
numB = int(input("Enter the base: "))
foo(numA, numB)
print()