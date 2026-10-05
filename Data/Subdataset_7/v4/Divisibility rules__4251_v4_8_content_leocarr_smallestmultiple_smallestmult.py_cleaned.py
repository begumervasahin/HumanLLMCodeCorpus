
b1 = int(input("What is the max multiple? "))
b2 = False
a1 = 0
b3 = b1
while not b2:
    a2 = 0
    for b4 in range(1, b1 + 1):
        if b3 % b4 = = 0:
            a2 += 1
    if a2 = = b1:
        b2 = True
        a1 = b3
    else:
        b3 += b1
print(f"The a1 number that is evenly divisible by all of the numbers from 1 to {b1} is {a1}")