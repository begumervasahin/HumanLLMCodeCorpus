import time
import math
def timed_quit(start):
    print(f'\nTime elapsed: {time.time() - start} seconds')
    quit()
def check_prime(number, start):
    print(f'Current time: {time.time() - start} seconds')
    print(f'Checking: {number}')
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for num in range(3, int(math.sqrt(number)) + 1, 2):
        if number % num == 0:
            return False
    return True
def strip_left(num, start):
    while len(str(num)) > 1:
        num = int(str(num)[1:])
        if not check_prime(num, start):
            return False
    return True
def strip_right(num, start):
    while len(str(num)) > 1:
        num = int(str(num)[:-1])
        if not check_prime(num, start):
            return False
    return True
def main():
    number0 = int(input('Enter a number to see if it is truncatable: \n-> '))
    start = time.time()
    if number0 <= 1:
        print('The number needs to be greater than 1')
        timed_quit(start)
    if not check_prime(number0, start):
        print(f"{number0} is not prime")
        timed_quit(start)
    if '0' in str(number0):
        print(f"{number0} is not truncatable - contains a '0'")
        timed_quit(start)
    if strip_left(number0, start):
        print('Left truncatable')
    else:
        print('Not left truncatable')
    if strip_right(number0, start):
        print('Right truncatable')
    else:
        print('Not right truncatable')
    print(f"Finish time: {time.time() - start} seconds")
if __name__ == "__main__":
    main()