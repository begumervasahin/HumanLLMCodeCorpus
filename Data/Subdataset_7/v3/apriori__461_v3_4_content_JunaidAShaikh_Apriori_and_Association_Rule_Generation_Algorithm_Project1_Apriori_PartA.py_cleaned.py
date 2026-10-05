import numpy as np
from datetime import datetime
a1 = 0
b1 = []
b2 = {}
a2 = 70
a3 = 50
b3 = 'associationruletestdata.txt'
def fonk1(rule, body):
    global a1, a2
    a4 = 0.0
    a5 = 0.0
    b4 = list(sorted(set(rule) - set(body)))
    for record in range(a1):
        b5 = fonk2(record, body, b4)
        if b5:
            a5 += 1.0
            if fonk3(record, b4):
                a4 += 1.0
    if (a4 / a5) * 100 >= a2:
        return True
    else:
        return False
def fonk2(record, body, b4):
    for element in body:
        b7, b6 = fonk4(element)
        if b6 = = "Up":
            if b1[record][b7 - 1] == 0:
                return False
        elif b6 = = "Down":
            if b1[record][b7 - 1] == 1:
                return False
        elif b1[record][b7 - 1] != b2[b6]:
            return False
    return True
def fonk3(record, b4):
    for element in b4:
        b7, b6 = fonk4(element)
        if b6 = = "Up":
            if b1[record][b7 - 1] == 0:
                return False
        elif b6 = = "Down":
            if b1[record][b7 - 1] == 1:
                return False
        elif b1[record][b7 - 1] != b2[b6]:
            return False
    return True
def fonk4(element):
    b7 = int(element[0:3])
    b6 = element[4:]
    return b7, b6
def fonk5(b23, b19, unsupported_list_from_previous_iteration):
    for prev in unsupported_list_from_previous_iteration:
        b8 = list(set(b23).intersection(prev))
        if len(b8) == (b19 - 1):
            return False
    return True
def fonk6():
    global a1, b1, b2, a3, b3
    b1 = []
    a6 = 0
    a1 = 0
    b9 = []
    with open(b3, 'r') as f:
        for line in f:
            a1 += 1
            b10 = line.split('\t')
            b11 = b10[-1].strip()
            b9.append(b11)
            b10 = b10[:-1]
            a6 = len(b10)
            for index, b12 in enumerate(b10):
                if b12 = = "Down":
                    b10[index] = 0
                elif b12 = = "Up":
                    b10[index] = 1
            b1.append(b10)
    b1 = np.array(b1)
    b13 = sorted(set(b9))
    b14 = list(b13)
    for name in b14:
        b2[name] = b14.index(name)
    b15 = np.zeros((a1, 1))
    b1 = np.hstack((b1, b15))
    a7 = 0
    for x in b9:
        b1[a7][a6] = b2[x]
        a7 += 1
    b16 = fonk7(a6, b14)
    b17 = []
    while True:
        b21, b18 = fonk8(b16)
        if not b21:
            print("No Supported Combinations of b19 equal and greater than " + str(b19))
            break
        print("Supported Combinations of size " + str(b19) + "  " + str(len(b21)))
        b17.append(b21)
        b16, b19 = fonk10(b21, b18)
        if not b16:
            print("No Combinations of b19 and after " + str(b19))
            break
    return b17
def fonk7(a6, b14):
    b16 = []
    for i in range(a6):
        b20 = '{b20:03d}'.format(b20=(i + 1))
        b16.append([b20 + "_Down"])
        b16.append([b20 + "_Up"])
    for x in b14:
        b20 = '{b20:03d}'.format(b20=(a6))
        b16.append([b20 + "_" + str(x)])
    return sorted(b16)
def fonk8(b16):
    global a1, a3
    b21 = []
    b18 = []
    for current_list in b16:
        a8 = 0
        for record in range(a1):
            b5 = fonk9(record, current_list)
            if b5:
                a8 += 1
                if a8 >= a3:
                    break
        if a8 < a3:
            b18.append(current_list)
        else:
            b21.append(current_list)
    return b21, b18
def fonk9(record, current_list):
    for element in current_list:
        b7, b6 = fonk4(element)
        if b6 = = "Up":
            if b1[record][b7 - 1] == 0:
                return False
        elif b6 = = "Down":
            if b1[record][b7 - 1] == 1:
                return False
        elif b1[record][b7 - 1] != b2[b6]:
            return False
    return True
def fonk10(b21, unsupported_list_from_previous_iteration):
    global a6
    b16 = []
    b19 = len(b21[0]) + 1
    if b19 != 2:
        for element1_idx, element1 in enumerate(b21):
            for element2_idx in range(element1_idx + 1, len(b21)):
                b22 = b21[element2_idx]
                for i in range(b19 - 2):
                    if element1[i] != b22[i]:
                        break
                else:
                    b23 = list(sorted(set(element1 + b22)))
                    if fonk5(b23, b19, unsupported_list_from_previous_iteration):
                        b16.append(b23)
    else:
        for element1_idx, element1 in enumerate(b21):
            for element2_idx in range(element1_idx + 1, len(b21)):
                b22 = b21[element2_idx]
                b16.append(element1 + b22)
    b16 = set(tuple(x) for x in b16)
    b16 = list(tuple(x) for x in b16)
    return b16, b19
def fonk11():
    b24 = datetime.now()
    b17 = fonk6()
    return b17
if b25 = = "__main__":
    fonk11()