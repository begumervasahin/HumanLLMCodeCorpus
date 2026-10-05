def partition(lista, inicio, fim):
    esquerda = inicio
    direita = fim
    pivo = lista[inicio]
    while esquerda < direita:
        while lista[esquerda] <= pivo:
            esquerda += 1
            if esquerda == fim:
                break
        while lista[direita] > pivo:
            direita -= 1
            if direita == inicio:
                break
        if esquerda < direita:
            lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
    lista[inicio] = lista[direita]
    lista[direita] = pivo
    return direita
def quick(lista, inicio, fim):
    if fim > inicio:
        pivo = partition(lista, inicio, fim)
        quick(lista, inicio, pivo - 1)
        quick(lista, pivo + 1, fim)
tamanho = int(input("Informe o tamanho do seu vetor: "))
print("Insira seus", tamanho, "elementos: ")
lista = [int(input()) for _ in range(tamanho)]
print("Sua lista ordenada: ")
quick(lista, 0, len(lista) - 1)
for num in lista:
    print(num)