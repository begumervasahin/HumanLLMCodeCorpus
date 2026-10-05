def generate_fibonacci_list(limit):
    first_number = 1
    second_number = 0
    fibonacci_list = []
    for counter in range(limit):
        answer = first_number + second_number
        fibonacci_list.append(answer)
        first_number = second_number
        second_number = answer
    return fibonacci_list
def print_fibonacci_sequence(fibonacci_list):
    for counter in range(len(fibonacci_list)):
        if counter == 0:
            print(f"{fibonacci_list[0]} + 0 = {fibonacci_list[0]}")
        elif counter == 1:
            print(f"0 + {fibonacci_list[1]} = {fibonacci_list[1]}")
        else:
            print(f"{fibonacci_list[counter - 2]} + {fibonacci_list[counter - 1]} = {fibonacci_list[counter]}")
def main():
    limit = 100
    fibonacci_list = generate_fibonacci_list(limit)
    print_fibonacci_sequence(fibonacci_list)
if __name__ == "__main__":
    main()