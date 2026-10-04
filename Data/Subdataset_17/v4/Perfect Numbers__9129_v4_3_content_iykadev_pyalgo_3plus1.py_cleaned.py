def collatz_sequence(x):
    i = 0
    while x > 1:
        i += 1
        if x % 2:
            x = 3 * x + 1
        else:
            x = x / 2
        print(x)
def main(x):
    collatz_sequence(x)
main(15000)