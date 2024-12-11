def fonk1(number):
    if number <= 1:
        return False
    for b1 in range(2, number):
        if number % b1 = = 0:
            return False
    return True
def fonk2(num):
    if num % b2 = = 0:
        print("Buzz")
    if num % b3 = = 0:
        print("Fizz")
    if num % b4 = = 0:
        print("FizzBuzz")
    if fonk1(num):
        print("BuzzFizz")
    else:
        b5 = [0, 1]
        for i in range(2, num):
            b5.append(b5[-1] + b5[-2])
        print(b5[:num])
if b6 = = '__main__':
    print("How many Fibonacci numbers do you want to see?")
    b7 = int(input())
    fonk2(b7)