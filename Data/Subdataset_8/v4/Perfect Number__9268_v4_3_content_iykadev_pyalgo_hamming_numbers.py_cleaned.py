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
def hamming_numbers(x):
    if x == 1:
        return
    hamming_numbers(x - 1)
    if is_hamming_number(x):
        print("%s" % x, end=' ')
def hamming_numbers_main():
    sys.stdout.write("Hamming Numbers: ")
    hamming_numbers(9830)
hamming_numbers_main()