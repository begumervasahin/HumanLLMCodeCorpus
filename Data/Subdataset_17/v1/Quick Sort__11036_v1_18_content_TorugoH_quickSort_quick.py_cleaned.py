def particionar(lista, inicio, fim):
    esquerda = inicio
    direita = fim
    aux = 0
    pivo = lista[inicio]
    while esquerda < direita:
        while esquerda < len(lista) and lista[esquerda] <= pivo:
            esquerda += 1
        while lista[direita] > pivo:
            direita -= 1
        if esquerda < direita:
            aux = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = aux
    lista[inicio] = lista[direita]
    lista[direita] = pivo
    return direita
def quick(lista, inicio, fim):
    if fim > inicio:
        pivo = particionar(lista, inicio, fim)
        quick(lista, inicio, pivo - 1)
        quick(lista, pivo + 1, fim)
if __name__ == "__main__":
    lista = []
    print("Informe o tamanho do seu vetor:")
    tamanho = int(input())
    print(f"Insira os seus {tamanho} elementos:")
    for i in range(tamanho):
        numero = int(input())
        lista.append(numero)
    print("Sua lista ordenada:")
    quick(lista, 0, len(lista) - 1)
    for i in range(len(lista)):
        print(lista[i])