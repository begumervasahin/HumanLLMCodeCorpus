from itertools import accumulate, count
from time import sleep
from exceed import until_exceeded
def triangle_number(n):
    return n * (n + 1)
def triangle_number_alt(n):
    return sum(range(1, n + 1))
def triangle_numbers():
    return accumulate(count(1))
def is_triangle_number(number):
    for num in until_exceeded(number, triangle_numbers()):
        if num == number:
            return True
    return False
def main():
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for t_num in triangle_numbers():
            print(t_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
if __name__ == "__main__":
    main()