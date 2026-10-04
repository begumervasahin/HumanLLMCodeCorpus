def collatz_sequence(n):
    sequence = []
    while n > 1:
        sequence.append(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n = n
    sequence.append(1)
    return sequence
def main(start_value):
    sequence = collatz_sequence(start_value)
    for value in sequence:
        print(value)
if __name__ == "__main__":
    main(15000)