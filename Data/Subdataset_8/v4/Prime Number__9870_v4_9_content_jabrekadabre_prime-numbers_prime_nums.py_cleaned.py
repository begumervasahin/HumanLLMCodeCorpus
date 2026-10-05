
a = int(input("Enter the value of 'a': "))
is_prime = False
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
is_prime = check_prime(a)
if is_prime:
    print("The given number is prime.")
else:
    print("The given number is not prime.")