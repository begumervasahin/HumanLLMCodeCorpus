def fonk1(a):
    for i in range(0, len(a)-1):
        b1 = i
        for j in range(i+1, len(a)):
            if a[j] < a[b1]:
                b1 = j
        if b1 != i:
            a[i], a[b1] = a[b1], a[i]
b2 = [12, 3, 43, 43, 9, 3, 2, 2, 43, 23, 53, 3, 3, 23, 23, 12, 53, 91, 1]
print(b2)
fonk1(b2)
print(b2)