import queue
class class1:
    def fonk1(self, b2, b1 = None, b4='Move to', b3=0):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
b5 = []
b6 = {}
class class2:
    def fonk2(self, b7, b8):
        self.b7 = b7
        self.b8 = b8
    def fonk3(self, node_state):
        return self.b8 = = node_state
    def fonk4(self, action, b2):
        return b6[b2]
def fonk5(b2):
    for b19 in b5:
        if b19.b2 = = b2:
            return b19
    return None
def fonk6():
    try:
        with open('b9.txt', 'r') as file_obj:
            b9 = file_obj.read().split('\n')
            for b11 in b9:
                b10 = []
                b11 = b11.split(',')
                if len(b11) < 2:
                    break
                b12 = fonk5(b11[0]) or class1(b11[0])
                b5.append(b12)
                b13 = fonk5(b11[1]) or class1(b11[1], b11[0], int(b11[2]))
                b5.append(b13)
                b6.setdefault(b12.b2, []).append(b13)
                b6.setdefault(b13.b2, []).append(b12)
    except Exception as e:
        print(e)
def fonk7(b20):
    return b20.get()
def fonk8(s_list):
    b14 = []
    b15 = b25.b8
    b14.append(b15)
    while b15 in s_list:
        b15 = s_list[b15]
        b14.append(b15)
    b14.reverse()
    return b14
def fonk9(b20, node_state):
    b16 = False
    b17 = queue.Queue() if b23 == 1 else queue.LifoQueue()
    while not b20.empty():
        b18 = b20.get()
        if b18 = = node_state:
            b16 = True
        b17.put(b18)
    return b17, b16
def fonk10(b14):
    for node_state in b14:
        b19 = fonk5(node_state)
        if b19:
            print(f"{b19.b2} {b19.b3} {b19.b4}")
def fonk11():
    b14 = {}
    b19 = fonk5(b25.b7)
    if b25.fonk3(b19.b2):
        return b19.b2
    b20 = fonk12(b19.b2)
    b21 = []
    while not b20.empty():
        b19 = fonk7(b20)
        b21.append(b19.b2)
        b22 = b25.fonk4(b19.b4, b19.b2)
        for child in b22:
            b20, b16 = fonk9(b20, child.b2)
            if child.b2 not in b21 and not b16:
                if b25.fonk3(child.b2):
                    b14[child.b2] = b19.b2
                    return fonk8(b14)
                b20 = fonk13(b20, child.b2)
                b14[child.b2] = b19.b2
def fonk12(node_name):
    return queue.Queue() if b23 = = 1 else queue.LifoQueue()
def fonk13(b20, node_state):
    b20.put(node_state)
    return b20
if b24 = = "__main__":
    fonk6()
    b7 = input("Enter the Source class1: ")
    b8 = input("Enter the Destination class1: ")
    b23 = int(input("Enter 1 for BFS or 2 for DFS: "))
    b25 = class2(b7, b8)
    b14 = fonk11()
    fonk10(b14)