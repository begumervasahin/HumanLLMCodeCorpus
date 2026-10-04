def main():
    user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    list_int = convert_input_to_int_list(user_input)
    if len(list_int) != 5:
        print("Please enter exactly 5 integers.")
        return
    check_and_print_sequence_type(list_int)
def convert_input_to_int_list(user_input):
    try:
        return list(map(int, user_input.split(",")))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        sys.exit()
def check_and_print_sequence_type(lst):
    if is_arithmetic_sequence(lst):
        print("Arithmetic Sequence")
    if is_geometric_sequence(lst):
        print("Geometric Sequence")
    if is_quadratic_sequence(lst):
        print("Quadratic Sequence")
    if is_cubic_sequence(lst):
        print("Cubic Sequence")
    if is_fibonacci_sequence(lst):
        print("Fibonacci Sequence")
def is_arithmetic_sequence(lst):
    diff = lst[1] - lst[0]
    return all(lst[i] == lst[i - 1] + diff for i in range(1, 5))
def is_geometric_sequence(lst):
    if lst[0] == 0:
        return False
    ratio = lst[1]
    return all(lst[i] == lst[i - 1] * ratio for i in range(1, 5))
def is_quadratic_sequence(lst):
    first_diff = [lst[i] - lst[i - 1] for i in range(1, 5)]
    second_diff = [first_diff[i] - first_diff[i - 1] for i in range(1, 4)]
    return all(second_diff[i] == second_diff[0] for i in range(1, 3))
def is_cubic_sequence(lst):
    first_diff = [lst[i] - lst[i - 1] for i in range(1, 5)]
    second_diff = [first_diff[i] - first_diff[i - 1] for i in range(1, 4)]
    third_diff = [second_diff[i] - second_diff[i - 1] for i in range(1, 3)]
    return all(third_diff[i] == third_diff[0] for i in range(1, 2))
def is_fibonacci_sequence(lst):
    return all(lst[i] == lst[i - 1] + lst[i - 2] for i in range(2, 5))
if __name__ == "__main__":
    main()