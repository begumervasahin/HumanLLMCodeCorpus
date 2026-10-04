import matplotlib.pyplot as plt
b1 = [15, 16, 18, 20, 22]
b2 = [0.000281, 0.000301, 0.000350, 0.000365, 0.000381]
b3 = [0.527918, 1.518410, 8.469174, 54.844483, 269.672949]
def fonk1():
    plt.figure(b4 = (10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(b1, b2, "ro-", b5 = "Dynamic Method", color="red")
    plt.ylabel("Time (s)")
    plt.title("Performance Comparison")
    plt.legend(b6 = "lower right")
    plt.subplot(2, 1, 2)
    plt.plot(b1, b3, "ro-", b5 = "Recursive Method", color="red")
    plt.ylabel("Time (s)")
    plt.xlabel("Input Size (M+N)")
    plt.legend(b6 = "upper left")
    plt.tight_layout()
    plt.show()
if b7 = = '__main__':
    fonk1()