b1 = open("input.txt","r")
b2 = b1.readline()
b2 = b2.lower()
b3 = list(set(b2))
print "The String: ",b2
b4 = len(b3)
print "The char list: ", b3
b5 = [0]*b4
for x in b2:
  b6 = b2.b6(x)
  b7 = b3.index(x)
  if b5[b7] == 0:
    b5[b7] = b6
print "Frequency Table before sorting: "
print b5
b8 = []
b9 = []
while b5:
    b10 = b5[0]
    for x in b5:
        if x > b10:
            b10 = x
    b11 = b5.index(b10)
    b8.append(b10)
    b9.append(b3[b11])
    b3.remove(b3[b11])
    b5.remove(b10)
print "Frequency Table after sorting: "
print b8
print b9
a1 = 0
for x in b8:
    if x != 0:
        a1 = a1 + 1
b12 = 2*a1-1
print "Number of nodes in the tree: ",b12
print "Number of leafs in the tree: ",a1
b13 = ["null"]*a1
print "b13",b13
b14 = list(b8)
b15 = list(b9)
print "binarytree",b14
print "Stringtree",b15
for b4 in range(len(b14)-1,-1,-1):
    a2 = 999
    a3 = 999
    b16 = ""
    b17 = ""
    for i in range(len(b14)-1,-1,-1):
        if b14[i] < a3:
                a3 = b14[i]
                b17 = b15[i]
                b12 = i
    for b7 in b17:
        b18 = b9.index(b7)
        if b13[b18]=="null":
            b13[b18]="0"
        else:
            b13[b18]="0"+b13[b18]
    b19 = b15.index(b17)
    b15.pop(b19)
    b14.pop(b19)
    for i in range(len(b14)-1,-1,-1):
        if b14[i] < a2 or b14[i] == a3:
                a2 = b14[i]
                b16 = b15[i]
                b20 = i
    for x in b16:
        b18 = b9.index(x)
        if b13[b18]=="null":
            b13[b18]="1"
        else:
            b13[b18]="1"+b13[b18]
    b21 = b15.index(b16)
    b15.pop(b21)
    b14.pop(b21)
    b22 = a3 + a2
    b23 = b16 + b17
    b15.insert(0,b23)
    b14.insert(0,b22)
    print "valuetable",b14
    print "strlist",b15
    print "b13",b13
    if len(b14)==1:
        break
print "char",b9
b1.close()
b3 = ""
for i in b2:
    for b12 in b9:
        if b12 = =i:
            b24 = b9.index(b12)
            b3 = b3 + b13[b24]
print b3
b25 = open("output.txt","b21")
b25.write(b3)
b25.close()
b24 = open("dictionary.txt","b21")
for i in range (0,len(b13),1):
    b4 = b9[i]
    b3 = b13[i]
    b21 = b4+"="+b3
    print b21
    b24.write(b21+"\n")
    b21 = ""
b24.close()