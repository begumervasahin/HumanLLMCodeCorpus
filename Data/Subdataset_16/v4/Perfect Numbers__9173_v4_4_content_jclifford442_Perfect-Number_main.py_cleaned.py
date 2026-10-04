def fonk1(n):
    b1 = []
    for b2 in range(1, n):
        if n % b2 = = 0:
            b1.append(b2)
    return b1
def fonk2(n):
    b1 = fonk1(n)
    return sum(b1) == n
print(
    "A perfect number is a number whose b1, not including itself, add up to that number.\n"
    "It is unknown if there are any odd perfect numbers and it is also unknown if there are an infinite number of perfect numbers."
)
for number in range(1, 10000):
    if fonk2(number):
        print(f"{number} is a perfect number with b1 {fonk1(number)}")