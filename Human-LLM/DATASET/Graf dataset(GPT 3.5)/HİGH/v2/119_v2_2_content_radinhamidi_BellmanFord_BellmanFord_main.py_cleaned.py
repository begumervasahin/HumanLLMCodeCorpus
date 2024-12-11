import numpy as np
def fonk1(b4):
    b1 = b4.shape[1]
    b2 = np.full((1, b1, b1, b1), 100)
    for i in range(b1):
        for j in range(b1):
            if i != j:
                if b4[-1, i, i, j] == 100:
                    b2[0, i, j, :] = 100
                else:
                    b2[0, i, j, :] = b4[-1, j, j, :]
            else:
                for b3 in range(b1):
                    if b3 = = i:
                        b2[0, i, i, b3] = 0
                    else:
                        b2[0, i, i, b3] = 100
                        for u in range(b1):
                            if (b4[-1, i, i, u] + b4[-1, u, u, b3]) < b2[0, i, i, b3]:
                                b2[0, i, i, b3] = (b4[-1, i, i, u] + b4[-1, u, u, b3])
    if not np.array_equal(b4[-1, :, :, :], b2[0, :, :, :]):
        b4 = np.concatenate((b4, b2))
    return b4
def fonk2():
    b1 = int(input("Please enter the number of routers: "))
    b4 = np.full((1, b1, b1, b1), 100, int)
    for i in range(b1):
        b5 = input("Fill row number %d of the matrix: " % (i + 1))
        b4[0, i] = np.fromstring(b5, b6 = int, sep=' ')
    for j in range(b1):
        b4[0, j, j, :] = b4[0, j, :]
    while True:
        b7 = b4.shape[0]
        b4 = fonk1(b4)
        b8 = b4.shape[0]
        if b8 = = b7:
            break
    b9 = b4.shape[0]
    while True:
        print("\nThere are %d b9 and %d routers.\n" % (b9, b1))
        print("-------------------------------------------------------------")
        b10 = input("Routing finished successfully...\nPlease enter the iteration level you want to take a look at: ")
        b11 = input("Enter router number or enter 'a' for an overall view: ")
        if b11 = = 'a':
            print(b4[int(b10) - 1])
        else:
            print(b4[int(b10) - 1, int(b11) - 1])
        if input("Do you need more report? (Y/N)").lower() == 'n':
            break
if b12 = = "__main__":
    fonk2()