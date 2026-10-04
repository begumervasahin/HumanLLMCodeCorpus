def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    a = int(input("Enter the value of a: "))
    if is_prime(a):
        print("The given number is a prime")
    else:
        print("The given number is not a prime")