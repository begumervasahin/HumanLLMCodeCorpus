import numpy as np
def fonk1(b4, b8):
    b1 = np.full((1, b8, b8, b8), 100)
    for i in range(b8):
        for j in range(b8):
            if i != j:
                if b4[-1, i, i, j] == 100:
                    b1[0, i, j, :] = 100
                else:
                    b1[0, i, j, :] = b4[-1, j, j, :]
            else:
                for b2 in range(b8):
                    if b2 = = i:
                        b1[0, i, i, b2] = 0
                    else:
                        b1[0, i, i, b2] = 100
                        for u in range(b8):
                            b3 = b4[-1, i, i, u] + b4[-1, u, u, b2]
                            if b3 < b1[0, i, i, b2]:
                                b1[0, i, i, b2] = b3
    if not np.array_equal(b4[-1, :, :, :], b1[0, :, :, :]):
        b4 = np.concatenate((b4, b1))
    return b4
def fonk2(b8):
    b5 = np.full((b8, b8), 100, b7=int)
    for i in range(b8):
        b6 = input("Fill row number %d of the matrix: " % (i + 1))
        b5[i] = np.fromstring(b6, b7 = int, sep=' ')
    return b5
def fonk3():
    print("Welcome to the router routing system!")
    b8 = int(input("Please enter the number of routers: "))
    b9 = np.full((1, b8, b8, b8), 100, b7=int)
    b5 = fonk2(b8)
    for j in range(b8):
        b9[0, j, j, :] = b5[j, :]
    while True:
        b10 = b9.shape[0]
        b9 = fonk1(b9, b8)
        b11 = b9.shape[0]
        if b11 = = b10:
            break
    b12 = b9.shape[0]
    print("\nRouting finished successfully after %d b12." % b12)
    while True:
        print("\nThere are %d b12 and %d routers.\n" % (b12, b8))
        print("-------------------------------------------------------------")
        b13 = input("Please enter the iteration level you want to take a look at: ")
        b14 = input("Enter router number or enter 'a' for an overall view: ")
        if b14 = = 'a':
            print(b9[int(b13) - 1])
        else:
            print(b9[int(b13) - 1, int(b14) - 1])
        if input("Do you need more report? (Y/N)").lower() == 'n':
            break
if b15 = = "__main__":
    fonk3()