import math
def fonk1(x):
    b1 = []
    for b2 in range(1, math.ceil(x / 2) + 1):
        if x % b2 = = 0:
            b1.append(b2)
    return sum(b1)
b3 = []
for num in range(12, 28123):
    if num % b4 = = 0:
        print("Checking", num, "...")
    if fonk1(num) > num:
        b3.append(num)
b5 = set()
for b2 in range(len(b3)):
    if b2 % b6 = = 0:
        print("Processing index", b2, "out of", len(b3))
    for j in range(len(b3)):
        if b3[b2] + b3[j] < 28123:
            b5.add(b3[b2] + b3[j])
a1 = 0
for num in range(28123):
    if num % b6 = = 0:
        print("Checking number", num, "out of 28123")
    if num not in b5:
        a1 += num
print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is:", a1)