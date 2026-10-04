import re
import time
import threading
class class1:
    def fonk1(self, b1, b10, b3, b4, b5):
        self.b1 = b1
        self.b2 = list(map(int, b10))
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = [float('inf')] * b1
        self.b6[int(b3) - 1] = 0
        self.b7 = [None] * b1
    def fonk2(self):
        print("Router", self.b3, "will send data to routers:", self.b4)
    def fonk3(self):
        print("Sending data...")
    def fonk4(self):
        print("Receiving data...")
    def fonk5(self, b8):
        b8 = list(map(int, b8))
        for i in range(self.b1):
            if b8[i] < self.b2[i]:
                self.b2[i] = b8[i]
                self.b6[i] = self.b2[i]
                self.b7[i] = int(self.b3)
        print("Updated costs:", self.b2)
def fonk6():
    b4 = {}
    b5 = {}
    b1 = 0
    b3 = input("Welcome to Emulated Bellman-Ford Algorithm\nWhich router am I?\n")
    with open("which_port.txt") as which_router_file:
        for line in which_router_file:
            b4[line[0]] = int(line[2:6])
            b5[int(line[2:6])] = int(line[0])
            b1 += 1
    with open("adj_mat.txt") as adj_mat_file:
        b9 = adj_mat_file.readlines()[int(b3) - 1].strip()
        b10 = re.split(r"\b12+", b9)
    print('Initial Cost is {}\n'.format(b10))
    b11 = class1(b1, b10, b3, b4, b5)
    b11.fonk2()
    b12 = input("To b13 Bellman-Ford Algorithm, Enter 'b12'\n")
    while b12 != 'b12':
        b12 = input("Wrong input! To b13 Bellman-Ford Algorithm, Enter 'b12'\n")
    b11.fonk3()
    b13 = time.time()
    def fonk7():
        nonlocal b13
        while True:
            time.sleep(1)
            b14 = time.time() - b13
            if b14 > 1:
                b11.fonk3()
                b13 = time.time()
    b15 = threading.Thread(target=periodic_send)
    b15.b16 = True
    b15.b13()
    while True:
        b11.fonk4()
        if msvcrt.kbhit():
            b17 = ord(msvcrt.getch())
            if b17 = = ord('u'):
                with open("adj_mat.txt") as adj_mat_file:
                    b9 = adj_mat_file.readlines()[int(b3) - 1].strip()
                    b8 = re.split(r"\b12+", b9)
                    print('New b2 is {}\n'.format(b8))
                    b11.fonk5(b8)
if b18 = = "__main__":
    fonk6()