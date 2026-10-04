import random
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def find_monisen_number(n):
    count = 0
    p = 2
    while count < n:
        if is_prime(p):
            m = 2 ** p - 1
            if is_prime(m):
                count += 1
                if count == n:
                    return m
        p += 1
def convert_and_print(num, base):
    if num >= base:
        convert_and_print(num
    print(num % base, end=' ')
def main():
    n = int(input("Enter the nth Monisen number: "))
    nth_monisen_number = find_monisen_number(n)
    print(f"The {n}-th Monisen number is: {nth_monisen_number}")
    with open("monisen_number.txt", "w") as file:
        file.write(str(nth_monisen_number))
    numA = int(input("Enter a number: "))
    numB = int(input("Enter the base: "))
    convert_and_print(numA, numB)
    print()
if __name__ == "__main__":
    main()