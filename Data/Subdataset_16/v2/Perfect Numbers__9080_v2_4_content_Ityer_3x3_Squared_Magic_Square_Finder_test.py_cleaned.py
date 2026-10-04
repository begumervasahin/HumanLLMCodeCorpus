import pickle
def fonk1(lst):
    if lst:
        lst.sort()
        b1 = lst[-1]
        for i in range(len(lst) - 2, -1, -1):
            if b1 = = lst[i]:
                del lst[i]
            else:
                b1 = lst[i]
    return lst
def fonk2():
    b2 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    with open("b2.pkl", 'wb') as file:
        pickle.dump(b2, file)
    with open("b2.pkl", 'rb') as file:
        b2 = pickle.load(file)
    print("Length before removing duplicates:", len(b2))
    b2 = fonk1(b2)
    print("Length after removing duplicates:", len(b2))
if b3 = = '__main__':
    fonk2()