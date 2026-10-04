def fonk1(N):
    if N <= 1:
        return False
    for b1 in range(2, N):
        if N % b1 = = 0:
            return False
    return True
def fonk2(num):
    b2 = []
    if num % b3 = = 0 or num % b4 == 0 or num % b5 == 0 or fonk1(num):
        if num % b3 = = 0:
            b2.append("Buzz")
        if num % b4 = = 0:
            b2.append("Fizz")
        if num % b5 = = 0:
            b2.append("FizzBuzz")
        if fonk1(num):
            b2.append("BuzzFizz")
        for item in b2:
            print(item)
    else:
        b6 = []
        a, b7 = 0, 1
        for b8 in range(num):
            if b8 = = 0:
                b6.append(a)
            elif b8 = = 1:
                b6.append(b7)
            else:
                a, b7 = b7, a + b7
                b6.append(b7)
        print(b6)
if b9 = = '__main__':
    b10 = int(input("How many Fibonacci numbers do you want to see? "))
    fonk2(b10)