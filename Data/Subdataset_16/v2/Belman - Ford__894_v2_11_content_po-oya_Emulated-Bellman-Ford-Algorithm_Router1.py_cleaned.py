import re
import time
import threading
class class1:
    def fonk1(self, b1, b12, b3, b4, b5):
        self.b1 = b1
        self.b2 = list(map(int, b12))
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = [float('inf')] * b1
        self.b6[int(b3) - 1] = 0
        self.b7 = [None] * b1
    def fonk2(self):
        print(f"Router {self.b3} will send data to routers: {self.b4}")
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
def fonk6(file_path):
    b4 = {}
    b5 = {}
    b1 = 0
    with open(file_path) as file:
        for b11 in file:
            b9 = b11[0]
            b10 = int(b11[2:6])
            b4[b9] = b10
            b5[b10] = int(b9)
            b1 += 1
    return b4, b5, b1
def fonk7(file_path, b3):
    with open(file_path) as file:
        b11 = file.readlines()[int(b3) - 1].strip()
        b12 = re.split(r"\b14+", b11)
    return b12
def fonk8():
    b3 = input("Welcome to Emulated Bellman-Ford Algorithm\nWhich router am I?\n")
    b4, b5, b1 = fonk6("which_port.txt")
    b12 = fonk7("adj_mat.txt", b3)
    print(f'Initial Cost is {b12}\n')
    b13 = class1(b1, b12, b3, b4, b5)
    b13.fonk2()
    b14 = input("To start Bellman-Ford Algorithm, Enter 'b14'\n")
    while b14 != 'b14':
        b14 = input("Wrong input! To start Bellman-Ford Algorithm, Enter 'b14'\n")
    b13.fonk3()
    b15 = time.time()
    def fonk9():
        nonlocal b15
        while True:
            time.sleep(1)
            b16 = time.time() - b15
            if b16 > 1:
                b13.fonk3()
                b15 = time.time()
    b17 = threading.Thread(target=periodic_send, daemon=True)
    b17.start()
    while True:
        b13.fonk4()
        if msvcrt.kbhit():
            b18 = ord(msvcrt.getch())
            if b18 = = ord('u'):
                b8 = fonk7("adj_mat.txt", b3)
                print(f'New b2 is {b8}\n')
                b13.fonk5(b8)
if b19 = = "__main__":
    fonk8()