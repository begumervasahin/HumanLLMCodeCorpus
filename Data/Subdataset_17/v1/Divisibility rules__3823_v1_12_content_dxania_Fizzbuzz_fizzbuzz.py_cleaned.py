def get_input():
    list1 = [n.strip() for n in input("Enter the first list (separate elements with commas): ").split(",")]
    print("List1:", list1)
    print("List1 is " + str(len(list1)) + " elements long")
    list2 = [n.strip() for n in input("Enter the second list (separate elements with commas): ").split(",")]
    print("List2:", list2)
    print("List2 is " + str(len(list2)) + " elements long")
    print("Result:", fizzbuzz(list1, list2))
def fizzbuzz(a, b):
    total_length = len(a) + len(b)
    if total_length % 3 == 0 and total_length % 5 == 0:
        return 'FizzBuzz'
    elif total_length % 3 == 0:
        return 'Fizz'
    elif total_length % 5 == 0:
        return 'Buzz'
    else:
        return str(total_length)
get_input()