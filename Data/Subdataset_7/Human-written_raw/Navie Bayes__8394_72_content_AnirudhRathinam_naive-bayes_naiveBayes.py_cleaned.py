b1 = []
b2 = []
b3 = []
a1 = 0
a2 = 0
b4 = []
b5 = []
b6 = []
b7 = input('\nPlease input name of training dataset (with file extension): ')
b8 = input('\nPlease input name of b8 dataset (with file extension): ')
with open(b7, 'r') as file:
    b9 = file.readline()
    for i in b9.split()[:-1]:
        b2.append(i)
    a2 = len(b2)
    for l in file:
        a1+=1
        b1.append(l.split()[a2])
        b3.append(l.split())
b10 = (b1.count('0'))/len(b1)
b11 = (b1.count('1'))/len(b1)
for i in range (0, a2):
    b6 = [b14[i] for b14 in b3]
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    for a9 in range(0, a1):
        if(b6[a9] == '0'):
            a7 = a7+1
            if(b1[a9] == '0'):
                a3 = a3 + 1
            else:
                a4 = a4 + 1
        if(b6[a9] == '1'):
            a8 = a8 + 1
            if(b1[a9] == '1'):
                a6 = a6 + 1
            else:
                a5 = a5 + 1
    b4.append((a3/a7))
    b4.append((a4/a7))
    b5.append((a5/a8))
    b5.append((a6/a8))
a9 = 0
print('P(b12 = 0): ' + str(b10))
for i in range (0, a2):
    print('P('+ b2[i] + ' = 0|b13 = 0): '+ str("%.2f" % b4[a9]) + ' P(' + b2[i] + ' = 1|b13 = 0): '+ str("%.2f" % b4[a9+1]), end = ' ')
    a9 = a9 + 2
print('\n\n')
a9 = 0
print('P(b12 = 1): ' + str(b11))
for i in range (0, a2):
    print('P('+ b2[i] + ' = 0|b13 = 1): '+ str("%.2f" % b5[a9]) + ' P(' + b2[i] + ' = 1|b13 = 1): '+ str("%.2f" % b5[a9+1]), end = ' ')
    a9 = a9 + 2
def fonk1(b14, b4, b5, b10, b11):
    b14 = list(map(int, b14))
    b15 = b10
    b16 = b11
    for i in range (0, len(b14)-1):
        a9 = i*2
        if(b14[i] == 0):
            b15 = b15*b4[a9]
            b16 = b16*b5[a9]
        else:
            b15 = b15*b4[a9+1]
            b16 = b16*b5[a9+1]
    if(b16 > b15):
        return('1')
    else:
        return('0')
a10 = 0
for i in range(0, a1):
    b13 = fonk1(b3[i], b4, b5, b10, b11)
    if(b13 = = b1[i]):
        a10 = a10+1
print('\n\nAccuracy on training set (' + str(a1) + ' instances) is: ' + str("%.2f" % ((a10/a1)*100)))
b1 = []
b2 = []
b3 = []
a1 = 0
a2 = 0
with open(b8, 'r') as file:
    b9 = file.readline()
    for i in b9.split()[:-1]:
        b2.append(i)
    a2 = len(b2)
    for l in file:
        a1+=1
        b1.append(l.split()[a2])
        b3.append(l.split())
a10 = 0
for i in range(0, a1):
    b13 = fonk1(b3[i], b4, b5, b10, b11)
    if(b13 = = b1[i]):
        a10 = a10+1
print('\n\nAccuracy on b8 set (' + str(a1) + ' instances) is: ' + str("%.2f" % ((a10/a1)*100)))