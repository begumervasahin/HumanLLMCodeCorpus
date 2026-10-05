class class1:
    def fonk1(b6, b1 = None):
        b6.b1 = b1 if b1 is not None else b'*'
        b6.a1 = 0
        b6.b2 = None
        b6.b3 = None
        b6.b4 = None
        b6.a2 = 0
    def fonk2(b6, node):
        b6.b3 = node
        node.b2 = b6
        node.fonk5()
    def fonk3(b6, node):
        b6.b4 = node
        node.b2 = b6
        node.fonk5()
    def fonk4(b6, child, new_node):
        if b6.b3 = = child:
            b6.fonk2(new_node)
        elif b6.b4 = = child:
            b6.fonk3(new_node)
    def fonk5(b6):
        b6.a2 = b6.b2.a2 + 1 if b6.b2 else 0
        for child in [b6.b3, b6.b4]:
            if child:
                child.fonk5()
    def fonk6(b6):
        return not b6.b3 and not b6.b4
    def fonk7(b6, node):
        b5 = b6.b2
        while b5:
            if b5 = = node:
                return True
            b5 = b5.b2
        return False
    def fonk8(b6, node):
        if b6 = = node or node.fonk7(b6) or b6.fonk7(node):
            return
        parent1, b7 = b6.b2, node.b2
        b7.fonk4(node, b6)
        parent1.fonk4(b6, node)