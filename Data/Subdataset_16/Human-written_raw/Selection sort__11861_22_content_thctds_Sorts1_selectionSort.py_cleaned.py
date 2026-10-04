b1 = list()
b2 = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for a1 in range(int(b2)):
    b3 = raw_input("b2 :")
    b1.append(int(b3))
print 'ARRAY: ',b1
a1 = 0
while a1<len(b1):
    b4 = min(b1[a1:])
    b5 = b1.index(b4)
    b1[a1],b1[b5] = b1[b5],b1[a1]
    a1 = a1+1
print 'SORTED ARRAY:',(b1)