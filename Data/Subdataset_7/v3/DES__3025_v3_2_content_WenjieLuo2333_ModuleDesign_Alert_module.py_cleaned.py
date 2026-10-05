import numpy as np
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = [[] for _ in range(3)]
        self.a1 = -1
    def fonk2(self, value, b7):
        b5 = {
            'bo': (0.1, 0.3),
            'bp': (80, 120),
            'pul': (60, 90)
        }
        min_threshold, b6 = b5[b7]
        if not min_threshold <= value <= b6:
            return list(b5.keys()).index(b7)
        return -1
    def fonk3(self):
        return self.a1
    def fonk4(self, data):
        value, b7 = data
        b8 = {
            0: self.b1,
            1: self.b2,
            2: self.b3
        }
        b9 = b8[b7]
        b9.append(float(value))
        if len(b9) > 20:
            b9.pop(0)
        b10 = np.mean(b9)
        if len(b9) > 2:
            b11 = self.fonk2(b10, list(b8.keys())[b7])
            if b11 != -1:
                self.a1 = b11
        return self.a1
b12 = class1()
b13 = [
    (0.15, 0),
    (110, 1),
    (70, 2)
]
for data in b13:
    a1 = b12.fonk4(data)
    if a1 != -1:
        print(f"Alert Flag: {a1}")
    else:
        print("No alert")