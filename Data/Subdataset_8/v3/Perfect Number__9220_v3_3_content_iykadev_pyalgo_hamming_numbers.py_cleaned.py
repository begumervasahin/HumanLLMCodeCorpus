import sys
def is_hamming_number(x):
    if x == 1:
        return True
    for factor in (2, 3, 5):
        if x % factor == 0:
            return is_hamming_number(x
    return False
def print_hamming_numbers(limit):
    for num in range(1, limit + 1):
        if is_hamming_number(num):
            print(num, end=' ')
def hamming_numbers_main():
    print("Hamming Numbers:", end=' ')
    print_hamming_numbers(9830)
if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    hamming_numbers_main()