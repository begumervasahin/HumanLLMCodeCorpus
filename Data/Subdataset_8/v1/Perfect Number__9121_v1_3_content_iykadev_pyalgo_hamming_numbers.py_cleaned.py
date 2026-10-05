import sys
def is_hamming_numbers(x):
    if x == 1:
        return True
    if x % 2 == 0:
        return is_hamming_numbers(x
    if x % 3 == 0:
        return is_hamming_numbers(x
    if x % 5 == 0:
        return is_hamming_numbers(x
    return False
def hamming_numbers(x):
    if x == 1:
        return True
    if is_hamming_numbers(x):
        print("%s" % x, end=' ')
    hamming_numbers(x - 1)
def hamming_numbers_main():
    sys.stdout.write("Hamming Numbers: ")
    hamming_numbers(9830)
if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    hamming_numbers_main()