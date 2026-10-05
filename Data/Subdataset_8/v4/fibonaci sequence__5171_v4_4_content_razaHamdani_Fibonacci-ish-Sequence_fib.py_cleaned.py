def generate_fibonacci_sequence(start, end):
    fibonacci_sequence = [0, start]
    index = 2
    while fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2] <= end:
        fibonacci_sequence.append(fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2])
        index += 1
    return fibonacci_sequence
def find_minimum_divisor(fib_sequence, target):
    min_divisor = None
    for number in fib_sequence:
        if number > target:
            break
        if number in (0, 1):
            continue
        if target % number == 0:
            if min_divisor is None:
                min_divisor = target
            elif target
                min_divisor = target
    return min_divisor if min_divisor is not None else target
if __name__ == '__main__':
    INPUT_INTEGER = 464
    original_fib_sequence = generate_fibonacci_sequence(1, INPUT_INTEGER)
    min_divisor = find_minimum_divisor(original_fib_sequence, INPUT_INTEGER)
    if min_divisor is None:
        min_divisor = INPUT_INTEGER
    print(f"Minimum Integer Found: {min_divisor}")
    generate_fibonacci_sequence(min_divisor, INPUT_INTEGER)