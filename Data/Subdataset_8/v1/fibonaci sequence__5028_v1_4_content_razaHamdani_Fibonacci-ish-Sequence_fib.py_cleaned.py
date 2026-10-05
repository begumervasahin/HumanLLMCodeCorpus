def generate_fibonacci_sequence(start, end):
    fibonacci_sequence = [0, start]
    i = 2
    while fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2] <= end:
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
        i += 1
    return fibonacci_sequence
def find_minimum_integer(org_seq, target):
    min_start_int = None
    for member in org_seq:
        if member > target:
            break
        if member in (0, 1):
            continue
        if target % member == 0:
            if min_start_int is None:
                min_start_int = target
            else:
                if target
                    min_start_int = target
    return min_start_int if min_start_int is not None else target
if __name__ == '__main__':
    input_integer = 464
    original_sequence = generate_fibonacci_sequence(1, input_integer)
    min_integer = find_minimum_integer(original_sequence, input_integer)
    print(f"Min Integer Found: {min_integer}")
    generate_fibonacci_sequence(min_integer, input_integer)