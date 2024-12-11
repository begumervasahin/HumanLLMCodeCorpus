import queue
b1 = []
b2 = {}
b3 = None
a1 = 1
class class1:
    def fonk1(self, b4, b7, b6, b5):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
def fonk2(b4):
    for b20 in b1:
        if b20.b4 = = b4:
            return b20
    return None
def fonk3():
    try:
        with open('b8.txt', 'r') as flobj:
            b8 = flobj.read().split('\n')
            for i in b8:
                b9 = i.split(',')
                b10 = []
                if len(b9) < 2:
                    break
                b11 = fonk2(b9[0])
                if b11 is None:
                    b11 = class1(b9[0], None, 'Move to', 0)
                    b1.append(b11)
                b12 = fonk2(b9[1])
                if b12 is None:
                    b12 = class1(b9[1], b9[0], 'Move to', int(b9[2]))
                    b1.append(b12)
                b10 = b2.get(b11.b4, [])
                b10.append(b12)
                b2[b11.b4] = b10
                b10 = b2.get(b12.b4, [])
                b10.append(b11)
                b2[b12.b4] = b10
    except Exception as e:
        print(e)
class class2:
    def fonk4(self, b13, b14):
        self.b13 = b13
        self.b14 = b14
    def fonk5(self, node_state):
        return self.b14 = = node_state
    def fonk6(self, action, b4):
        return b2[b4]
def fonk7(b21):
    return b21.get()
def fonk8(s_list):
    b15 = []
    b16 = b3.b14
    b15.append(b16)
    while b16 in s_list.keys():
        b16 = s_list[b16]
        b15.append(b16)
    b15.reverse()
    return b15
def fonk9(b21, node_state):
    b17 = False
    b18 = queue.Queue() if a1 == 1 else queue.LifoQueue()
    while not b21.empty():
        b19 = b21.get()
        if b19 = = node_state:
            b17 = True
        b18.put(b19)
    return b18, b17
def fonk10(b15):
    for node_state in b15:
        b20 = fonk2(node_state)
        if b20 is not None:
            print(b20.b4 + ' ' + str(b20.b5) + ' ' + b20.b6)
def fonk11():
    b15 = {}
    b20 = fonk2(b3.b13)
    if b3.fonk5(b20.b4):
        return b20.b4
    b21 = fonk12(b20.b4)
    b22 = []
    while not b21.empty():
        b20 = fonk7(b21)
        b22.append(b20.b4)
        b23 = b3.fonk6(b20.b6, b20.b4)
        for child in b23:
            b21, b17 = fonk9(b21, child.b4)
            if child.b4 not in b22 and not b17:
                if b3.fonk5(child.b4):
                    b15[child.b4] = b20.b4
                    return fonk8(b15)
                b21 = fonk13(b21, child.b4)
                b15[child.b4] = b20.b4
def fonk12(node_name):
    return queue.Queue() if a1 = = 1 else queue.LifoQueue()
def fonk13(b21, node_state):
    b21.put(node_state)
    return b21
if b24 = = "__main__":
    fonk3()
    b13 = input("Enter the Source class1: ")
    b14 = input("Enter the Destination class1: ")
    a1 = int(input("Enter 1 for BFS or 2 for DFS: "))
    b3 = class2(b13, b14)
    b15 = fonk11()
    fonk10(b15)