def fonk1(b5, inicio, fim):
    b1 = inicio
    b2 = fim
    b3 = b5[inicio]
    while b1 < b2:
        while b5[b1] <= b3:
            b1 += 1
            if b1 = = fim:
                break
        while b5[b2] > b3:
            b2 -= 1
            if b2 = = inicio:
                break
        if b1 < b2:
            b5[b1], b5[b2] = b5[b2], b5[b1]
    b5[inicio] = b5[b2]
    b5[b2] = b3
    return b2
def fonk2(b5, inicio, fim):
    if fim > inicio:
        b3 = fonk1(b5, inicio, fim)
        fonk2(b5, inicio, b3 - 1)
        fonk2(b5, b3 + 1, fim)
b4 = int(input("Informe o b4 do seu vetor: "))
print("Insira seus", b4, "elementos: ")
b5 = [int(input()) for _ in range(b4)]
print("Sua b5 ordenada: ")
fonk2(b5, 0, len(b5) - 1)
for num in b5:
    print(num)