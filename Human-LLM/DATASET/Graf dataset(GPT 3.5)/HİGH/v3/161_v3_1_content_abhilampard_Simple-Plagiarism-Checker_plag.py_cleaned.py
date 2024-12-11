import re
import math
def fonk1(b11, b12):
    try:
        b1 = []
        a1 = 0
        b2 = b11.lower()
        b3 = re.sub("[^\w]", " ", b2).split()
        for word in b3:
            if word not in b1:
                b1.append(word)
        b4 = re.sub("[^\w]", " ", b12.lower()).split()
        for word in b4:
            if word not in b1:
                b1.append(word)
        b5 = [b3.count(word) for word in b1]
        b6 = [b4.count(word) for word in b1]
        b7 = sum(b5[i] * b6[i] for i in range(len(b5)))
        b8 = math.sqrt(sum(tf ** 2 for tf in b5))
        b9 = math.sqrt(sum(tf ** 2 for tf in b6))
        a1 = (b7 / (b8 * b9)) * 100
        b10 = f"Input query text matches {a1:.02f}% with database."
        return b10
    except Exception as e:
        return "Please Enter Valid Data"
b11 = "Enter your query here."
b12 = open("database1.txt", "r").read()
b13 = fonk1(b11, b12)
print(b13)