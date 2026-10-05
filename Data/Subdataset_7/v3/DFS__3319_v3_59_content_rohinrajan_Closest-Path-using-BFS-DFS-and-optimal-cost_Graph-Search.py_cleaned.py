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
    for b18 in b5:
        if b18.b2 = = b2:
            return b18
    return None
def fonk6():
    try:
        with open('b9.txt', 'r') as file_obj:
            b9 = file_obj.read().split('\n')
            for b10 in b9:
                b10 = b10.split(',')
                if len(b10) < 2:
                    break
                b11 = fonk5(b10[0]) or class1(b10[0])
                b5.append(b11)
                b12 = fonk5(b10[1]) or class1(b10[1], b10[0], int(b10[2]))
                b5.append(b12)
                b6.setdefault(b11.b2, []).append(b12)
                b6.setdefault(b12.b2, []).append(b11)
    except Exception as e:
        print(e)
def fonk7(b19):
    return b19.get()
def fonk8(s_list):
    b13 = []
    b14 = b24.b8
    b13.append(b14)
    while b14 in s_list:
        b14 = s_list[b14]
        b13.append(b14)
    b13.reverse()
    return b13
def fonk9(b19, node_state):
    b15 = False
    b16 = queue.Queue() if b22 == 1 else queue.LifoQueue()
    while not b19.empty():
        b17 = b19.get()
        if b17 = = node_state:
            b15 = True
        b16.put(b17)
    return b16, b15
def fonk10(b13):
    for node_state in b13:
        b18 = fonk5(node_state)
        if b18:
            print(f"{b18.b2} {b18.b3} {b18.b4}")
def fonk11():
    b13 = {}
    b18 = fonk5(b24.b7)
    if b24.fonk3(b18.b2):
        return b18.b2
    b19 = fonk12(b18.b2)
    b20 = []
    while not b19.empty():
        b18 = fonk7(b19)
        b20.append(b18.b2)
        b21 = b24.fonk4(b18.b4, b18.b2)
        for child in b21:
            b19, b15 = fonk9(b19, child.b2)
            if child.b2 not in b20 and not b15:
                if b24.fonk3(child.b2):
                    b13[child.b2] = b18.b2
                    return fonk8(b13)
                b19 = fonk13(b19, child.b2)
                b13[child.b2] = b18.b2
def fonk12(node_name):
    return queue.Queue() if b22 = = 1 else queue.LifoQueue()
def fonk13(b19, node_state):
    b19.put(node_state)
    return b19
if b23 = = "__main__":
    fonk6()
    b7 = input("Enter the Source class1: ")
    b8 = input("Enter the Destination class1: ")
    b22 = int(input("Enter 1 for BFS or 2 for DFS: "))
    b24 = class2(b7, b8)
    b13 = fonk11()
    fonk10(b13)