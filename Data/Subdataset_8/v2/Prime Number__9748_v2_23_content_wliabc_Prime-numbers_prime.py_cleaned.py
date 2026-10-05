
user_input = int(input("Please enter an integer you want to check: "))
is_prime = True
divisor = 2
while divisor < user_input ** 0.5:
    if user_input % divisor == 0:
        is_prime = False
        break
    divisor += 1
if is_prime:
    print(str(user_input) + " is a prime number")
else:
    print(str(user_input) + " is not a prime number")