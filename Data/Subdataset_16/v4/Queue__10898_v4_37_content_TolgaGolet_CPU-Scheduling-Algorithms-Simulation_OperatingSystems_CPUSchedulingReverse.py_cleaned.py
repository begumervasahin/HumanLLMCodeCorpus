import numpy as np
import matplotlib.pyplot as plt
import Processor
a1 = 0.1
a2 = 15
a3 = 3
a4 = 15.0
a5 = 0.6
b1 = 1 - a5
b2 = []
def fonk1():
    print("Creating the b3 pool...")
    for i in range(a2):
        b3 = [i+1, 0, 0, np.random.randint(1, 3)]
        b2.append(b3)
    b4 = fonk3()
    fonk2()
    print("Process pool successfully created.")
    return b4
def fonk2():
    b5 = np.random.b5(a3, a2)
    for i, a6 in enumerate(b5):
        if a6 <= 0:
            a6 = 1
        b2[i][2] = a6
    plt.subplot(2, 1, 1)
    plt.hist(b5, b6 = range(min(b5), max(b5) + 1))
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def fonk3():
    b7 = np.random.b7(a4, a2)
    for i, exp in enumerate(b7):
        b8 = max(1, int(exp))
        b2[i][1] = b8
    plt.subplot(2, 1, 2)
    plt.hist(b7, b6 = 30)
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return max(b7)
def fonk4():
    b2.sort(b9 = lambda elem: elem[1])
def fonk5():
    plt.figure(1)
    b4 = fonk1()
    fonk4()
    print("Number Of Processes:", a2)
    print("Burst Time Lambda:", a3)
    print("Arrival Time Scale:", a4)
    print("SJF Priority:", a5 * 100, "%")
    print("FCFS Priority:", b1 * 100, "%")
    print("[processID, arrivalTime, burstTime, b10]   b10 = 1=foreground(SJF), b10=2=batch(FCFS)")
    print("Process Pool:", b2)
    Processor.start(a5, b1, b2, b4, a1)
    plt.show()
if b11 = = "__main__":
    fonk5()