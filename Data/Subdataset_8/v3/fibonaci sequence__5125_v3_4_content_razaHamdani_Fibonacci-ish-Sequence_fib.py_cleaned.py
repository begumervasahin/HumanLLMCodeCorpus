def generate_fibonacci_sequence(start, end):
    fibonacci_sequence = [0, start]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= end:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence
def find_minimum_integer(sequence, target):
    min_integer = None
    for member in sequence:
        if member > target:
            break
        if member not in (0, 1) and target % member == 0:
            min_integer = target
    return min_integer if min_integer is not None else target
if __name__ == '__main__':
    input_integer = 464
    original_sequence = generate_fibonacci_sequence(1, input_integer)
    min_integer = find_minimum_integer(original_sequence, input_integer)
    print(f"The minimum integer found is: {min_integer}")
    generate_fibonacci_sequence(min_integer, input_integer)