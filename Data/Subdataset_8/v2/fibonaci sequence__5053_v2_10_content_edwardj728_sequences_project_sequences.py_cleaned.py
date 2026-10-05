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
    diff1 = sequence[1] - sequence[0]
    diff2 = sequence[2] - sequence[1]
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + diff2:
            return False
    return True
def is_cubic(sequence):
    if len(sequence) < 4:
        return False
    diff1 = sequence[1] - sequence[0]
    diff2 = sequence[2] - sequence[1]
    diff3 = sequence[3] - sequence[2]
    ratio1 = diff2 - diff1
    ratio2 = diff3 - diff2
    return ratio1 == ratio2
def is_fibonacci(sequence):
    if len(sequence) < 4:
        return False
    for i in range(2, len(sequence) - 1):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False
    return True
user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
list_input = user_input.split(",")
sequence = list(map(int, list_input))
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