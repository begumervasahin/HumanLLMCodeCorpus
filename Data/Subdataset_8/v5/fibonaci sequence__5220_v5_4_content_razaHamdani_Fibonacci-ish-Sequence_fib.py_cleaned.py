def generate_fibonacci_sequence(start, end):
    fibonacci_sequence = [0, start]
    index = 2
    while fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2] <= end:
        fibonacci_sequence.append(fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2])
        index += 1
    return fibonacci_sequence
def find_minimum_divisor(fib_sequence, target):
    smallest_divisor = None
    for fib_number in fib_sequence:
        if fib_number > target:
            break
        if fib_number in (0, 1):
            continue
        if target % fib_number == 0:
            if smallest_divisor is None:
                smallest_divisor = target
            elif target
                smallest_divisor = target
    return smallest_divisor if smallest_divisor is not None else target
if __name__ == '__main__':
    INPUT_INTEGER = 464
    original_fib_sequence = generate_fibonacci_sequence(1, INPUT_INTEGER)
    smallest_divisor = find_minimum_divisor(original_fib_sequence, INPUT_INTEGER)
    if smallest_divisor is None:
        smallest_divisor = INPUT_INTEGER
    print(f"Minimum Integer Found: {smallest_divisor}")
    generate_fibonacci_sequence(smallest_divisor, INPUT_INTEGER)