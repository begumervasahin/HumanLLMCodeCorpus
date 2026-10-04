import time
import math
def timed_quit():
    print('\nElapsed time: ' + str(time.time() - start))
    quit()
def check_prime(number):
    print(f'Current time: {time.time() - start}')
    print(number)
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2
    for num in range(3, int(math.sqrt(number)) + 1, 2):
        if number % num == 0:
            return False
    return True
def strip_left(num):
    while True:
        try:
            num = int(str(num)[1:])
            if not check_prime(num):
                return False
        except ValueError:
            return True
def strip_right(num):
    while True:
        try:
            num = int(str(num)[:-1])
            if not check_prime(num):
                return False
        except ValueError:
            return True
def main():
    number0 = int(input('Enter a number to see if it is truncatable: \n-> '))
    global start
    start = time.time()
    if number0 <= 1:
        print('The number needs to be greater than 1.')
        timed_quit()
    if not check_prime(number0):
        print(f"{number0} is not prime.")
        timed_quit()
    if '0' in str(number0):
        print(f"{number0} is not truncatable - contains a '0'.")
        timed_quit()
    if strip_left(number0):
        print('Left truncatable.')
    else:
        print('Not left truncatable.')
    if strip_right(number0):
        print('Right truncatable.')
    else:
        print('Not right truncatable.')
    print("Finish time: " + str(time.time() - start))
if __name__ == "__main__":
    main()