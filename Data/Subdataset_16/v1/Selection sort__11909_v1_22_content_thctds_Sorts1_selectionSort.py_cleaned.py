def fonk1(b2):
    for i in range(len(b2)):
        b1 = i
        for j in range(i+1, len(b2)):
            if b2[j] < b2[b1]:
                b1 = j
        b2[i], b2[b1] = b2[b1], b2[i]
    return b2
def fonk2():
    b2 = []
    b3 = int(input("Enter how many elements you want: "))
    print('Enter numbers in array: ')
    for i in range(b3):
        b4 = int(input("b3: "))
        b2.append(b4)
    print('ARRAY:', b2)
    b5 = fonk1(b2)
    print('SORTED ARRAY:', b5)
if b6 = = "__main__":
    fonk2()