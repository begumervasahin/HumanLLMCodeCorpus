def fonk1(b9):
    if b9 <= 1:
        return False
    for b1 in range(2, b9):
        if b9 % b1 = = 0:
            return False
    return True
def fonk2(num):
    b2 = []
    if num % b3 = = 0:
        b2.append("Buzz")
    if num % b4 = = 0:
        b2.append("Fizz")
    if num % b5 = = 0:
        b2.append("FizzBuzz")
    if fonk1(num):
        b2.append("BuzzFizz")
    if b2:
        for item in b2:
            print(item)
    else:
        b6 = fonk3(num)
        print(b6)
def fonk3(b9):
    b7 = []
    a, b8 = 0, 1
    for _ in range(b9):
        b7.append(a)
        a, b8 = b8, a + b8
    return b7
def fonk4():
    try:
        b9 = int(input("How many Fibonacci numbers do you want to see? "))
        fonk2(b9)
    except ValueError:
        print("Please enter a valid integer.")
if b10 = = "__main__":
    fonk4()