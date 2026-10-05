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
        return str("(class2 creation b5 = " + str(round(self.b3, 6)) + " b4 = " + str(round(self.b4, 6)) + ")")
class class3:
    def fonk3(self, b6):
        self.b6 = b6
        self.b7 = deque([])
        self.b8 = False
        self.a1 = 0
        self.a2 = 0.0
        self.a3 = 0
        self.a4 = 0
    def fonk4(self, b10, a5, b16, b9 = True):
        self.a1 += 1
        self.a2 += (a5 - b10.b3)
        if (b10.b3 + b10.b4 >= a5):
            self.a3 += 1
            if b9:
                print(str(a5) + "   \t: ", b10, "   \tDeparted as Goodput")
        else:
            self.a4 += 1
            if b9:
                print(str(a5) + "   \t: ", b10,"   \tDeparted as Badput")
        if len(self.b7) == 0:
            self.b8 = False
        else:
            self.b8 = True
            b10 = self.b7.popleft()
            b11 = random.expovariate(1.0/self.b6)
            b16.push(a5 + b11,
                            class1.b2, b10)
    def fonk5(self, b10, a5, b16, b9 = True):
        if b9:
            print(str(a5) + "   \t: ", b10, "   \tArrived ")
        if not self.b8:
            self.b8 = True
            b11 = random.expovariate(1.0/self.b6)
            b16.push(a5 + b11,
                            class1.b2, b10)
        else:
            self.b7.append(b10)
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
b6 = float(input("Enter mean service b5 of b17: "))
b12 = float(input("Enter mean interarrival b5 of requests: "))
b13 = float(input("Enter average b4 of requests: "))
b14 = int(input("Enter maximum number of customers to service before stopping a run: "))
b15 = int(input("Enter number of runs: "))
b9 = bool(int(input("Type 1 for b9 and 0 for no b9: ")))
def fonk12(i, b6, b12, b14):
    b16 = PriorityQueue()
    a5 = 0.0
    b17 = class3(b6)
    b18 = random.expovariate(1.0/b12)
    b4 = random.expovariate(1.0/b13)
    b16.push(a5 + b18, class1.b1, class2(a5 + b18, b4))
    a6 = 0.0
    a7 = 0
    while not (b16.isEmpty() or b17.fonk6() == b14):
        event_start_time, b20, b10 = b16.pop()
        b19 = a5
        a5 = event_start_time
        if b20 = = class1.b2:
            a6 += (a5 - b19)
            a7 += (a5 - b19) * b17.fonk8()
            b17.fonk4(b10, a5, b16, b9)
        elif b20 = = class1.b1:
            if (b17.fonk7() == True):
                a6 += (a5 - b19)
            a7 += (a5 - b19) * b17.fonk8()
            b17.fonk5(b10, a5, b16, b9)
            b18 = random.expovariate(1.0/b12)
            b4 = random.expovariate(1.0/b13)
            b16.push(a5 + b18, class1.b1, class2(a5 + b18, b4))
    assert b17.fonk6() == b14
    b21 = a5
    a2 = b17.fonk9()
    b22 = a6 / b21
    b23 = a7 / b21
    b24 = a2 / b14
    b25 = b14 / b21
    a3 = b17.fonk10() / b21
    a4 = b17.fonk11() / b21
    assert abs(a3 + a4 - b25) < 1e-3
    print("")
    print("class3 Utilization: \t", b22)
    print("Average Queue Length: \t", b23)
    print("Average Response Time: \t", b24)
    print("Goodput: \t\t", a3)
    print("Badput: \t\t", a4)
    return b22, b23, b24, a3, a4
b26 = []
b27 = []
b28 = []
b29 = []
b30 = []
def fonk13(list_):
    return sum(list_) / len(list_)
for i in range(b15):
    print("--------------------------------------------------")
    print("Run " + str(i))
    b22, b23, b24, a3, a4 = fonk12(
        i, b6, b12, b14)
    b26.append(b22)
    b27.append(b23)
    b28.append(b24)
    b29.append(a3)
    b30.append(a4)
print("\n")
print("class3 Utilization: \t", fonk13(b26))
print("Queue Length: \t\t", fonk13(b27))
print("Response Time: \t\t", fonk13(b28))
print("Goodput: \t\t", fonk13(b29))
print("Badput: \t\t", fonk13(b30))