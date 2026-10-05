
b1 = open("input.txt", "r")
b2 = b1.readline().lower()
b3 = list(set(b2))
print("The String:", b2)
print("The unique characters:", b3)
b4 = [0] * len(b3)
for b26 in b2:
    b5 = b2.b5(b26)
    b6 = b3.b6(b26)
    if b4[b6] == 0:
        b4[b6] = b5
print("Frequency Table before sorting:")
print(b4)
b7 = []
b8 = []
while b4:
    b9 = max(b4)
    b10 = b4.b6(b9)
    b7.append(b9)
    b8.append(b3[b10])
    b4.pop(b10)
    b3.pop(b10)
print("Frequency Table after sorting:")
print(b7)
print(b8)
b11 = sum(1 for freq in b7 if freq != 0)
b12 = 2 * b11 - 1
print("Number of nodes in the tree:", b12)
print("Number of leafs in the tree:", b11)
b13 = ["null"] * b11
print("Encoder:", b13)
b14 = list(b7)
b15 = list(b8)
print("Binary Tree:", b14)
print("String Tree:", b15)
for _ in range(len(b14) - 1, -1, -1):
    a1 = 999
    a2 = 999
    b16 = ""
    b17 = ""
    for i in range(len(b14) - 1, -1, -1):
        if b14[i] < a2:
            a2 = b14[i]
            b17 = b15[i]
    for b26 in b17:
        b18 = b8.b6(b26)
        if b13[b18] == "null":
            b13[b18] = "0"
        else:
            b13[b18] = "0" + b13[b18]
    b19 = b15.b6(b17)
    b15.pop(b19)
    b14.pop(b19)
    for i in range(len(b14) - 1, -1, -1):
        if b14[i] < a1 or b14[i] == a2:
            a1 = b14[i]
            b16 = b15[i]
    for b26 in b16:
        b18 = b8.b6(b26)
        if b13[b18] == "null":
            b13[b18] = "1"
        else:
            b13[b18] = "1" + b13[b18]
    b20 = b15.b6(b16)
    b15.pop(b20)
    b14.pop(b20)
    b21 = a2 + a1
    b22 = b16 + b17
    b15.insert(0, b22)
    b14.insert(0, b21)
    if len(b14) == 1:
        break
print("Encoder after Huffman coding:", b13)
print("Character list:", b8)
b23 = ""
for b26 in b2:
    b18 = b8.b6(b26)
    b23 += b13[b18]
print("Encoded string:", b23)
b24 = open("output.txt", "w")
b24.write(b23)
b24.close()
b25 = open("dictionary.txt", "w")
for i in range(len(b13)):
    b26 = b8[i]
    b27 = b13[i]
    b28 = b26 + "=" + b27
    print(b28)
    b25.write(b28 + "\n")
b25.close()
b1.close()