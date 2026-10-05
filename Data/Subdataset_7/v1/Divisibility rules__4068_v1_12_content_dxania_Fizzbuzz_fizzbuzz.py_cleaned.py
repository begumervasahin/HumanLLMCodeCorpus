def fonk1():
    b1 = [n.strip() for n in input("Enter the first list (separate elements with commas): ").split(",")]
    print("List1:", b1)
    print("List1 is", len(b1), "characters long")
    b2 = [n.strip() for n in input("Enter the second list (separate elements with commas): ").split(",")]
    print("List2:", b2)
    print("List2 is", len(b2), "characters long")
    print(fonk2(b1, b2))
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
if b6 = = "__main__":
    fonk1()