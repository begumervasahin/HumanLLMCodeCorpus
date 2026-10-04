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
        b3 = [i + 1, 0, 0, np.random.randint(1, 3)]
        b2.append(b3)
    b4 = fonk3()
    fonk2()
    print("Process pool successfully created.")
    return b4
def fonk2():
    b5 = np.random.poisson(a3, a2)
    for i, burst_time in enumerate(b5):
        b2[i][2] = max(1, burst_time)
    plt.subplot(2, 1, 1)
    plt.hist(b5, b6 = range(min(b5), max(b5) + 1), align='left')
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def fonk3():
    b7 = np.random.exponential(a4, a2)
    for i, arrival_time in enumerate(b7):
        b2[i][1] = max(1, int(arrival_time))
    plt.subplot(2, 1, 2)
    plt.hist(b7, b6 = 30)
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return max(b7)
def fonk4():
    b2.sort(b8 = lambda elem: elem[1])
def fonk5():
    print("Number Of Processes:", a2)
    print("Burst Time Lambda:", a3)
    print("Arrival Time Scale:", a4)
    print("SJF Priority:", a5 * 100, "%")
    print("FCFS Priority:", b1 * 100, "%")
    print("[processID, arrivalTime, burstTime, b9]   b9 = 1=foreground(SJF), b9=2=batch(FCFS)")
    print("Process Pool:", b2)
def fonk6():
    plt.figure(1)
    b4 = fonk1()
    fonk4()
    fonk5()
    Processor.start(a5, b1, b2, b4, a1)
    plt.show()
if b10 = = "__main__":
    fonk6()