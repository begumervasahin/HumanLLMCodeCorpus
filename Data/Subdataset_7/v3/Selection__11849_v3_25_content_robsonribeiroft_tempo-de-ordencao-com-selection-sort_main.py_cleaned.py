import random
import timeit
import matplotlib.pyplot as plt
b1 = []
b2 = [100, 1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
b3 = []
b4 = []
def fonk1(tamanho):
    random.seed()
    return random.sample(range(1, 10 * tamanho + 1), tamanho)
def fonk2(tamanho):
    b5 = b1[:tamanho]
    for i in range(len(b5)):
        b6 = i
        for j in range(i + 1, len(b5)):
            if b5[j] < b5[b6]:
                b6 = j
        b5[i], b5[b6] = b5[b6], b5[i]
    return b5
for i in b2:
    b3.append(timeit.timeit("fonk1({})".format(i), b7 = "from __main__ import gerar_aleatorios", number=1))
    b4.append(timeit.timeit("fonk2({})".format(i), b7 = "from __main__ import selection_sort", number=1))
    print(i)
plt.plot(b2, b3, '*-', b8 = 'Tempo de Geração')
plt.plot(b2, b4, 'o-', b8 = 'Tempo de Ordenação')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade de elementos')
plt.legend()
plt.show()