import sys
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def find_prime_numbers_in_range(low_num, high_num):
    sys.stdout.write("Prime Numbers in range (%s,%s): " % (low_num, high_num))
    for i in range(low_num, high_num):
        if is_prime(i):
            print(i, end=' ')
def main():
    find_prime_numbers_in_range(2, 100000)
if __name__ == "__main__":
    main()