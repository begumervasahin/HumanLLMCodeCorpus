def generate_fibonacci_sequence(start, max_value):
    fibonacci_sequence = [0, start]
    while (fibonacci_sequence[-1] + fibonacci_sequence[-2] <= max_value):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    print(fibonacci_sequence)
    return fibonacci_sequence
def find_min_starting_integer(fib_sequence, target_value):
    min_start_int = None
    for num in fib_sequence:
        if num > target_value:
            break
        if num in (0, 1):
            continue
        if target_value % num == 0:
            quotient = target_value
            if min_start_int is None or quotient < min_start_int:
                min_start_int = quotient
    return min_start_int
if __name__ == '__main__':
    INPUT_INTEGER = 464
    original_fib_sequence = generate_fibonacci_sequence(1, INPUT_INTEGER)
    min_starting_int = find_min_starting_integer(original_fib_sequence, INPUT_INTEGER)
    if min_starting_int is None:
        min_starting_int = INPUT_INTEGER
    print(f"Min Integer Found: {min_starting_int}")
    generate_fibonacci_sequence(min_starting_int, INPUT_INTEGER)