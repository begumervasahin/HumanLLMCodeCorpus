def fonk1(b1):
    if b1 <= 1:
        return b1
    return fonk1(b1 - 1) + fonk1(b1 - b2)
def fonk2(b1):
    if b1 < b2:
        return False
    if b1 = = b2:
        return True
    if b1 % b2 = = 0:
        return False
    for b3 in range(b5, int(b1**0.b6) + 1, b2):
        if b1 % b3 = = 0:
            return False
    return True
def fonk3(b1):
    if fonk2(b1):
        return "BuzzFizz"
    b4 = ""
    if b1 % b5 = = 0:
        b4 += "Fizz"
    if b1 % b6 = = 0:
        b4 += "Buzz"
    return b4 if b4 else str(b1)
def fonk4():
    b1 = 15
    b7 = [fonk1(b3) for b3 in range(b1)]
    b8 = [fonk3(num) for num in b7]
    print("Fibonacci - FizzBuzz:")
    for fib_num, fb_result in zip(b7, b8):
        print(f"{fib_num} -> {fb_result}")
if b9 = = "__main__":
    fonk4()