import random
import timeit
import matplotlib.pyplot as plt
b1 = []
b2 = [100,1000,3000,6000,9000,12000,15000,18000,21000,24000]
b3 = []
b4 = []
def fonk1(tamanho):
    random.seed()
    global b1
    b1 = []
    a1 = 0
    while a1 < b7:
        b5 = random.randint(1,10*b7)
        if b5 not in b1:
            b1.append(b5)
            a1 += 1
    return b1
def fonk2(tamanho):
    for a1 in range(len(b1)):
        b6 = a1
        for j in range(a1+1,len(b1)):
            if(b1[j] < b1[b6]):
                b6 = j
        b1[a1],b1[b6] = b1[b6],b1[a1]
    return b1
for a1 in b2:
    b7 = a1
    b3.append(timeit.timeit("fonk1({})".format(a1), b8 = "from __main__ import ger_aleatorios",number=1))
    b4.append(timeit.timeit("fonk2({})".format(a1), b8 = "from __main__ import selection_sort",number=1))
    print(a1)
plt.plot(b2, b3, '*-', b9 = 'Tempo de GeraÃ§Ã£o')
plt.plot(b2, b4, 'o-', b9 = 'Tempo de OrdenaÃ§Ã£o')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade de elementos')
plt.show()