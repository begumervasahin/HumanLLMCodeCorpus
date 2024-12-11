
b1 = int(input("Enter the number of elements: "))
b2 = []
for i in range(0, b1):
    b2.append(input("Enter the element: "))
print("THE LIST IS", b2)
b3 = input("Enter the b3 to find: ")
a1 = 0
b4 = False
a2 = 0
while a1 < len(b2) and not b4:
    a2 += 1
    if b2[a1] == b3:
        b4 = True
        print("Found")
    a1 += 1
print("Number of iterations:", a2)