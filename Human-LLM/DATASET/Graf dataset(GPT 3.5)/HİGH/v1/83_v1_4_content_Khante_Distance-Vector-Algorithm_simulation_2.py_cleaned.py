import queue
import threading
from time import sleep
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = False
        self.b3 = {}
    def fonk2(self):
        return self.b1
    def fonk3(self):
        print(f'{self}: Running')
        while not self.b2:
            sleep(0.5)
        print(f'{self}: Stopped')
    def fonk4(self, dest, msg):
        if dest in self.b3:
            self.b3[dest].put(msg)
        else:
            print(f'{self}: Destination {dest} not found')
class class2:
    def fonk5(self, b1, b4, b5):
        self.b1 = b1
        self.b2 = False
        self.b4 = b4
        self.b5 = b5
        self.b3 = {}
        self.b6 = {}
    def fonk6(self):
        return self.b1
    def fonk7(self):
        print(f'{self}: Running')
        while not self.b2:
            sleep(0.5)
        print(f'{self}: Stopped')
    def fonk8(self, update_interval):
        print(f'{self}: Sending routing updates every {update_interval} seconds')
        sleep(update_interval)
        print(f'{self}: Routing updates sent')
    def fonk9(self):
        print(f'{self}: Routing table:')
        for dest, cost in self.b6.items():
            print(f'Destination: {dest}, Cost: {cost}')
class class3:
    def fonk10(self, b7, b8, b9, b10):
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        print(f'Created link: {self}')
    def fonk11(self):
        return f'class3 {self.b7}-{self.b8} - {self.b9}-{self.b10}'
class class4:
    def fonk12(self):
        self.b11 = []
        self.b2 = False
    def fonk13(self):
        return 'class3 Layer'
    def fonk14(self, link):
        self.b11.append(link)
    def fonk15(self):
        print(f'{self}: Running')
        while not self.b2:
            sleep(0.5)
        print(f'{self}: Stopped')
if b12 = = '__main__':
    b13 = []
    b14 = class1('H1')
    b13.append(b14)
    b15 = class1('H2')
    b13.append(b15)
    b4 = {'H1': {0: 1}, 'RB': {1: 1}}
    b16 = class2(b1='RA', b4=b4, b5=0)
    b13.append(b16)
    b4 = {'H2': {1: 3}, 'RA': {0: 1}}
    b17 = class2(b1='RB', b4=b4, b5=0)
    b13.append(b17)
    b18 = class4()
    b13.append(b18)
    b18.fonk14(class3(b14, 0, b16, 0))
    b18.fonk14(class3(b16, 1, b17, 0))
    b18.fonk14(class3(b17, 1, b15, 0))
    b19 = []
    for obj in b13:
        b19.append(threading.Thread(b1 = obj.fonk13(), target=obj.run))
    for t in b19:
        t.start()
    b16.fonk8(1)
    sleep(2)
    print("Converged routing tables")
    for obj in b13:
        if str(type(obj)) == "<class '__main__.class2'>":
            obj.fonk9()
    b14.fonk4('H2', 'MESSAGE_FROM_H1')
    b15.fonk4('H1', 'reply for MESSAGE_FROM_H1')
    sleep(2)
    for o in b13:
        o.b2 = True
    for t in b19:
        t.join()
    print("All simulation threads joined")