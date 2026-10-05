import numpy as np
import matplotlib.pyplot as plt
def fonk1(a5, a6, a7, a8):
    a1 = 0.1
    a2 = 0
    b1 = []
    print("Creating the b2 pool...")
    for i in range(a5):
        b2 = [i+1, 0, 0, np.random.randint(1, 3)]
        b1.append(b2)
    a2 = fonk3(b1, a5, a7)
    fonk2(b1, a5, a6)
    print("Process pool successfully created.")
    fonk4(b1)
    print("Number Of Processes: ", a5)
    print("Burst Time Lambda: ", a6)
    print("Arrival Time Scale: ", a7)
    print("SJF Priority: ", a8 * 100, "%")
    print("FCFS Priority: ", (1 - a8) * 100, "%")
    print("[processID, arrivalTime, burstTime, b3]   b3 = 1=foreground(SJF), b3=2=batch(FCFS)")
    print("Process Pool: ", b1)
def fonk2(b1, a5, a6):
    b4 = np.random.b4(a6, a5)
    for i, a3 in zip(range(a5), b4):
        if a3 <= 0:
            a3 = 1
        b1[i][2] = a3
    plt.subplot(2, 1, 1)
    plt.hist(b4)
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def fonk3(b1, a5, a7):
    b5 = np.random.b5(a7, a5)
    a2 = 0
    for i, exp in zip(range(a5), b5):
        if int(exp) <= 0:
            a4 = 1
        else:
            a4 = int(exp)
        b1[i][1] = a4
        if exp > a2:
            a2 = exp
    plt.subplot(2, 1, 2)
    plt.hist(b5)
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return a2
def fonk4(b1):
    b1.sort(b6 = lambda x: x[1])
if b7 = = "__main__":
    a5 = 15
    a6 = 3
    a7 = 15.0
    a8 = 0.6
    fonk1(a5, a6, a7, a8)