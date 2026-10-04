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
        return f"(class2 creation b5 = {round(self.b3, 6)} b4 = {round(self.b4, 6)})"
class class3:
    def fonk3(self, b6):
        self.b6 = b6
        self.b7 = deque()
        self.b8 = False
        self.a1 = 0
        self.a2 = 0.0
        self.a3 = 0
        self.a4 = 0
    def fonk4(self, b15, a5, b12, b9 = True):
        self.a1 += 1
        self.a2 += (a5 - b15.b3)
        if b15.b3 + b15.b4 >= a5:
            self.a3 += 1
            if b9:
                print(f"{a5}\t: {b15}\tDeparted as Goodput")
        else:
            self.a4 += 1
            if b9:
                print(f"{a5}\t: {b15}\tDeparted as Badput")
        if self.b7:
            self.b8 = True
            b10 = self.b7.popleft()
            b11 = random.expovariate(1.0 / self.b6)
            b12.push(a5 + b11, class1.b2, b10)
        else:
            self.b8 = False
    def fonk5(self, b15, a5, b12, b9 = True):
        if b9:
            print(f"{a5}\t: {b15}\tArrived")
        if not self.b8:
            self.b8 = True
            b11 = random.expovariate(1.0 / self.b6)
            b12.push(a5 + b11, class1.b2, b15)
        else:
            self.b7.append(b15)
    def fonk6(self):
        return self.a1
    def fonk7(self):
        return self.b8
    def fonk8(self):
        return len(self.b7)
    def fonk9(self):
        return self.a2
    def fonk10(self):
        return self.a3
    def fonk11(self):
        return self.a4
def fonk12(run_id, b6, b23, b25, b24, b9):
    b12 = PriorityQueue()
    a5 = 0.0
    b13 = class3(b6)
    b14 = random.expovariate(1.0 / b23)
    b4 = random.expovariate(1.0 / b24)
    b12.push(a5 + b14, class1.b1, class2(a5 + b14, b4))
    a6 = 0.0
    a7 = 0
    while not b12.is_empty() and b13.fonk6() < b25:
        event_start_time, b17, b15 = b12.pop()
        b16 = a5
        a5 = event_start_time
        if b17 = = class1.b2:
            a6 += (a5 - b16)
            a7 += (a5 - b16) * b13.fonk8()
            b13.fonk4(b15, a5, b12, b9)
        elif b17 = = class1.b1:
            if b13.fonk7():
                a6 += (a5 - b16)
            a7 += (a5 - b16) * b13.fonk8()
            b13.fonk5(b15, a5, b12, b9)
            b14 = random.expovariate(1.0 / b23)
            b4 = random.expovariate(1.0 / b24)
            b12.push(a5 + b14, class1.b1, class2(a5 + b14, b4))
    b18 = a5
    b19 = b13.fonk9() / b25
    b20 = a6 / b18
    b21 = a7 / b18
    b22 = b25 / b18
    a3 = b13.fonk10() / b18
    a4 = b13.fonk11() / b18
    assert abs(a3 + a4 - b22) < 1e-3
    print("")
    print(f"class3 Utilization: \t{b20}")
    print(f"Average Queue Length: \t{b21}")
    print(f"Average Response Time: \t{b19}")
    print(f"Goodput: \t\t{a3}")
    print(f"Badput: \t\t{a4}")
    return b20, b21, b19, a3, a4
def fonk13(values):
    return sum(values) / len(values)
def fonk14():
    b6 = float(input("Enter mean service b5 of b13: "))
    b23 = float(input("Enter mean interarrival b5 of requests: "))
    b24 = float(input("Enter average b4 of requests: "))
    b25 = int(input("Enter maximum number of customers to service before stopping a run: "))
    b26 = int(input("Enter number of runs: "))
    b9 = bool(int(input("Type 1 for b9 and 0 for no b9: ")))
    b27 = []
    b21 = []
    b28 = []
    b29 = []
    b30 = []
    for i in range(b26):
        print("--------------------------------------------------")
        print(f"Run {i}")
        b20, queue_length, b19, a3, a4 = fonk12(
            i, b6, b23, b25, b24, b9)
        b27.append(b20)
        b21.append(queue_length)
        b28.append(b19)
        b29.append(a3)
        b30.append(a4)
    print("\nAverage Results Over All Runs:")
    print(f"class3 Utilization: \t{fonk13(b27)}")
    print(f"Queue Length: \t\t{fonk13(b21)}")
    print(f"Response Time: \t\t{fonk13(b28)}")
    print(f"Goodput: \t\t{fonk13(b29)}")
    print(f"Badput: \t\t{fonk13(b30)}")
if b31 = = "__main__":
    fonk14()