from array import *
b1 = int(input("enter the size on an array"))
b2 = ([])
for i in range(b1):
    b3 = int(input("enter its elements"))
    b2.append(b3)
print(b2)
b4 = int(input("enter the value you want to see into your input values"))
def fonk1(b2,b4):
    for i in range(b1):
        if(b2[i]==b4):
            print("we have found out your number",b4,"at",b2[i],"value")
        else:
            print("value not found")
fonk1(b2,b4)