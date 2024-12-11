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
    def fonk4(self, b9, a5, b11, b8 = True):
        self.a1 += 1
        self.a2 += a5 - b9.b3
        if b9.b3 + b9.b4 >= a5:
            self.a3 += 1
            if b8:
                print(f"{a5}\t: {b9}\tDeparted as Goodput")
        else:
            self.a4 += 1
            if b8:
                print(f"{a5}\t: {b9}\tDeparted as Badput")
        if len(self.b6) == 0:
            self.b7 = False
        else:
            self.b7 = True
            b9 = self.b6.popleft()
            b10 = random.expovariate(1.0 / self.b5)
            b11.push(a5 + b10, class1.b2, b9)
    def fonk5(self, b9, a5, b11, b8 = True):
        if b8:
            print(f"{a5}\t: {b9}\tArrived ")
        if not self.b7:
            self.b7 = True
            b10 = random.expovariate(1.0 / self.b5)
            b11.push(a5 + b10, class1.b2, b9)
        else:
            self.b6.append(b9)
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.b7
    def fonk8(self):
        return len(self.b6)
    def fonk9(self):
        return self.a2
    def fonk10(self):
        return self.a3
    def fonk11(self):
        return self.a4
def fonk12(b5, b21, max_customers_to_service, b8 = True):
    b11 = PriorityQueue()
    a5 = 0.0
    b12 = class3(b5)
    b13 = random.expovariate(1.0 / b21)
    b4 = random.expovariate(1.0 / b22)
    b11.push(a5 + b13, class1.b1, class2(a5 + b13, b4))
    a6 = 0.0
    a7 = 0
    while not (b11.is_empty() or b12.fonk6() == max_customers_to_service):
        event_start_time, b15, b9 = b11.pop()
        b14 = a5
        a5 = event_start_time
        if b15 = = class1.b2:
            a6 += a5 - b14
            a7 += (a5 - b14) * b12.fonk8()
            b12.fonk4(b9, a5, b11, b8)
        elif b15 = = class1.b1:
            if b12.fonk7():
                a6 += a5 - b14
            a7 += (a5 - b14) * b12.fonk8()
            b12.fonk5(b9, a5, b11, b8)
            b13 = random.expovariate(1.0 / b21)
            b4 = random.expovariate(1.0 / b22)
            b11.push(a5 + b13, class1.b1, class2(a5 + b13, b4))
    assert b12.fonk6() == max_customers_to_service
    b16 = a5
    a2 = b12.fonk9()
    b17 = a6 / b16
    b18 = a7 / b16
    b19 = a2 / max_customers_to_service
    b20 = max_customers_to_service / b16
    a3 = b12.fonk10() / b16
    a4 = b12.fonk11() / b16
    return b17, b18, b19, a3, a4
b5 = float(input("Enter mean service time of b12: "))
b21 = float(input("Enter mean interarrival time of requests: "))
b22 = float(input("Enter average b4 of requests: "))
b23 = int(input("Enter maximum number of customers to service before stopping a run: "))
b24 = int(input("Enter number of runs: "))
b8 = bool(int(input("Type 1 for b8 and 0 for no b8: ")))
b25 = []
b26 = []
b27 = []
b28 = []
b29 = []
for i in range(b24):
    print("--------------------------------------------------")
    print("Run", i)
    b17, b18, b19, a3, a4 = fonk12(
        b5, b21, b23, b8)
    b25.append(b17)
    b26.append(b18)
    b27.append(b19)
    b28.append(a3)
    b29.append(a4)
print("\nAverage Results:")
print("class3 Utilization:\t", sum(b25) / len(b25))
print("Queue Length:\t\t", sum(b26) / len(b26))
print("Response Time:\t\t", sum(b27) / len(b27))
print("Goodput:\t\t", sum(b28) / len(b28))
print("Badput:\t\t\t", sum(b29) / len(b29))