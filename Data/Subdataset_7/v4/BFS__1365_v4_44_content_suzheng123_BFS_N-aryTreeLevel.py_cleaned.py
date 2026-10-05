
class class1(object):
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
class class2(object):
    def fonk2(self, root):
        if not root:
            return []
        b3 = [root]
        b4 = []
        while b3:
            b5 = []
            b6 = []
            for node in b3:
                b5.append(node.b1)
                for child in node.b2:
                    b6.append(child)
            b3 = b6
            b4.append(b5)
        return b4
