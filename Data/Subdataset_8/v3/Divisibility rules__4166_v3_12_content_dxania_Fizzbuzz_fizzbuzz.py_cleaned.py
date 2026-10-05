def get_input():
    list1 = input_list("first")
    list2 = input_list("second")
    print_fizzbuzz_result(list1, list2)
def input_list(list_name):
    input_str = input(f"Enter the {list_name} list (separate elements with commas): ")
    elements = [element.strip() for element in input_str.split(",")]
    print(f"{list_name.capitalize()} list:", elements)
    print(f"{list_name.capitalize()} list is {len(elements)} elements long")
    return elements
def print_fizzbuzz_result(list1, list2):
    total_length = len(list1) + len(list2)
    result = fizzbuzz(total_length)
    print("FizzBuzz result:", result)
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
if __name__ == "__main__":
    get_input()
Q