class class1(object):
    def fonk1(self, root):
        b1 = []
        b2 = []
        b3 = root
        b4 = set()
        while b3 or b2:
            if b3:
                b2.append(b3)
                b3 = b3.left
            else:
                b3 = b2.pop()
                if b3.right and not(b3.right in b4):
                    b2.append(b3)
                    b3 = b3.right
                else:
                    b4.add(b3)
                    b1.append(b3.val)
                    b3 = None
        return b1