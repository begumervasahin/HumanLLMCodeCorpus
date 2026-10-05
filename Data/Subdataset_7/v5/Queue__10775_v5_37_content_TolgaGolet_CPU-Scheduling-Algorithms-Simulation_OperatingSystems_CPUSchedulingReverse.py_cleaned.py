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
    global a6
    for i in range(a2):
        b3 = [i + 1, 0, 0, np.random.randint(1, 3)]
        b2.append(b3)
    a6 = fonk3()
    fonk2()
    print("Process pool successfully created.")
    return a6
def fonk2():
    b4 = np.random.b4(a3, a2)
    for i, burst_time in enumerate(b4):
        b2[i][2] = max(burst_time, 1)
    fonk4(b4, b5 = 'Poisson Burst Times')
def fonk3():
    b6 = np.random.b6(a4, a2)
    for i, exp in enumerate(b6):
        b2[i][1] = max(int(exp), 1)
    fonk4(b6, b5 = 'Exponential Arrival Times')
    return max(b6)
def fonk4(data, b5):
    plt.hist(data)
    plt.b5(b5)
    plt.ylabel('Frequency')
    plt.xlabel('Values')
    plt.tight_layout()
    plt.show()
def fonk5():
    b2.sort(b7 = lambda x: x[1])
plt.figure(1)
a6 = fonk1()
fonk5()
print("Number Of Processes:", a2)
print("Burst Time Lambda:", a3)
print("Arrival Time Scale:", a4)
print("SJF Priority:", a5 * 100, "%")
print("FCFS Priority:", b1 * 100, "%")
print("[processID, arrivalTime, burstTime, b8]  b8 = 1=foreground(SJF), b8=2=batch(FCFS)")
print("Process Pool:", b2)
Processor.start(a5, b1, b2, a6, a1)