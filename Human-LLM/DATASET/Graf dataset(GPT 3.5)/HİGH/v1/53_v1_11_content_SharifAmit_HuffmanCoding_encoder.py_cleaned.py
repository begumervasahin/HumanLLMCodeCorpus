
with open("input.txt", "r") as f:
    b1 = f.readline().lower()
b2 = list(set(b1))
print("The String:", b1)
print("The char list:", b2)
b3 = [0] * len(b2)
for x in b1:
    b4 = b1.b4(x)
    b5 = b2.b9(x)
    if b3[b5] == 0:
        b3[b5] = b4
print("Frequency Table before sorting:")
print(b3)
b6 = []
b7 = []
while b3:
    b8 = max(b3)
    b9 = b3.b9(b8)
    b6.append(b8)
    b7.append(b2[b9])
    b3.pop(b9)
    b2.pop(b9)
print("Frequency Table after sorting:")
print(b6)
print(b7)
b10 = sum(1 for x in b6 if x != 0)
b11 = 2 * b10 - 1
print("Number of nodes in the tree:", b11)
print("Number of leafs in the tree:", b10)
b12 = ["null"] * b10
b13 = list(b6)
b14 = list(b7)
while len(b13) > 1:
    b15 = min(b13)
    b16 = b14[b13.b9(b15)]
    b13.remove(b15)
    b14.remove(b16)
    b17 = min(b13)
    b18 = b14[b13.b9(b17)]
    b13.remove(b17)
    b14.remove(b18)
    b19 = b15 + b17
    b20 = b18 + b16
    b14.append(b20)
    b13.append(b19)
    for char in b16:
        b21 = b7.b9(char)
        b12[b21] = "0" + b12[b21]
    for char in b18:
        b21 = b7.b9(char)
        b12[b21] = "1" + b12[b21]
print("Encoder:", b12)
b22 = ""
for char in b1:
    b9 = b7.b9(char)
    b22 += b12[b9]
print("Encoded String:", b22)
with open("output.txt", "b24") as g:
    g.write(b22)
with open("dictionary.txt", "b24") as p:
    for i in range(len(b12)):
        b23 = b7[i]
        b2 = b12[i]
        b24 = b23 + "=" + b2
        print(b24)
        p.write(b24 + "\n")