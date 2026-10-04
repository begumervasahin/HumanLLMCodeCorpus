def fonk1(b3):
    for i in range(len(b3)):
        b1 = i + b3[i:].index(min(b3[i:]))
        b3[i], b3[b1] = b3[b1], b3[i]
    return b3
def fonk2():
    b2 = int(input("Enter how many elements you want: "))
    b3 = []
    print("Enter numbers in array: ")
    for _ in range(b2):
        b4 = int(input("b4: "))
        b3.append(b4)
    print("ARRAY:", b3)
    b5 = fonk1(b3)
    print("SORTED ARRAY:", b5)
if b6 = = "__main__":
    fonk2()