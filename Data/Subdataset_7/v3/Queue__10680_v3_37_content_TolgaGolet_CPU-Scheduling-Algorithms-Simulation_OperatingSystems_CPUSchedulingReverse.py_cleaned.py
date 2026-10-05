import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, a2, a3, a4):
    b1 = fonk2(a1)
    b2 = fonk3(b1, a1, a3, a2)
    fonk4(b1)
    fonk5(a1, a2, a3, a4, b1)
    fonk6(b1)
def fonk2(a1):
    b1 = []
    for i in range(a1):
        b1.append([i+1, 0, 0, np.random.randint(1, 3)])
    return b1
def fonk3(b1, a1, a3, a2):
    b2 = 0
    for process in b1:
        b3 = np.random.exponential(a3)
        b4 = max(1, int(b3))
        process[1] = b4
        b2 = max(b2, b3)
        b5 = max(1, np.random.poisson(a2))
        process[2] = b5
    return b2
def fonk4(b1):
    b1.sort(b6 = lambda x: x[1])
def fonk5(a1, a2, a3, a4, b1):
    print("Creating the process pool...")
    print("Number Of Processes:", a1)
    print("Burst Time Lambda:", a2)
    print("Arrival Time Scale:", a3)
    print("SJF Priority:", a4 * 100, "%")
    print("FCFS Priority:", (1 - a4) * 100, "%")
    print("[processID, arrivalTime, burstTime, b7]   b7 = 1=foreground(SJF), b7=2=batch(FCFS)")
    print("Process Pool:", b1)
def fonk6(b1):
    plt.figure(b8 = (10, 8))
    plt.subplot(2, 1, 1)
    plt.hist([process[2] for process in b1])
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
    plt.subplot(2, 1, 2)
    plt.hist([process[1] for process in b1])
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    plt.tight_layout()
    plt.show()
if b9 = = "__main__":
    a1 = 15
    a2 = 3
    a3 = 15.0
    a4 = 0.6
    fonk1(a1, a2, a3, a4)