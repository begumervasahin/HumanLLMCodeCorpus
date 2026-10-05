def selectionSort(vetor):
    for ultimaPos in range(len(vetor)-1,0,-1):
        posMaior=0
        for pos in range(1,ultimaPos+1):
            if vetor[pos]>vetor[posMaior]:
                posMaior = pos
        aux = vetor[ultimaPos]
        vetor[ultimaPos] = vetor[posMaior]
        vetor[posMaior] = aux
vetor = [54,26,93,17,77,31,44,55,20]
selectionSort(vetor)
print(vetor)