import sys
sys.setrecursionlimit(10000)
def is_hamming_number(x):
    if x == 1:
        return True
    if x % 2 == 0:
        return is_hamming_number(x
    if x % 3 == 0:
        return is_hamming_number(x
    if x % 5 == 0:
        return is_hamming_number(x
    return False
def print_hamming_numbers(limit):
    for num in range(1, limit + 1):
        if is_hamming_number(num):
            print(num, end=' ')
def hamming_numbers_main():
    sys.stdout.write("Hamming Numbers: ")
    print_hamming_numbers(9830)
if __name__ == "__main__":
    hamming_numbers_main()