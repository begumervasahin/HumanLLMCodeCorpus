import random
import timeit
import matplotlib.pyplot as plt
lista = []
num_elementos = [100, 1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempo = []
tempo_ordena = []
def gerar_aleatorios(tamanho):
    random.seed()
    global lista
    lista = []
    i = 0
    while i < tamanho:
        x = random.randint(1, 10 * tamanho)
        if x not in lista:
            lista.append(x)
            i += 1
    return lista
def selection_sort(tamanho):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
for i in num_elementos:
    tempo.append(timeit.timeit("gerar_aleatorios({})".format(i), setup="from __main__ import gerar_aleatorios", number=1))
    tempo_ordena.append(timeit.timeit("selection_sort({})".format(i), setup="from __main__ import selection_sort", number=1))
    print(i)
plt.plot(num_elementos, tempo, '*-', label='Tempo de Geração')
plt.plot(num_elementos, tempo_ordena, 'o-', label='Tempo de Ordenação')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade de elementos')
plt.legend()
plt.show()