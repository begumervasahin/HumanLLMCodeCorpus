def fonk1(b5, inicio, fim):
    b1 = inicio
    b2 = fim
    a1 = 0
    b3 = b5[inicio]
    while b1 < b2:
        while b1 < len(b5) and b5[b1] <= b3:
            b1 += 1
        while b5[b2] > b3:
            b2 -= 1
        if b1 < b2:
            a1 = b5[b1]
            b5[b1] = b5[b2]
            b5[b2] = a1
    b5[inicio] = b5[b2]
    b5[b2] = b3
    return b2
def fonk2(b5, inicio, fim):
    if fim > inicio:
        b3 = fonk1(b5, inicio, fim)
        fonk2(b5, inicio, b3 - 1)
        fonk2(b5, b3 + 1, fim)
if b4 = = "__main__":
    b5 = []
    print("Informe o b6 do seu vetor:")
    b6 = int(input())
    print(f"Insira os seus {b6} elementos:")
    for i in range(b6):
        b7 = int(input())
        b5.append(b7)
    print("Sua b5 ordenada:")
    fonk2(b5, 0, len(b5) - 1)
    for i in range(len(b5)):
        print(b5[i])