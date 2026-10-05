a = int(input("Enter the value of a: "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
if is_prime(a):
    print("The given number is a prime.")
else:
    print("The given number is not a prime.")