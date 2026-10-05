import random
import timeit
import matplotlib.pyplot as plt
lista = []
num_elementos = [100,1000,3000,6000,9000,12000,15000,18000,21000,24000]
tempo = []
tempo_ordena = []
def ger_aleatorios(tamanho):
    random.seed()
    global lista
    lista=[]
    i = 0
    while i < l:
        x  = random.randint(1,10*l)
        if x not in lista:
            lista.append(x)
            i += 1
    return lista
def selection_sort(tamanho):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1,len(lista)):
            if(lista[j] < lista[menor]):
                menor = j
        lista[i],lista[menor] = lista[menor],lista[i]
    return lista
for i in num_elementos:
    l = i
    tempo.append(timeit.timeit("ger_aleatorios({})".format(i), setup="from __main__ import ger_aleatorios",number=1))
    tempo_ordena.append(timeit.timeit("selection_sort({})".format(i), setup="from __main__ import selection_sort",number=1))
    print(i)
plt.plot(num_elementos, tempo, '*-', label='Tempo de GeraÃ§Ã£o')
plt.plot(num_elementos, tempo_ordena, 'o-', label='Tempo de OrdenaÃ§Ã£o')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade de elementos')
plt.show()