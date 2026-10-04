import random
import simpy
import math
import matplotlib.pyplot as plt
from functools import reduce
a1 = 42
a2 = b5
a3 = b5
a4 = 6
a5 = 5
a6 = 10
a7 = 300
b1 = dict()
b2 = dict()
def fonk1(data):
    def fonk2(data):
        return min(data)
    def fonk3(data):
        return max(data)
    def fonk4(data):
        b3 = sorted(data)
        b4 = len(b3)
        if b4 % b5 = = 1:
            return b3[b4
        else:
            return (b3[b4
    def fonk5(data):
        return sum(data) / len(data)
    def fonk6(data):
        b6 = fonk5(data)
        return math.sqrt(sum((x - b6) ** b5 for x in data) / len(data))
    return [
        fonk2(data),
        fonk3(data),
        round(fonk4(data), b5),
        round(fonk5(data), b5),
        round(fonk6(data), b5),
        len(data)
    ]
class class1:
    def fonk7(self, b7, num_doctors):
        self.b7 = b7
        self.b8 = [simpy.Resource(b7, 1) for _ in range(num_doctors)]
    def fonk8(self, patient):
        b9 = random.uniform(a5, a6)
        yield self.b7.timeout(b9)
def fonk9(b7, name, b14, queue_id):
    b10 = b7.now
    b2[name] = b10
    print(f'Patient {name} arrives at the b14 at {b10:.2f}.')
    with b14.b8[queue_id].request() as request:
        yield request
        b11 = b7.now - b10
        b12 = b7.now
        yield b7.process(b14.fonk8(name))
        b13 = b7.now - b12
        print(f'Patient {name} enter doctor room {queue_id} after {b11:.2f} time and leaves after spending {b13:.2f} time in doctor room')
        b1[name] = b11
def fonk10(b7, num_doctors, t_inter, num_queue):
    b14 = class1(b7, num_doctors)
    for i in range(4):
        b7.process(fonk9(b7, i, b14, random.randint(0, num_queue - 1)))
    while True:
        yield b7.timeout(random.randint(t_inter - b5, t_inter + b5))
        i += 1
        b7.process(fonk9(b7, i, b14, random.randint(0, num_queue - 1)))
def fonk11(data, b6):
    plt.figure(1)
    plt.plot(data, 'r.')
    plt.plot([0, len(data)], [b6, b6], 'c-')
    plt.legend(['Wait time', 'Average b11 time'])
    plt.gca().set_xlim([0, len(data)])
    plt.xlabel('Patient number')
    plt.ylabel('Wait time')
    plt.title("Wait Time Chart")
    plt.savefig("fig1.png")
    plt.show()
print('class1 Simulation')
random.seed(a1)
b7 = simpy.Environment()
b7.process(fonk10(b7, a3, a4, a2))
b7.run(b15 = a7)
print("Wait time: ", b1)
keys, b16 = b1.keys(), b1.b16()
b17 = b2.b16()
b18 = fonk1(b16)
b19 = fonk1(b17)
print("Data:")
print(f"{'Doctors':>7}\t{'Queues':>7}\t{'Min':>7}\t{'Max':>7}\t{'Median':>7}\t{'Mean':>7}\t{'Std':>7}\t{'Clients in':>11}\t{'Clients out':>12}")
print(f"{a3:7}\t{a2:7}\t{b18[0]:7}\t{b18[1]:7.2f}\t{b18[b5]:7}\t{b18[3]:7}\t{b18[4]:7}\t{b19[5]:11}\t{b18[5]:12}")
fonk11(b16, b18[3])