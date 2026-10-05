import numpy as np
def fonk1(b5):
    b1 = b5.shape[1]
    b2 = np.full((1, b1, b1, b1), fill_value=100)
    for i in range(b1):
        for j in range(b1):
            if i != j:
                if b5[-1, i, i, j] == 100:
                    b2[0, i, j, :] = 100
                else:
                    b2[0, i, j, :] = b5[-1, j, j, :]
            else:
                for b3 in range(b1):
                    if b3 = = i:
                        b2[0, i, i, b3] = 0
                    else:
                        b2[0, i, i, b3] = 100
                        for u in range(b1):
                            b4 = b5[-1, i, i, u] + b5[-1, u, u, b3]
                            if b4 < b2[0, i, i, b3]:
                                b2[0, i, i, b3] = b4
    if not np.array_equal(b5[-1, :, :, :], b2[0, :, :, :]):
        b5 = np.concatenate((b5, b2))
    return b5
def fonk2():
    b1 = int(input("Please enter the number of routers: "))
    b5 = np.full((1, b1, b1, b1), fill_value=100, b7=int)
    for i in range(b1):
        b6 = input("Fill row number %d of the matrix: " % (i + 1))
        b5[0, i] = np.fromstring(b6, b7 = int, sep=' ')
    for j in range(b1):
        b5[0, j, j, :] = b5[0, j, :]
    while True:
        b8 = b5.shape[0]
        b5 = fonk1(b5)
        b9 = b5.shape[0]
        if b9 = = b8:
            break
    b10 = b5.shape[0]
    while True:
        print("\nThere are %d b10 and %d routers.\n" % (b10, b1))
        print("-------------------------------------------------------------")
        b11 = input("Routing finished successfully...\nPlease enter the iteration level you want to take a look at: ")
        b12 = input("Enter router number or enter 'a' for an overall view: ")
        if b12 = = 'a':
            print(b5[int(b11) - 1])
        else:
            print(b5[int(b11) - 1, int(b12) - 1])
        if input("Do you need more report? (Y/N)").lower() == 'n':
            break
if b13 = = "__main__":
    fonk2()