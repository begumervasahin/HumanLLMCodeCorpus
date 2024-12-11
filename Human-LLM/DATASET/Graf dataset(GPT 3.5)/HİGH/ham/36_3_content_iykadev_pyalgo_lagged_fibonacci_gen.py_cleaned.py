a1 = 3
a2 = 7
b1 = [8, 6, 7, 5, 3, 0, 9]
for n in range(10):
    for i in range(len(b1)):
        if i is 0:
            b2 = (b1[a1-1] + b1[a2-1]) % 10
        elif 0 < i < 6:
            b1[i] = b1[i+1]
        else:
            b1[i] = b2
            print(b1[i])