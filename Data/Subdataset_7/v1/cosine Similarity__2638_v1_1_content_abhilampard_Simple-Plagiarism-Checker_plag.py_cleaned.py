import re
import math
def fonk1(b12, b13):
    try:
        b1 = []
        a1 = 0
        b2 = b12.lower()
        b3 = re.sub("[^\w]", " ", b2).split()
        for b7 in b3:
            if b7 not in b1:
                b1.append(b7)
        b4 = re.sub("[^\w]", " ", b13.lower()).split()
        for b7 in b4:
            if b7 not in b1:
                b1.append(b7)
        b5 = []
        b6 = []
        for b7 in b1:
            a2 = 0
            a3 = 0
            for word2 in b3:
                if b7 = = word2:
                    a2 += 1
            b5.append(a2)
            for word2 in b4:
                if b7 = = word2:
                    a3 += 1
            b6.append(a3)
        b8 = sum(b5[i] * b6[i] for i in range(len(b5)))
        b9 = math.sqrt(sum(b5[i] ** 2 for i in range(len(b5))))
        b10 = math.sqrt(sum(b6[i] ** 2 for i in range(len(b6))))
        a1 = (float)(b8 / (b9 * b10)) * 100
        b11 = "Input query text matches %0.02f%% with database." % a1
        return b11
    except Exception as e:
        return "Please Enter Valid Data"
b12 = "Enter your query here."
b13 = open("database1.txt", "r").read()
b14 = fonk1(b12, b13)
print(b14)