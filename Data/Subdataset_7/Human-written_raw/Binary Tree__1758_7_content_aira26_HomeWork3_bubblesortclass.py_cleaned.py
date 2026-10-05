class class1(object):
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        for passnum in range(len(self.b1)-1,0,-1):
            for i in range(passnum):
                if self.b1[i]>self.b1[i+1]:
                    b2 = self.b1[i]
                    self.b1[i] = self.b1[i+1]
                    self.b1[i + 1] = b2
    def fonk3(self,value):
        self.b1.append(value)
        self.fonk2()
    def fonk4(self):
        return self.b1[0]
    def fonk5(self):
        return self.b1[-1]
b3 = class1()
b3.fonk3(2)
b3.fonk3(5)
b3.fonk3(4)
b3.fonk3(12)
print(b3.fonk5())
print(b3.fonk4())
print(b3.fonk2())
import random
import matplotlib.pyplot as plt
for r in range(100):
    b4 = random.randint(0,1000)
    b3.fonk3(b4)
    b5 = b3.fonk4()
    b6 = b3.fonk5()
import time
def fonk6(b13, b12):
    a1 = 0
    a2 = 0
    a3 = 0
    for b4 in b12:
        b7 = time.time()
        b13.fonk3(b4)
        a1 += (time.time() - b7)
        b7 = time.time()
        b8 = b13.fonk4()
        a2 += (time.time() - b7)
        b7 = time.time()
        b9 = b13.fonk5()
        a3 += (time.time() - b7)
    return a1, a2, a3
if b10 = = '__main__':
    b3 = class1()
    b3.fonk3(5)
    print(b3.b1, b3.fonk4(), b3.fonk5())
    b3.fonk3(7)
    print(b3.b1, b3.fonk4(), b3.fonk5())
    b3.fonk3(3)
    print(b3.b1, b3.fonk4(), b3.fonk5())
    b3.fonk3(9)
    print(b3.b1, b3.fonk4(), b3.fonk5())
    a4 = 3
    a5 = 500
    a6 = 100
    values_bubble, values_bubble_min, b11 = [], [], []
    for rounds in range(a6, a5, a6):
        b12 = []
        for r in range(rounds):
            b12.append(random.randint(0, 500))
        a1, a2, a3 = 0, 0, 0
        for repetition in range(5):
            b13 = class1()
            my_add, b5, b6 = fonk6(b13, b12)
            a1 += my_add
            a2 += b5
            a3 += b6
        a1 /= 5
        a2 /= 5
        a3 /= 5
        values_bubble.append(a1 * 1000)
        values_bubble_min.append(a2 * 1000)
        b11.append(a3 * 1000)
    b14 = range(a6, a5, a6)
    plt.plot(b14, values_bubble, b15 = 'Add')
    plt.plot(b14, values_bubble_min, b15 = 'Get Min')
    plt.plot(b14, b11, b15 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of bubble's Solution")
    plt.show()