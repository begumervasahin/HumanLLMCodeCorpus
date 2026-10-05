import sys
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
def print_hamming_numbers(x):
    if x == 1:
        return
    if is_hamming_number(x):
        print(x, end=' ')
    print_hamming_numbers(x - 1)
def hamming_numbers_main():
    sys.stdout.write("Hamming Numbers: ")
    print_hamming_numbers(9830)
if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    hamming_numbers_main()