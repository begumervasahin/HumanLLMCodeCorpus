def calculate_fibonacci(n):
    first_number = 1
    second_number = 0
    fibonacci_list = []
    for _ in range(n):
        answer = first_number + second_number
        fibonacci_list.append(answer)
        first_number, second_number = second_number, answer
    return fibonacci_list
def print_fibonacci(fibonacci_list):
    for i, number in enumerate(fibonacci_list):
        if i == 0:
            print(f"{number} + 0 = {number}")
        elif i == 1:
            print(f"0 + {number} = {number}")
        else:
            print(f"{fibonacci_list[i - 2]} + {fibonacci_list[i - 1]} = {number}")
def main():
    fibonacci_numbers = calculate_fibonacci(100)
    print_fibonacci(fibonacci_numbers)
if __name__ == "__main__":
    main()