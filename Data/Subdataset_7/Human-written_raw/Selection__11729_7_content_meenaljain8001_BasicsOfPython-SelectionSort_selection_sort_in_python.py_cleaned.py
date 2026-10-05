import sys
b1 = [64, 25, 12, 22, 11]
for i in range(len(b1)):
    b2 = i
    for j in range(i+1, len(b1)):
        if b1[b2] > b1[j]:
            b2 = j
    b1[i], b1[b2] = b1[b2], b1[i]
print ("Sorted array")
for i in range(len(b1)):
    print("%d" %b1[i]),