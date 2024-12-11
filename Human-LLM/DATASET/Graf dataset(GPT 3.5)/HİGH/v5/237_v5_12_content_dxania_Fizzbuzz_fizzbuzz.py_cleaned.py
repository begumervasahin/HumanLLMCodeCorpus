def fonk1():
    b1 = fonk2("first")
    b2 = fonk2("second")
    fonk3(b1, b2)
def fonk2(list_name):
    b3 = input(f"Enter the {list_name} list (separate b4 with commas): ")
    b4 = [element.strip() for element in b3.split(",")]
    print(f"{list_name.capitalize()} list:", b4)
    print(f"{list_name.capitalize()} list contains {len(b4)} b4")
    return b4
def fonk3(b1, b2):
    b5 = len(b1) + len(b2)
    b6 = fonk4(b5)
    print("FizzBuzz b6:", b6)
def fonk4(b5):
    if b5 % b7 = = 0 and b5 % b8 == 0:
        return 'FizzBuzz'
    elif b5 % b7 = = 0:
        return 'Fizz'
    elif b5 % b8 = = 0:
        return 'Buzz'
    else:
        return b5
fonk1()