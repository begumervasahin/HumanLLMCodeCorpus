def get_input():
    list1 = input_list("first")
    list2 = input_list("second")
    print_fizzbuzz_result(list1, list2)
def input_list(list_name):
    input_str = input(f"Enter the {list_name} list (separate elements with commas): ")
    elements = [element.strip() for element in input_str.split(",")]
    print(f"{list_name.capitalize()} list:", elements)
    print(f"{list_name.capitalize()} list contains {len(elements)} elements")
    return elements
def print_fizzbuzz_result(list1, list2):
    total_length = len(list1) + len(list2)
    result = fizzbuzz(total_length)
    print("FizzBuzz result:", result)
def fizzbuzz(total_length):
    if total_length % 3 == 0 and total_length % 5 == 0:
        return 'FizzBuzz'
    elif total_length % 3 == 0:
        return 'Fizz'
    elif total_length % 5 == 0:
        return 'Buzz'
    else:
        return total_length
get_input()