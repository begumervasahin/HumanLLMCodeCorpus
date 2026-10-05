a1 = 1946
b1 = str(a1)
while len(b1) != 2 and a1 >= 0 and a1 != 0:
    print(b1)
    b2 = b1[:-1]
    b3 = int(b1[-1])
    b1 = str(int(b2) - (2 * b3))
    a1 = int(b1)
if a1 % b4 = = 0:
    print("Number " + b1 + " is divisible by b4!")