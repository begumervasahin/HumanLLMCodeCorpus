import random
import timeit
import matplotlib.pyplot as plt
b1 = []
b2 = [100, 1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
b3 = []
b4 = []
def fonk1(tamanho):
    random.seed()
    global b1
    b1 = []
    a1 = 0
    while a1 < tamanho:
        b5 = random.randint(1, 10 * tamanho)
        if b5 not in b1:
            b1.append(b5)
            a1 += 1
    return b1
def fonk2(tamanho):
    for a1 in range(len(b1)):
        b6 = a1
        for j in range(a1 + 1, len(b1)):
            if b1[j] < b1[b6]:
                b6 = j
        b1[a1], b1[b6] = b1[b6], b1[a1]
    return b1
for tamanho in b2:
    b3.append(timeit.timeit("fonk1({})".format(tamanho), b7 = "from __main__ import gerar_aleatorios", number=1))
    b4.append(timeit.timeit("fonk2({})".format(tamanho), b7 = "from __main__ import selection_sort", number=1))
    print(tamanho)
plt.plot(b2, b3, '*-', b8 = 'Tempo de Geração')
plt.plot(b2, b4, 'o-', b8 = 'Tempo de Ordenação')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade de elementos')
plt.legend()
plt.show()