class class1:
    def fonk1(b6, b1 = None):
        b6.a1 = 0
        b6.b2 = None
        b6.b3 = None
        b6.b4 = None
        b6.a2 = 0
        b6.b1 = b1 if b1 is not None else b'*'
    def fonk2(b6, node):
        b6.b3 = node
        node.b2 = b6
        node.fonk5()
    def fonk3(b6, node):
        b6.b4 = node
        node.b2 = b6
        node.fonk5()
    def fonk4(b6, old_child, new_child):
        if b6.b3 = = old_child:
            b6.fonk2(new_child)
        elif b6.b4 = = old_child:
            b6.fonk3(new_child)
    def fonk5(b6):
        b6.a2 = b6.b2.a2 + 1 if b6.b2 else 0
        if b6.b3:
            b6.b3.fonk5()
        if b6.b4:
            b6.b4.fonk5()
    def fonk6(b6):
        return b6.b3 is None and b6.b4 is None
    def fonk7(b6, node):
        b5 = b6
        while b5:
            if b5 = = node:
                return True
            b5 = b5.b2
        return False
    def fonk8(b6, node):
        if b6 = = node or b6.fonk7(node) or node.fonk7(b6):
            return
        self_parent, b7 = b6.b2, node.b2
        if self_parent:
            self_parent.fonk4(b6, node)
        if b7:
            b7.fonk4(node, b6)
        b6.b3, node.b3 = node.b3, b6.b3
        b6.b4, node.b4 = node.b4, b6.b4
        b6.fonk5()
        node.fonk5()