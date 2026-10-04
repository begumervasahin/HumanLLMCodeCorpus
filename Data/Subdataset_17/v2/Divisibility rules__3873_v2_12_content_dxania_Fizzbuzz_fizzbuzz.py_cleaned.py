def get_input():
    list1 = [item.strip() for item in input("Enter the first list (separate elements with commas): ").split(",")]
    print(f"List1: {list1}")
    print(f"List1 is {len(list1)} elements long")
    list2 = [item.strip() for item in input("Enter the second list (separate elements with commas): ").split(",")]
    print(f"List2: {list2}")
    print(f"List2 is {len(list2)} elements long")
    result = fizzbuzz(list1, list2)
    print(f"Result: {result}")
def fizzbuzz(list1, list2):
    total_length = len(list1) + len(list2)
    if total_length % 3 == 0 and total_length % 5 == 0:
        return 'FizzBuzz'
    elif total_length % 3 == 0:
        return 'Fizz'
    elif total_length % 5 == 0:
        return 'Buzz'
    else:
        return str(total_length)
if __name__ == "__main__":
    get_input()