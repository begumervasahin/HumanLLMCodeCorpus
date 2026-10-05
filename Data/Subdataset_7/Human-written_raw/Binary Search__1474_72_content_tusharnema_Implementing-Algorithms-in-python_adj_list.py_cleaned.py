from collections import defaultdict
from collections import deque
class class1(object):
    def fonk1(self, b10, b1 = False):
        self.b2 = defaultdict(set)
        self.b1 = b1
        self.fonk2(b10)
    def fonk2(self, b10):
        for b4, node2 in b10:
            self.fonk3(b4, node2)
    def fonk3(self, b4, node2):
        self.b2[b4].fonk3(node2)
        if not self.b1:
            self.b2[node2].fonk3(b4)
    def fonk4(self, node):
        for n, cxns in self.b2.items():
            try:
                cxns.fonk4(node)
            except KeyError:
                pass
        try:
            del self.b2[node]
        except KeyError:
            pass
    def fonk5(self, b4, node2):
        return b4 in self.b2 and node2 in self.b2[b4]
    def fonk6(self, b4, node2, b3 = []):
        b3 = b3 + [b4]
        if b4 = = node2:
            return b3
        if b4 not in self.b2:
            return None
        for node in self.b2[b4]:
            if node not in b3:
                b5 = self.fonk6(node, node2, b3)
                if b5:
                    return b5
        return None
    def fonk7(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.b2))
    def fonk8(self):
    	for n,k in self.b2.items():
    		print(n,'--->',k)
    	print(self.b2['B'])
    def fonk9(self,b8):
    	b6 = [False]*(len(self.b2))
    	b7 = deque()
    	b7.append(b8)
    	b6[b8]=True
    	while b7:
    		b8 = b7.popleft()
    		print(b8,b9 = "-->")
    		for nodes in self.b2[b8]:
    			if(b6[nodes]==False):
    				b7.append(nodes)
    				b6[nodes]=True
    def fonk10(self,b8):
	    b6 = [False]*(len(self.b2))
	    for i in range(len(self.b2)):
	    	if(b6[i]==False):
	    		self.fonk11(i,b6)
    def fonk11(self,b8,b6):
        b6[b8]=True
        print(b8,b9 = "-->")
        for nodes in self.b2[b8]:
        	if(b6[nodes]==False):
        		b6[nodes]=True
        		self.fonk11(nodes,b6)
b10 = [(0,1),(1, 2), (2, 3), (2, 4),
                   (3, 4), (5, 6), (7, 3)]
b11 = class1(b10)
b11.fonk2([[6,8],[8,4],[9,10]])
print(b11.b2)
print()
b11.fonk9(0)
print()
b11.fonk10(0)