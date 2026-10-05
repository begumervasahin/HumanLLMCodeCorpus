def fonk1(b5,inicio,fim):
    b1 = inicio
    b2 = fim
    a1 = 0
    b3 = b5[inicio]
    while(b1<b2):
        if(b5[b1]<=b3):
            b1 = b1+1
        while(b5[b2]>b3):
            b2 = b2-1
        if(b1<b2):
            b4 = b5[b1]
            b5[b1]=b5[b2]
            b5[b2]=b4
    b5[inicio]=b5[b2]
    b5[b2]=b3
    return b2
def fonk2(b5,inicio,fim):
    b3 = 0
    if(fim>inicio):
        b3 = fonk1(b5,inicio,fim)
        fonk2(b5,inicio,b3-1)
        fonk2(b5,b3+1,fim)
a2 = 0
b5 = []
a3 = 0
a4 = 0
print("informe o a2 do seu vetor")
a2 = int(input())
print("Insira o seus",a2,"elementos ")
while (a4<a2):
    a3 = int(input())
    b5.append(a3)
    a4+=1
print("Sua b5 ordenada: ")
fonk2(b5,0,len(b5)-1)
for a4 in range(0,len(b5)):
    print(b5[a4])