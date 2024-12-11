import Queue
b1 = []
b2 = {}
b3 = None
a1 = 1
class class1:
    def fonk1(self, state, parent, actions, path_cost):
        self.b4 = state
        self.b5 = path_cost
        self.b6 = actions
        self.b7 = parent
def fonk2(state):
    for b17 in b1:
        if b17.b4 = = state:
            return b17
    return None
'''
    Common Method for BFS and DFS based on the imput given by the user the queue insertion and deletion would be different
'''
def fonk3():
    try:
        with open('input_data.txt', 'r') as flobj:
            b8 = flobj.read().split('\n')
            for i in b8:
                b9 = i.split(',')
                b10 = []
                if len(b9) < 2:
                    break
                b11 = fonk2(b9[0])
                if b11 = = None:
                    b11 = class1(b9[0], None, 'Move to', 0)
                    b1.append(b11)
                b12 = fonk2(b9[1])
                if b12 = = None:
                    b12 = class1(b9[1], b9[0], 'Move to', b9[2])
                    b1.append(b12)
                if b9[0] in b2:
                    b10 = b2[b11.b4]
                    b10.append(b12)
                else:
                    b10 = [b12]
                    b2[b11.b4] = b10
                if b9[1] in b2:
                    b10 = b2[b12.b4]
                    b10.append(b11)
                else:
                    b10 = [b11]
                    b2[b12.b4] = b10
    except Exception, e:
        print e
class class2:
    def fonk4(self, source, destination):
        self.b13 = source
        self.b14 = destination
    def fonk5(self, NodeState):
        return self.b14 = = NodeState
    def fonk6(self, action, state):
        b15 = b2[state]
        return b15
def fonk7(b23):
    b16 = b23.get()
    b17 = fonk2(b16)
    return b17
def fonk8(sList):
    b18 = []
    b19 = b3.b14
    b18.append(b19)
    while b19 in sList.keys():
        b19 = sList[b19]
        b18.append(b19)
    b18.reverse()
    return b18
def fonk9(b23, b16):
    b20 = False
    if a1 = = 1:
        b21 = Queue.Queue()
    else:
        b21 = Queue.LifoQueue()
    while not b23.empty():
        b22 = b23.get()
        if b22 = = b16:
            b20 = True
        b21.put(b22)
    return b21, b20
def fonk10(b18):
    for b16 in b18:
        b17 = fonk2(b16)
        if b17 is not None:
            print b17.b4 + ' ' + str(b17.b5) + ' ' + b17.b6
def fonk11():
    b18 = {}
    b17 = fonk2(b3.b13)
    if b3.fonk5(b17.b4):
        return b17.b4
    b23 = fonk12(b17.b4)
    b24 = []
    while b23.qsize() > 0:
        b17 = fonk7(b23)
        b24.append(b17.b4)
        b15 = b3.fonk6(b17.b6, b17.b4)
        for child in b15:
            b23, b20 = fonk9(b23, child.b4)
            if child.b4 not in b24 and b20 = = False:
                if b3.fonk5(child.b4):
                    b18[child.b4] = b17.b4
                    return fonk8(b18)
                b23 = fonk13(b23, child.b4)
                b18[child.b4] = b17.b4
def fonk12(nodeName):
    if a1 = = 1:
        b25 = Queue.Queue()
    else:
        b25 = Queue.LifoQueue()
    b25.put(nodeName)
    return b25
def fonk13(b23, b16):
    b23.put(b16)
    return b23
if b26 = = "__main__":
    fonk3()
    b13 = raw_input("Enter the b13 class1: ")
    b14 = raw_input("Enter the b14 class1: ")
    a1 = int(raw_input("Enter 1. for BFS \nEnter 2. for DFS: "))
    b3 = class2(b13, b14)
    b18 = fonk11()
    fonk10(b18)