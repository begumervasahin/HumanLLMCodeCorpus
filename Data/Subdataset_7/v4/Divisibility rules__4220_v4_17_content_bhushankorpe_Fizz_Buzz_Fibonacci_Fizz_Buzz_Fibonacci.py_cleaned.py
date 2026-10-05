def fonk1(number):
    if number <= 1:
        return False
    for b1 in range(2, number):
        if number % b1 = = 0:
            return False
    return True
def fonk2(b8):
    b2 = [0, 1]
    for i in range(2, b8):
        b2.append(b2[-1] + b2[-2])
    return b2
def fonk3(num):
    if num % b3 = = 0:
        print("Buzz")
    if num % b4 = = 0:
        print("Fizz")
    if num % b5 = = 0:
        print("FizzBuzz")
    if fonk1(num):
        print("BuzzFizz")
    else:
        b6 = fonk2(num)
        print(b6)
if b7 = = '__main__':
    print("How many Fibonacci numbers do you want to see?")
    b8 = int(input())
    fonk3(b8)