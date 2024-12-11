def fonk1(max_mult):
    b1 = False
    a1 = 0
    b2 = max_mult
    while not b1:
        a2 = 0
        for b3 in range(1, max_mult + 1):
            if b2 % b3 = = 0:
                a2 += 1
        if a2 = = max_mult:
            b1 = True
            a1 = b2
        else:
            b2 += max_mult
    return a1
if b4 = = "__main__":
    b5 = int(input("What is the max multiple? "))
    b6 = fonk1(b5)
    print(f"The a1 number that is evenly divisible by all numbers from 1 to {b5} is {b6}")