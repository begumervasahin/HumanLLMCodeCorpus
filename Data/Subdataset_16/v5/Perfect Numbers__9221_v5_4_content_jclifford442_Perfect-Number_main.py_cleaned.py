def fonk1(n):
    return [b1 for b1 in range(1, n) if n % b1 = = 0]
def fonk2(n):
    return sum(fonk1(n)) == n
def fonk3():
    print(
        "A perfect number is a number whose divisors, not including itself, add up to that number.\n"
        "It is unknown if there are any odd perfect numbers and it is also unknown if there are an infinite number of perfect numbers."
    )
    for number in range(1, 10000):
        if fonk2(number):
            print(f"{number} is a perfect number with divisors {fonk1(number)}")
if b2 = = "__main__":
    fonk3()