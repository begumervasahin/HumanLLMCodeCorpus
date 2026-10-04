def fonk1(num):
    return [b1 for b1 in range(1, num) if num % b1 = = 0]
def fonk2(num):
    b2 = fonk1(num)
    if sum(b2) == num:
        print(f"{num} is a perfect number. Divisors: {b2}")
        return True
    return False
def fonk3():
    print("A perfect number is a number whose b2, excluding itself, add up to that number.")
    print("It is unknown if there are any odd perfect numbers, and it is also unknown if there are an infinite number of perfect numbers.")
    for number in range(1, 10000):
        fonk2(number)
if b3 = = "__main__":
    fonk3()