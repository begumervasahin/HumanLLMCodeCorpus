import pickle
def fonk1(L):
    if L:
        L.sort()
        b1 = L[-1]
        for i in range(len(L) - 2, -1, -1):
            if b1 = = L[i]:
                del L[i]
            else:
                b1 = L[i]
    return L
def fonk2():
    b2 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    with open("Fail.txt", 'wb') as f:
        pickle.dump(b2, f)
    with open("Fail.txt", 'rb') as f:
        b2 = pickle.load(f)
    print(len(b2))
    b2 = fonk1(b2)
    print(len(b2))
if b3 = = '__main__':
    fonk2()