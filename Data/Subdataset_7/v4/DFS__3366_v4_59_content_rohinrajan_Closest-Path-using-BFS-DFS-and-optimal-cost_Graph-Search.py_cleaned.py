import queue
b1 = []
b2 = {}
b3 = None
a1 = 1
class class1:
    def fonk1(self, b5, b4 = None, b7='Move to', b6=0):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b4 = b4
def fonk2(b5):
    for b19 in b1:
        if b19.b5 = = b5:
            return b19
    return None
def fonk3():
    try:
        with open('b8.txt', 'r') as file_obj:
            b8 = file_obj.read().split('\n')
            for b9 in b8:
                b9 = b9.split(',')
                if len(b9) < 2:
                    break
                b10 = fonk2(b9[0]) or class1(b9[0])
                b1.append(b10)
                b11 = fonk2(b9[1]) or class1(b9[1], b9[0], b9[2])
                b1.append(b11)
                b2.setdefault(b10.b5, []).append(b11)
                b2.setdefault(b11.b5, []).append(b10)
    except Exception as e:
        print(e)
class class2:
    def fonk4(self, b12, b13):
        self.b12 = b12
        self.b13 = b13
    def fonk5(self, node_state):
        return self.b13 = = node_state
    def fonk6(self, action, b5):
        return b2[b5]
def fonk7(b20):
    return b20.get()
def fonk8(s_list):
    b14 = []
    b15 = b3.b13
    b14.append(b15)
    while b15 in s_list:
        b15 = s_list[b15]
        b14.append(b15)
    b14.reverse()
    return b14
def fonk9(b20, node_state):
    b16 = False
    b17 = queue.Queue() if a1 == 1 else queue.LifoQueue()
    while not b20.empty():
        b18 = b20.get()
        if b18 = = node_state:
            b16 = True
        b17.put(b18)
    return b17, b16
def fonk10(b14):
    for node_state in b14:
        b19 = fonk2(node_state)
        if b19:
            print(f"{b19.b5} {b19.b6} {b19.b7}")
def fonk11():
    b14 = {}
    b19 = fonk2(b3.b12)
    if b3.fonk5(b19.b5):
        return b19.b5
    b20 = fonk12(b19.b5)
    b21 = []
    while not b20.empty():
        b19 = fonk7(b20)
        b21.append(b19.b5)
        b22 = b3.fonk6(b19.b7, b19.b5)
        for child in b22:
            b20, b16 = fonk9(b20, child.b5)
            if child.b5 not in b21 and not b16:
                if b3.fonk5(child.b5):
                    b14[child.b5] = b19.b5
                    return fonk8(b14)
                b20 = fonk13(b20, child.b5)
                b14[child.b5] = b19.b5
def fonk12(node_name):
    return queue.Queue() if a1 = = 1 else queue.LifoQueue()
def fonk13(b20, node_state):
    b20.put(node_state)
    return b20
if b23 = = "__main__":
    fonk3()
    b12 = input("Enter the Source class1: ")
    b13 = input("Enter the Destination class1: ")
    a1 = int(input("Enter 1 for BFS or 2 for DFS: "))
    b3 = class2(b12, b13)
    b14 = fonk11()
    fonk10(b14)