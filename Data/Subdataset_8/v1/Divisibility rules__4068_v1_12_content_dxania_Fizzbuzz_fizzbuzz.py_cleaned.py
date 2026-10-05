def get_input():
    list1 = [n.strip() for n in input("Enter the first list (separate elements with commas): ").split(",")]
    print("List1:", list1)
    print("List1 is", len(list1), "characters long")
    list2 = [n.strip() for n in input("Enter the second list (separate elements with commas): ").split(",")]
    print("List2:", list2)
    print("List2 is", len(list2), "characters long")
    print(Fizzbuzz(list1, list2))
def Fizzbuzz(a, b):
    totallength = len(a) + len(b)
    if totallength % 3 == 0 and totallength % 5 == 0:
        return 'FizzBuzz'
    elif totallength % 3 == 0:
        return 'Fizz'
    elif totallength % 5 == 0:
        return 'Buzz'
    else:
        return totallength
if __name__ == "__main__":
    get_input()