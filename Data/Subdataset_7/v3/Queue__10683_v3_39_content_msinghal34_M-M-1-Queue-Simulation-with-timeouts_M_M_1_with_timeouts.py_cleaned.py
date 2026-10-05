import random
from enum import Enum
from collections import deque
from util import PriorityQueue
class class1(Enum):
    b1 = "Arrival"
    b2 = "Departure"
class class2:
    def fonk1(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"class2(b3 = {round(self.b3, 6)}, b4={round(self.b4, 6)})"
class class3:
    def fonk3(self, b5):
        self.b5 = b5
        self.b6 = deque([])
        self.b7 = False
        self.a1 = 0
        self.a2 = 0.0
        self.a3 = 0
        self.a4 = 0
    def fonk4(self, b9, sim_time, event_list, b8 = True):
        self.a1 += 1
        self.a2 += sim_time - b9.b3
        if b9.b3 + b9.b4 >= sim_time:
            self.a3 += 1
            if b8:
                print(f"{sim_time}\t: {b9}\tDeparted as Goodput")
        else:
            self.a4 += 1
            if b8:
                print(f"{sim_time}\t: {b9}\tDeparted as Badput")
        if len(self.b6) == 0:
            self.b7 = False
        else:
            self.b7 = True
            b9 = self.b6.popleft()
            b10 = random.expovariate(1.0 / self.b5)
            event_list.push(sim_time + b10, class1.b2, b9)
    def fonk5(self, b9, sim_time, event_list, b8 = True):
        if b8:
            print(f"{sim_time}\t: {b9}\tArrived ")
        if not self.b7:
            self.b7 = True
            b10 = random.expovariate(1.0 / self.b5)
            event_list.push(sim_time + b10, class1.b2, b9)
        else:
            self.b6.append(b9)
def fonk6(b5, b12, b13, max_customers_to_service, b8 = True):
if b11 = = "__main__":
    b5 = float(input("Enter mean service time of server: "))
    b12 = float(input("Enter mean interarrival time of requests: "))
    b13 = float(input("Enter average b4 of requests: "))
    b14 = int(input("Enter maximum number of customers to service before stopping a run: "))
    b15 = int(input("Enter number of runs: "))
    b8 = bool(int(input("Type 1 for b8 and 0 for no b8: ")))
    b16 = []
    b17 = []
    b18 = []
    b19 = []
    b20 = []
    for i in range(b15):
        print("--------------------------------------------------")
        print("Run", i)
        utilization, queue_length, response_time, a3, a4 = fonk6(
            b5, b12, b13, b14, b8)
        b16.append(utilization)
        b17.append(queue_length)
        b18.append(response_time)
        b19.append(a3)
        b20.append(a4)
    print("\nAverage Results:")
    print("class3 Utilization:\t", sum(b16) / len(b16))
    print("Queue Length:\t\t", sum(b17) / len(b17))
    print("Response Time:\t\t", sum(b18) / len(b18))
    print("Goodput:\t\t", sum(b19) / len(b19))
    print("Badput:\t\t\t", sum(b20) / len(b20))