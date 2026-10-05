import time
import math
def timed_quit():
    print('\ntime:\n' + str(time.time() - start))
    quit()
number0 = int(input('Enter a number to check if it is truncatable:\n->'))
start = time.time()
def check_prime(number):
    print(f'Current time: {time.time() - start}')
    print(number)
    if number % 2 == 0:
        return False
    for num in range(3, (int(math.sqrt(number)) + 1), 2):
        if number % num == 0:
            return False
    return True
def strip_left(num):
    while True:
        try:
            if not check_prime(num := int(str(num)[1:])):
                return False
        except ValueError:
            return True
def strip_right(num):
    while True:
        try:
            if not check_prime(num := int(str(num)[0:-1])):
                return False
        except ValueError:
            return True
if number0 <= 1:
    print('It needs to be greater than 1')
    timed_quit()
prime_bool = check_prime(number0)
if not prime_bool:
    print(f"{number0} is not prime")
    timed_quit()
for char in str(number0):
    if char == '0':
        print(f"{number0} is not truncatable - it contains a '0'")
        timed_quit()
if strip_left(number0):
    print('Left truncatable')
else:
    print('Not left truncatable')
if strip_right(number0):
    print('Right truncatable')
else:
    print('Not right truncatable')
print("Finish time: " + str(time.time() - start))