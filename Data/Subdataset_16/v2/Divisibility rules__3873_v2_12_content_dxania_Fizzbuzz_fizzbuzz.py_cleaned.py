def fonk1():
    b1 = [item.strip() for item in input("Enter the first list (separate elements with commas): ").split(",")]
    print(f"List1: {b1}")
    print(f"List1 is {len(b1)} elements long")
    b2 = [item.strip() for item in input("Enter the second list (separate elements with commas): ").split(",")]
    print(f"List2: {b2}")
    print(f"List2 is {len(b2)} elements long")
    b3 = fonk2(b1, b2)
    print(f"Result: {b3}")
def fonk2(b1, b2):
    b4 = len(b1) + len(b2)
    if b4 % b5 = = 0 and b4 % b6 == 0:
        return 'FizzBuzz'
    elif b4 % b5 = = 0:
        return 'Fizz'
    elif b4 % b6 = = 0:
        return 'Buzz'
    else:
        return str(b4)
if b7 = = "__main__":
    fonk1()