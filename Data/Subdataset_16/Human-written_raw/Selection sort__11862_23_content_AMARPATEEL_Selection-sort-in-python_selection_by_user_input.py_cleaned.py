def fonk1(b2):
    for i in range(0,len(b2)):
        b1 = i
        print("Current minimum is:",b2[i])
        for j in range (i+1,len(b2)):
            if(b2[b1]>b2[j]):
                b1 = j
        b2[i],b2[b1]=b2[b1],b2[i]
        print("new minimum is:",b2[i])
        print(b2)
        print()
b2 = []
b3 = int(input("No of elments i the b2:"));
for i in range(0,b3):
    b4 = int(input("Enter an element:"));
    b2.append(b4)
print("List before sorting:",b2)
fonk1(b2)
print("List after sorting:",b2)