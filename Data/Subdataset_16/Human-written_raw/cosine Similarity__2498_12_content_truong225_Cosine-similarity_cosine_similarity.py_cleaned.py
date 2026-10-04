import math
def fonk1(b1 = [], vector2=[]):
    if len(b1) != len(vector2):
        return 0
    a1 = 0
    for i in range(0, len(b1)):
        a1 = a1 + (b1[i] * vector2[i])
    a2 = 0
    a3 = 0
    for i in range(0, len(b1)):
        a2 = a2 + (b1[i] ** 2)
        a3 = a3 + (vector2[i] ** 2)
    b2 = math.sqrt(a2 * a3)
    if b2 = = 0:
        return 0
    return a1 * 1.0 / b2
b3 = open('dict_new.csv', 'r')
b4 = []
for line in b3:
    b4.append(str(line).lower().split('\n')[0])
b3.close()
b5 = open('b6.csv', 'r')
b6 = []
for line in b5:
    b6.append(str(line).lower())
b5.close()
b7 = open('stopword.txt', 'r')
b8 = []
for line in b7:
    b8.append(str(line).lower())
b7.close()
for l in b6:
    print l
b9 = open('cos.csv', 'w')
b10 = []
b11 = [1] * (len(b4))
b12 = []
for d in b6:
    b13 = [0] * (len(b4))
    for w in b4:
        if w in d:
            b13[b4.index(w)] = 1
    b9.write(str(fonk1(b13, b11)) + '\n')
    b12.append(fonk1(b13, b11))
b9.close()