def main():
    user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    list_int = list(map(int, user_input.split(",")))
    if len(list_int) != 5:
        print("Please enter exactly 5 integers.")
        return
    if check_arithmetic_sequence(list_int):
        print("Arithmetic Sequence")
    if check_geometric_sequence(list_int):
        print("Geometric Sequence")
    if check_quadratic_sequence(list_int):
        print("Quadratic Sequence")
    if check_cubic_sequence(list_int):
        print("Cubic Sequence")
    if check_fibonacci_sequence(list_int):
        print("Fibonacci Sequence")
def check_arithmetic_sequence(lst):
    diff = lst[1] - lst[0]
    return all(lst[i] == lst[i - 1] + diff for i in range(1, 5))
def check_geometric_sequence(lst):
    if lst[0] == 0:
        return False
    ratio = lst[1]
    return all(lst[i] == lst[i - 1] * ratio for i in range(1, 5))
def check_quadratic_sequence(lst):
    first_diff = [lst[i] - lst[i - 1] for i in range(1, 5)]
    second_diff = [first_diff[i] - first_diff[i - 1] for i in range(1, 4)]
    return all(second_diff[i] == second_diff[0] for i in range(1, 3))
def check_cubic_sequence(lst):
    first_diff = [lst[i] - lst[i - 1] for i in range(1, 5)]
    second_diff = [first_diff[i] - first_diff[i - 1] for i in range(1, 4)]
    third_diff = [second_diff[i] - second_diff[i - 1] for i in range(1, 3)]
    return all(third_diff[i] == third_diff[0] for i in range(1, 2))
def check_fibonacci_sequence(lst):
    return all(lst[i] == lst[i - 1] + lst[i - 2] for i in range(2, 5))
if __name__ == "__main__":
    main()