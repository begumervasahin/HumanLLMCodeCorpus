import random
a1 = 0
''' merge sort script '''
def fonk1(lst):
    global a1
    if len(lst) <= 1:
        a1 += 1
        return lst
    b1 = len(lst)
    b2 = fonk1(lst[:b1])
    b3 = fonk1(lst[b1:])
    return fonk2(b2, b3)
def fonk2(b2, b3):
    global a1
    b4 = []
    a2 = 0
    a3 = 0
    while a2 < len(b2) and a3 < len(b3):
        if b2[a2] < b3[a3]:
            a1 += 1
            b4.append(b2[a2])
            a2+=1
        else:
            b4.append(b3[a3])
            a3+=1
    a1 += 1
    b4 += b2[a2:]
    b4 += b3[a3:]
    return b4
b5 = [line.rstrip('\n') for line in open('words.txt')]
b6 = len(b5)
print(b6)
''' All below this is to test on various inputs '''
''' Testing on 10 words '''
print('-------------')
print('Testing on 10 words')
print('10 words sorted')
b7 = b5[0:10]
fonk1(b7)
print('number of comparisons:', a1)
print('10 words reversed')
b8 = list(reversed(b7))
fonk1(b8)
print('number of comparisons:', a1)
print('10 words random')
b9 = random.randint(0,80000)
b10 = b5[b9:b9+10]
random.shuffle(b10)
fonk1(b10)
print('number of comparisons:', a1)
print('-------------')
print('')
'''Testing on 30 words '''
print('-------------')
print('Testing on 30 words')
print('30 words sorted')
b11 = b5[0:30]
fonk1(b11)
print('number of comparisons:', a1)
print('30 words reversed')
b12 = list(reversed(b11))
fonk1(b12)
print('number of comparisons:', a1)
print('30 words random')
b13 = random.randint(0,80000)
b14 = b5[b13:b13+30]
random.shuffle(b14)
fonk1(b14)
print('number of comparisons:', a1)
print('-------------')
print('')
'''Testing on 100 words '''
print('-------------')
print('Testing on 100 words')
print('100 words sorted')
b15 = b5[0:100]
fonk1(b15)
print('number of comparisons:', a1)
print('100 words reversed')
b16 = list(reversed(b15))
fonk1(b16)
print('number of comparisons:', a1)
print('100 words random')
b17 = random.randint(0,80000)
b18 = b5[b17:b17+100]
random.shuffle(b18)
fonk1(b14)
print('number of comparisons:', a1)
print('-------------')
print('')
'''Testing on 300 words '''
print('-------------')
print('Testing on 300 words')
print('300 words sorted')
b19 = b5[0:300]
fonk1(b19)
print('number of comparisons:', a1)
print('300 words reversed')
b20 = list(reversed(b19))
fonk1(b20)
print('number of comparisons:', a1)
print('300 words random')
b21 = random.randint(0,80000)
b22 = b5[b21:b21+300]
random.shuffle(b22)
fonk1(b22)
print('number of comparisons:', a1)
print('-------------')
print('')
'''Testing on 1000 words'''
print('-------------')
print('Testing on 1000 words')
print('1000 words sorted')
b23 = b5[0:1000]
fonk1(b23)
print('number of comparisons:', a1)
print('1000 words reversed')
b24 = list(reversed(b23))
fonk1(b24)
print('number of comparisons:', a1)
print('1000 words random')
b25 = random.randint(0,80000)
b26 = b5[b25:b25+1000]
random.shuffle(b26)
fonk1(b26)
print('number of comparisons:', a1)
print('-------------')
print('')
'''Testing on 3000 words'''
print('-------------')
print('Testing on 3000 words')
print('3000 words sorted')
b27 = b5[0:3000]
fonk1(b27)
print('number of comparisons:', a1)
print('3000 words reversed')
b28 = list(reversed(b27))
fonk1(b28)
print('number of comparisons:', a1)
print('3000 words random')
b29 = random.randint(0,77000)
b30 = b5[b29:b29+3000]
random.shuffle(b30)
fonk1(b30)
print('number of comparisons:', a1)
print('-------------')
print('')
'''Testing on 10000 words '''
print('-------------')
print('Testing on 10000 words')
print('10000 words sorted')
b31 = b5[0:10000]
fonk1(b31)
print('number of comparisons:', a1)
print('10000 words reversed')
b32 = list(reversed(b31))
fonk1(b32)
print('number of comparisons:', a1)
print('10000 words random')
b33 = random.randint(0,70000)
b34 = b5[b29:b29+10000]
random.shuffle(b34)
fonk1(b34)
print('number of comparisons:', a1)
print('-------------')
print('')
''' Testing on all words '''
print('-------------')
print('Testing on all words')
print('all words sorted')
b35 = b5[0:len(b5)]
fonk1(b35)
print('number of comparisons:', a1)
print('all words reversed')
b36 = list(reversed(b35))
fonk1(b36)
print('number of comparisons:', a1)
print('all words random')
random.shuffle(b35)
fonk1(b35)
print('number of comparisons:', a1)
print('-------------')