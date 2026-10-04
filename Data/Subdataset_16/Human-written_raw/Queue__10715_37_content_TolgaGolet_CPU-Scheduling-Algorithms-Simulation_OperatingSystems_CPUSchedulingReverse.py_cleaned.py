import numpy as np
import matplotlib.pyplot as plt
import Processor
a1 = 0.1
a2 = 15
a3 = 3
a4 = 15.0
a5 = 0.6
b1 = 1 - a5
a6 = 0
b2 = []
def fonk1():
    print("Creating the b3 pool...")
    for i in range(a2):
        b3 = [i+1, 0, 0, np.random.randint(1, 3)]
        b2.append(b3)
    a6 = fonk3()
    fonk2()
    print("Process pool successfully created.")
    return a6
def fonk2():
    b4 = np.random.b4(a3, a2)
    for i, a7 in zip(range(a2+1), b4):
        if a7 <= 0:
            a7 = 1
        b2[i][2] = a7
    plt.subplot(2, 1, 1)
    plt.hist(b4)
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def fonk3():
    b5 = np.random.b5(a4, a2)
    for i, exp in zip(range(a2+1), b5):
        if int(exp) <= 0:
            a8 = 1
        else:
            a8 = int(exp)
        b2[i][1] = a8
    plt.subplot(2, 1, 2)
    plt.hist(b5)
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return max(b5)
def fonk4():
    def fonk5(elem):
        return elem[1]
    b2.sort(b6 = sortByArrivalTime)
plt.figure(1)
a6 = fonk1()
fonk4()
print("Number Of Processes: ", a2)
print("Burst Time Lambda: ", a3)
print("Arrival Time Scale: ", a4)
print("SJF Priority: ", a5 * 100, "%")
print("FCFS Priority: ", b1 * 100, "%")
print("[processID, a8, a7, b7]   b7 = 1=foreground(SJF), b7=2=batch(FCFS)")
print("Process Pool: ", b2)
Processor.start(a5, b1, b2, a6, a1)