
b1 = int( input("Enter the number of Elements"))
b2 = []
for i in range(0,b1):
    b2.append(input("enter the elements"))
print("THE LIST IS",b2)
b3 = input("ente the b3 to find")
a1 = 0
b4 = False
a2 = 0
while a1 <  len(b2) and not b4:
    a2 = a2+1
    if b2[a1] == b3:
        b4 = True
        print("b4")
    a1 = a1 +1
print("number of iteration",a2)