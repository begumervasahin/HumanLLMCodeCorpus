class class1(object):
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
    def fonk2(self, value):
        self.b1.append(value)
        self.a1 += 1
    def fonk3(self):
        if len(self.b1) > 1:
            b2 = self.b1[0]
            self.b3 = class1()
            self.b4 = class1()
            for i in range(1, len(self.b1)):
                if (self.b1[i] < b2):
                    self.b3.fonk2(self.b1[i])
                else:
                    self.b4.fonk2(self.b1[i])
            return self.b3.fonk3() + [b2] + self.b4.fonk3()
        else:
            return self.b1
    def fonk4(self):
        b5 = self.fonk3()
        return b5[0]
    def fonk5(self):
        b5 = self.fonk3()
        b6 = self.a1 - 1
        return b5[b6]
    def fonk6(self):
        return self.b1
b7 = class1()
b7.fonk2(5)
b7.fonk2(2)
b7.fonk2(4)
print(b7.fonk5())
print(b7.fonk4())
print(b7.fonk3())
print(b7.b1)
import random
for r in range(100):
    b8 = random.randint(0,1000)
    b7.fonk2(b8)
    b9 = b7.fonk4()
    b10 = b7.fonk5()
import time
import matplotlib.pyplot as plt
def fonk7(b15, b17):
    a2 = 0
    a3 = 0
    a4 = 0
    for b8 in b17:
        b11 = time.time()
        b15.fonk2(b8)
        a2 += (time.time() - b11)
        b11 = time.time()
        b12 = b15.fonk4()
        a3 += (time.time() - b11)
        b11 = time.time()
        b13 = b15.fonk5()
        a4 += (time.time() - b11)
    return a2, a3, a4
if b14 = = '__main__':
    b15 = class1()
    b15.fonk2(5)
    print(b15.b1, b15.fonk4(), b15.fonk5())
    b15.fonk2(7)
    print( b15.b1, b15.fonk4(), b15.fonk5())
    b15.fonk2(3)
    print(b15.b1, b15.fonk4(), b15.fonk5())
    b15.fonk2(9)
    print(b15.b1, b15.fonk4(), b15.fonk5())
    a5 = 5
    a6 = 500
    a7 = 100
    values_heap_add, values_heap_min, b16 = [], [], []
    for rounds in range(a7, a6, a7):
        b17 = []
        for r in range(rounds):
            b17.append(random.randint(0, 500))
        a2, a3, a4 = 0, 0, 0
        for repetition in range(5):
           b15 = class1()
           myadd, mymin, b18 = fonk7(b15, b17)
           a2 += myadd
           a3 += mymin
           a4 += b18
        a2 /= 5
        a3 /= 5
        a4 /= 5
        values_heap_add.append(a2 * 1000)
        values_heap_min.append(a3 * 1000)
        b16.append(a4 * 1000)
    b19 = range(a7, a6, a7)
    plt.plot(b19, values_heap_add, b20 = 'Add')
    plt.plot(b19, values_heap_min, b20 = 'Get Min')
    plt.plot(b19, b16, b20 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of class1 Solution")
    plt.show()