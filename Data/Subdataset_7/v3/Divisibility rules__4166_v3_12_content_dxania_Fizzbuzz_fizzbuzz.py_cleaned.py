def fonk1():
    b1 = fonk2("first")
    b2 = fonk2("second")
    fonk3(b1, b2)
def fonk2(list_name):
    b3 = input(f"Enter the {list_name} list (separate b4 with commas): ")
    b4 = [element.strip() for element in b3.split(",")]
    print(f"{list_name.capitalize()} list:", b4)
    print(f"{list_name.capitalize()} list is {len(b4)} b4 long")
    return b4
def fonk3(b1, b2):
    b5 = len(b1) + len(b2)
    b6 = fonk4(b5)
    print("FizzBuzz b6:", b6)
def fonk4(n):
    if n % b7 = = 0 and n % b8 == 0:
        return 'FizzBuzz'
    elif n % b7 = = 0:
        return 'Fizz'
    elif n % b8 = = 0:
        return 'Buzz'
    else:
        return n
if b9 = = "__main__":
    fonk1()
Q