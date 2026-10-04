print("Welcome random tester, this program will print all the prime numbers from 2 to b1")
b1 = int(input("Enter b1\b1"))
b2 = [True for i in range(b1+1)]
a1 = 2
while a1 * a1 <= b1:
    if b2[a1] == True:
        for i in range(a1 * 2, b1 + 1, a1):
            b2[i] = False
    a1 += 1
for x in range(2, b1 + 1):
    if b2[x]:
        print(x)