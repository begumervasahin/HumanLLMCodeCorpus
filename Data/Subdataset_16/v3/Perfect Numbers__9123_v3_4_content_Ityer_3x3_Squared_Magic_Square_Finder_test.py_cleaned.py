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
def fonk2(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
def fonk3(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
def fonk4():
    b2 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    fonk2(b2, "b2.pkl")
    b2 = fonk3("b2.pkl")
    print("Length before removing duplicates:", len(b2))
    b2 = fonk1(b2)
    print("Length after removing duplicates:", len(b2))
if b3 = = '__main__':
    fonk4()