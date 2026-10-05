import random
import simpy
import math
import matplotlib.pyplot as plt
a1 = 42
a2 = 2
a3 = 2
a4 = 6
a5 = 5
a6 = 10
a7 = 300
b1 = {}
b2 = {}
def fonk1(data):
    b3 = min(data)
    b4 = max(data)
    b5 = sorted(data)
    b6 = len(data)
    b7 = b5[b6
    b8 = sum(data) / b6
    b9 = math.sqrt(sum((x - b8) ** 2 for x in data) / b6)
    b10 = b6
    return [b3, b4, round(b7, 2), round(b8, 2), round(b9, 2), b10]
class class1:
    def fonk2(self, b11, num_doctors):
        self.b11 = b11
        self.b12 = [simpy.Resource(b11, 1) for _ in range(num_doctors)]
    def fonk3(self, patient):
        b13 = random.uniform(a5, a6)
        yield self.b11.timeout(b13)
def fonk4(b11, name, b17, num_queues):
    b14 = b11.now
    b2[name] = b14
    print(f'Patient {name} arrives at the b17 at {b14:.2f}.')
    with b17.b12[random.randint(0, num_queues - 1)].request() as request:
        yield request
        b15 = b11.now - b14
        b16 = b11.now
        yield b11.process(b17.fonk3(name))
        b13 = b11.now - b16
        print(f'Patient {name} enters doctor room after {b15:.2f} time and leaves after spending {b13:.2f} time in doctor room')
        b1[name] = b15
def fonk5(b11, num_doctors, t_inter, num_queue):
    b17 = class1(b11, num_doctors)
    for i in range(4):
        b11.process(fonk4(b11, i, b17, num_queue))
    while True:
        yield b11.timeout(random.randint(t_inter - 2, t_inter + 2))
        b11.process(fonk4(b11, i + 1, b17, num_queue))
def fonk6(data, b8):
    plt.figure(1)
    plt.plot(data, 'r.')
    plt.plot([0, len(data)], [b8, b8], 'c-')
    plt.legend(['Wait time', 'Average wait time'])
    plt.xlabel('Patient Number')
    plt.ylabel('Wait time')
    plt.title("Chart")
    plt.savefig("fig1.png")
    plt.show()
print('class1 Simulation')
random.seed(a1)
b11 = simpy.Environment()
b11.process(fonk5(b11, a3, a4, a2))
b11.run(b18 = a7)
print("Wait Times:", b1)
b19 = list(b1.values())
b20 = list(b2.values())
b21 = fonk1(b19)
b22 = fonk1(b20)
print("\nData:")
print("Doctors\tQueues\tMin\tMax\tMedian\tMean\tStd\tClients in\tClients out")
print(f"{a3}\t{a2}\t{b21[0]}\t{b21[1]}\t{b21[2]}\t{b21[3]}\t{b21[4]}\t{b22[5]}\t{b21[5]}")
fonk6(b19, b21[3])