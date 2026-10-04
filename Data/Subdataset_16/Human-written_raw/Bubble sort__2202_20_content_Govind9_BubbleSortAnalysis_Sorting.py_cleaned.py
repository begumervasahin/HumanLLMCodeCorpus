b1 = []
b2 = []
b3 = []
b4 = []
def fonk1():
    b5 = len(b3)
    b6 = b7 = b8 = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(b5):
        print(str(b2[i]) + "\t" + str(b3[i]) + "\t" + str(b4[i]))
	b6 = b6 + b2[i]
	b7 = b7 + b3[i]
	b8 = b8 + b4[i]
    print(str(b6) + "\t" + str(b7) + "\t" + str(b8))
def fonk2(x):
	b1 = []
	if (len(x) == len(b13)):
		b9 = ""
		for i in x:
			b9 = b9 + b13[int(i)]
		for i in b9:
			b1.append(int(i))
		fonk3(b1)
	for i in range(len(b13)):
		if (str(i) not in x):
			fonk2(x + str(i))
def fonk3(b1):
    b10 = b1
    b3.append(fonk4(b10))
    b10 = b1
    b2.append(fonk5(b10))
    b10 = b1
    b4.append(fonk6(b10))
    b10 = b1
    fonk1()
def fonk4(b1):
    a1 = 0
    for j in range(len(b1)):
        a1 = a1 + 1
        for i in range(len(b1) -1 - j):
            a1 = a1 + 2
            if (b1[i] > b1[i + 1]):
                b11 = b1[i]
                b1[i] = b1[i + 1]
                b1[i + 1] = b11
    return a1
def fonk5(b1):
    a1 = 0
    for j in range(len(b1)):
        a1 = a1 + 3
        a2 = 0
        for i in range(len(b1) -1 - j):
            a1 = a1 + 2
            if (b1[i] > b1[i + 1]):
                a1 = a1 + 2
                a2 = a2 + 1
                b11 = b1[i]
                b1[i] = b1[i + 1]
                b1[i + 1] = b11
        if (a2 < 2):
            break
    return a1
def fonk6(b1):
    a1 = 0
    for j in range(len(b1)):
        a1 = a1 + 3
        b12 = False
        for i in range(len(b1) -1 - j):
            a1 = a1 + 2
            if (b1[i] > b1[i + 1]):
                a1 = a1 + 2
                b12 = True
                b11 = b1[i]
                b1[i] = b1[i + 1]
                b1[i + 1] = b11
        if (not b12):
            break
    return a1
b13 = '123456'
fonk2("")