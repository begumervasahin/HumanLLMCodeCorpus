import pickle
def fonk1(lst):
    if lst:
        lst.sort()
        b1 = [lst[-1]]
        for i in range(len(lst) - 2, -1, -1):
            if lst[i] != b1[0]:
                b1.insert(0, lst[i])
        return b1
    return lst
with open("Fail.txt", 'rb') as file:
    b2 = pickle.load(file)
print("Original length:", len(b2))
b2 = fonk1(b2)
print("Length after removing duplicates:", len(b2))