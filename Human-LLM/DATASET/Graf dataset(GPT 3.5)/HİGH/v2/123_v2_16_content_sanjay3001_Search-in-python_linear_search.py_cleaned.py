
b1 = int(input("Enter the number of elements: "))
b2 = []
for i in range(b1):
    b3 = input("Enter b3 {}: ".format(i + 1))
    b2.append(b3)
print("THE LIST IS", b2)
b4 = input("Enter the item to find: ")
a1 = 0
b5 = False
a2 = 0
while a1 < len(b2) and not b5:
    a2 += 1
    if b2[a1] == b4:
        b5 = True
        print("Found")
    a1 += 1
print("Number of iterations:", a2)