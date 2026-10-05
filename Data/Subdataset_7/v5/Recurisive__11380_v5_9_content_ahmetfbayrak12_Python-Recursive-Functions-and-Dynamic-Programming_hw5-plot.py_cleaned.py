import matplotlib.pyplot as plt
def fonk1(b4, b5, b6):
    plt.subplot(211)
    plt.plot(b4, b5, "ro-", b1 = "Dynamic Method", color="red")
    plt.ylabel("Y axis (Time)")
    plt.legend(b2 = "lower right")
    plt.subplot(212)
    plt.plot(b4, b6, "ro-", b1 = "Recursive Method", color="red")
    plt.ylabel("Y axis (Time)")
    plt.xlabel("X axis (M+N)")
    plt.legend(b2 = "upper left")
    plt.show()
if b3 = = "__main__":
    b4 = [15, 16, 18, 20, 22]
    b5 = [0.000281095504761, 0.000301122665405, 0.000349998474121, 0.000365018844604, 0.000380992889404]
    b6 = [0.527917861938, 1.51841020584, 8.46917390823, 54.8444831371, 269.672949076]
    fonk1(b4, b5, b6)