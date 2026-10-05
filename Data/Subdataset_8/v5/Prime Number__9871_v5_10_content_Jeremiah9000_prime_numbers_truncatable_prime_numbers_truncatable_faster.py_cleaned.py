import time
import math
def timed_quit(start_time):
    print('\nTime elapsed:', time.time() - start_time)
    quit()
def check_prime(number):
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
            if not check_prime(num := int(str(num)[:-1])):
                return False
        except ValueError:
            return True
def main():
    start_time = time.time()
    number = int(input('Enter a number to check if it is truncatable:\n->'))
    if number <= 1:
        print('The number should be greater than 1')
        timed_quit(start_time)
    prime_bool = check_prime(number)
    if not prime_bool:
        print(f"{number} is not prime")
        timed_quit(start_time)
    if '0' in str(number):
        print(f"{number} is not truncatable - it contains '0'")
        timed_quit(start_time)
    if strip_left(number):
        print('Left truncatable')
    else:
        print('Not left truncatable')
    if strip_right(number):
        print('Right truncatable')
    else:
        print('Not right truncatable')
    print("Time elapsed:", time.time() - start_time)
if __name__ == "__main__":
    main()