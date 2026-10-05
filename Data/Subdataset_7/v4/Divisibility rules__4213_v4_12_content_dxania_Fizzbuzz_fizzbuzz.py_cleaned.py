def fonk1():
    b1 = input("Enter the first list (separate elements with commas): ").split(",")
    print("List1:", b1)
    print("List1 contains", len(b1), "elements")
    b2 = input("Enter the second list (separate elements with commas): ").split(",")
    print("List2:", b2)
    print("List2 contains", len(b2), "elements")
    print(f"Fizzbuzz result: {fonk2(b1, b2)}")
def fonk2(a, b):
    b3 = len(a) + len(b)
    if b3 % b4 = = 0 and b3 % b5 == 0:
        return 'FizzBuzz'
    elif b3 % b4 = = 0:
        return 'Fizz'
    elif b3 % b5 = = 0:
        return 'Buzz'
    else:
        return b3
fonk1()