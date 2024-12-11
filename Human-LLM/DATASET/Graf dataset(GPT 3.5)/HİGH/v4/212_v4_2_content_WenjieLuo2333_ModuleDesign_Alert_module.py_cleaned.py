import numpy as np
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = [[] for _ in range(3)]
        self.a1 = -1
    def fonk2(self, value, b5):
        if b5 = = 0:
            return 0 if not 0.1 <= value <= 0.3 else -1
        elif b5 = = 1:
            return 1 if not 80 <= value <= 120 else -1
        else:
            return 2 if not 60 <= value <= 90 else -1
    def fonk3(self):
        if self.a1 != -1:
            return self.a1
        else:
            return -1
    def fonk4(self, data):
        value, b5 = data
        if len(self.b4[b5]) < 20:
            self.b4[b5].append(float(value))
        else:
            del self.b4[b5][0]
            self.b4[b5].append(float(value))
        if len(self.b4[0]) > 2 and self.fonk2(np.mean(self.b4[0]), 0) != -1:
            self.a1 = self.fonk2(np.mean(self.b4[b5]), 0)
        if len(self.b4[1]) > 2 and self.fonk2(np.mean(self.b4[1]), 1) != -1:
            self.a1 = self.fonk2(np.mean(self.b4[b5]), 1)
        if len(self.b4[2]) > 2 and self.fonk2(np.mean(self.b4[2]), 2) != -1:
            self.a1 = self.fonk2(np.mean(self.b4[b5]), 2)
        return self.fonk3()
b6 = class1()
b7 = [
    (0.15, 0),
    (110, 1),
    (70, 2)
]
for data in b7:
    a1 = b6.fonk4(data)
    if a1 != -1:
        print(f"Alert Flag: {a1}")
    else:
        print("No alert")