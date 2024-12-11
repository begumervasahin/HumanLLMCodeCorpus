b1 = int(input("Enter first number: "))
b2 = int(input("Enter second number: "))
b3 = [b1, b2]
b3.sort()
b4 = []
for x in range(b3[0] + 1, b3[1]):
    if all(x % i != 0 for i in range(2, x)):
        b4.append(x)
if len(b4) > 1:
    for i in range(0, len(b4) - 1, 3):
        b4[i] = str(b4[i]) + ":"
    for i in range(1, len(b4) - 1, 3):
        b4[i] = str(b4[i]) + "!"
    for i in range(2, len(b4) - 1, 3):
        b4[i] = str(b4[i]) + ","
    print("".join(map(str, b4)))
elif len(b4) == 1:
    print("".join(map(str, b4)))
else:
    print("No Primes")