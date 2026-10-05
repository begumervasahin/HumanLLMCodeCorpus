import numpy as np
def fonk1(b4, b5):
    b1 = np.full((1, b5, b5, b5), 100)
    for i in range(b5):
        for j in range(b5):
            if i != j:
                if b4[-1, i, i, j] == 100:
                    b1[0, i, j, :] = 100
                else:
                    b1[0, i, j, :] = b4[-1, j, j, :]
            else:
                for b2 in range(b5):
                    if b2 = = i:
                        b1[0, i, i, b2] = 0
                    else:
                        b1[0, i, i, b2] = 100
                        for u in range(b5):
                            b3 = b4[-1, i, i, u] + b4[-1, u, u, b2]
                            if b3 < b1[0, i, i, b2]:
                                b1[0, i, i, b2] = b3
    if not np.array_equal(b4[-1, :, :, :], b1[0, :, :, :]):
        b4 = np.concatenate((b4, b1))
    return b4
def fonk2():
    print("Welcome to the router routing system!")
    b5 = int(input("Please enter the number of routers: "))
    b6 = np.full((1, b5, b5, b5), 100, b9=int)
    b7 = np.full((b5, b5), 100, b9=int)
    for i in range(b5):
        b8 = input("Fill row number %d of the matrix: " % (i + 1))
        b7[i] = np.fromstring(b8, b9 = int, sep=' ')
    for j in range(b5):
        b6[0, j, j, :] = b7[j, :]
    while True:
        b10 = b6.shape[0]
        b6 = fonk1(b6, b5)
        b11 = b6.shape[0]
        if b11 = = b10:
            break
    b12 = b6.shape[0]
    print("\nRouting finished successfully after %d b12." % b12)
    while True:
        print("\nThere are %d b12 and %d routers.\n" % (b12, b5))
        print("-------------------------------------------------------------")
        b13 = input("Please enter the iteration level you want to take a look at: ")
        b14 = input("Enter router number or enter 'a' for an overall view: ")
        if b14 = = 'a':
            print(b6[int(b13) - 1])
        else:
            print(b6[int(b13) - 1, int(b14) - 1])
        if input("Do you need more report? (Y/N)").lower() == 'n':
            break
if b15 = = "__main__":
    fonk2()