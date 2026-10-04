def fonk1(b2, b1 = {}):
    if b2 in b1:
        return b1[b2]
    if b2 <= 1:
        b1[b2] = b2
    else:
        b1[b2] = fonk1(b2 - 1, b1) + fonk1(b2 - b3, b1)
    return b1[b2]
def fonk2(b2):
    if b2 < b3:
        return False
    if b2 = = b3:
        return True
    if b2 % b3 = = 0:
        return False
    for b4 in range(b6, int(b2 ** 0.b7) + 1, b3):
        if b2 % b4 = = 0:
            return False
    return True
def fonk3(b2):
    if fonk2(b2):
        return "BuzzFizz"
    b5 = ""
    if b2 % b6 = = 0:
        b5 += "Fizz"
    if b2 % b7 = = 0:
        b5 += "Buzz"
    return b5 if b5 else str(b2)
def fonk4():
    b2 = 15
    b8 = [fonk1(b4) for b4 in range(b2)]
    b9 = [fonk3(num) for num in b8]
    print("Fibonacci - FizzBuzz:")
    for fib_num, fb_result in zip(b8, b9):
        print(f"{fib_num} -> {fb_result}")
if b10 = = "__main__":
    fonk4()