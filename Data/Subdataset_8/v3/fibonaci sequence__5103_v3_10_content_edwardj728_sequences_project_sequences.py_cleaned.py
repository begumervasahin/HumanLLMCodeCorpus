def is_arithmetic(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] != sequence[i] + (sequence[i] - sequence[i - 1]):
            return False
    return True
def is_geometric(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] != sequence[i] * 2:
            return False
    return True
def is_quadratic(sequence):
    if len(sequence) < 3:
        return False
    differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    return all(diff == differences[0] for diff in differences)
def is_cubic(sequence):
    if len(sequence) < 4:
        return False
    differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    ratios = [differences[i + 1] - differences[i] for i in range(0, len(differences) - 1)]
    return all(ratio == ratios[0] for ratio in ratios)
def is_fibonacci(sequence):
    if len(sequence) < 4:
        return False
    return all(sequence[i] == sequence[i - 1] + sequence[i - 2] for i in range(2, len(sequence)))
user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
sequence = list(map(int, user_input.split(",")))
if is_arithmetic(sequence):
    print("Arithmetic Sequence")
if is_geometric(sequence):
    print("Geometric Sequence")
if is_quadratic(sequence):
    print("Quadratic Sequence")
if is_cubic(sequence):
    print("Cubic Sequence")
if is_fibonacci(sequence):
    print("Fibonacci Sequence")