import numpy as np
from datetime import datetime
a1 = 70
a2 = 50
b1 = 'associationruletestdata.txt'
a3 = 0
b2 = []
b3 = {}
def fonk1(rule, body):
    global a3, a1
    numerator, b4 = 0.0, 0.0
    b5 = list(sorted(set(rule) - set(body)))
    for record in range(a3):
        b6 = fonk2(record, body, b5)
        if b6:
            b4 += 1.0
            if fonk3(record, b5):
                numerator += 1.0
    if (numerator / b4) * 100 >= a1:
        return True
    else:
        return False
def fonk2(record, body, b5):
    global b2, b3
    for element in body + b5:
        b8, b7 = fonk4(element)
        if b7 = = "Up" and b2[record][b8 - 1] == 0:
            return False
        elif b7 = = "Down" and b2[record][b8 - 1] == 1:
            return False
        elif b2[record][b8 - 1] != b3.get(b7):
            return False
    return True
def fonk3(record, b5):
    global b2, b3
    for element in b5:
        b8, b7 = fonk4(element)
        if b7 = = "Up" and b2[record][b8 - 1] == 0:
            return False
        elif b7 = = "Down" and b2[record][b8 - 1] == 1:
            return False
        elif b2[record][b8 - 1] != b3.get(b7):
            return False
    return True
def fonk4(element):
    b8 = int(element[0:3])
    b7 = element[4:]
    return b8, b7
def fonk5(b23, a4, unsupported_list_from_previous_iteration):
    for prev in unsupported_list_from_previous_iteration:
        b9 = list(set(b23).intersection(prev))
        if len(b9) == (a4 - 1):
            return False
    return True
def fonk6():
    global a3, b2, b3, a2, b1
    fonk7(b1)
    b10 = fonk8()
    b11 = []
    a4 = 1
    while a4 <= len(b10[0]):
        b21, b12 = fonk9(b10)
        if not b21:
            print(f"No Supported Combinations of a4 equal and greater than {a4}")
            break
        print(f"Supported Combinations of size {a4}: {len(b21)}")
        b11.append(b21)
        b10, a4 = fonk11(b21, b12)
        if not b10:
            print(f"No Combinations of a4 and after {a4}")
            break
    return b11
def fonk7(file_path):
    global a3, b2, b3
    b2.clear()
    a5 = 0
    a3 = 0
    b13 = []
    with open(file_path, 'r') as f:
        for line in f:
            a3 += 1
            b14 = line.strip().split('\t')
            b15 = b14[-1]
            b13.append(b15)
            b14 = b14[:-1]
            a5 = len(b14)
            for index, b16 in enumerate(b14):
                if b16 = = "Down":
                    b14[index] = 0
                elif b16 = = "Up":
                    b14[index] = 1
            b2.append(b14)
    b2 = np.array(b2)
    b17 = sorted(set(b13))
    b18 = list(b17)
    for name in b18:
        b3[name] = b18.index(name)
    b19 = np.zeros((a3, 1))
    b2 = np.hstack((b2, b19))
    a6 = 0
    for x in b13:
        b2[a6][-1] = b3[x]
        a6 += 1
def fonk8():
    global a3
    b10 = []
    for i in range(a3):
        b20 = '{b20:03d}'.format(b20=(i + 1))
        b10.append([b20 + "_Down"])
        b10.append([b20 + "_Up"])
    for x in b3.keys():
        b20 = '{b20:03d}'.format(b20=(a3 + 1))
        b10.append([b20 + "_" + str(x)])
    return sorted(b10)
def fonk9(b10):
    global a3, a2
    b21 = []
    b12 = []
    for current_list in b10:
        a7 = 0
        for record in range(a3):
            b6 = fonk10(record, current_list)
            if b6:
                a7 += 1
                if a7 >= a2:
                    break
        if a7 < a2:
            b12.append(current_list)
        else:
            b21.append(current_list)
    return b21, b12
def fonk10(record, current_list):
    for element in current_list:
        b8, b7 = fonk4(element)
        if b7 = = "Up" and b2[record][b8 - 1] == 0:
            return False
        elif b7 = = "Down" and b2[record][b8 - 1] == 1:
            return False
        elif b2[record][b8 - 1] != b3.get(b7):
            return False
    return True
def fonk11(b21, unsupported_list_from_previous_iteration):
    b10 = []
    a4 = len(b21[0]) + 1
    if a4 != 2:
        for element1_idx, element1 in enumerate(b21):
            for element2_idx in range(element1_idx + 1, len(b21)):
                b22 = b21[element2_idx]
                if fonk12(element1, b22, a4):
                    b23 = list(sorted(set(element1 + b22)))
                    if fonk5(b23, a4, unsupported_list_from_previous_iteration):
                        b10.append(b23)
    else:
        for element1_idx, element1 in enumerate(b21):
            for element2_idx in range(element1_idx + 1, len(b21)):
                b22 = b21[element2_idx]
                b10.append(element1 + b22)
    return b10, a4
def fonk12(element1, b22, a4):
    for i in range(a4 - 2):
        if element1[i] != b22[i]:
            return False
    return True
def fonk13():
    b24 = datetime.now()
    b11 = fonk6()
    return b11
if b25 = = "__main__":
    fonk13()