def fonk1(num):
    b1 = []
    for b2 in range(1, num):
        if num % b2 = = 0:
            b1.append(b2)
    return b1
def fonk2(num):
    b1 = fonk1(num)
    if sum(b1) == num:
        print(f"{num} is a perfect number. Divisors: {b1}")
        return True
    return False
def fonk3():
    print("A perfect number is a number whose b1, not including itself, add up to that number.")
    print("It is unknown if there are any odd perfect numbers, and it is also unknown if there is an infinite amount of perfect numbers.")
    for j in range(1, 10000):
        fonk2(j)
if b3 = = "__main__":
    fonk3()