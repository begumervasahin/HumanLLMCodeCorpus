class class1:
    def fonk1(b6, b1 = None):
        b6.b1 = b1 or b'*'
        b6.a1 = 0
        b6.a2 = 0
        b6.b2 = None
        b6.b3 = None
        b6.b4 = None
    def fonk2(b6, child_node):
        b6.b3 = child_node
        b6.fonk9(child_node)
    def fonk3(b6, child_node):
        b6.b4 = child_node
        b6.fonk9(child_node)
    def fonk4(b6, current_child, new_child):
        if b6.b3 = = current_child:
            b6.fonk2(new_child)
        elif b6.b4 = = current_child:
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
        b5 = node.b2
        while b5:
            if b5 = = b6:
                return True
            b5 = b5.b2
        return False
    def fonk8(b6, other):
        if b6 = = other or b6.fonk7(other) or other.fonk7(b6):
            return
        b7 = b6.b2
        b8 = other.b2
        b8.fonk4(other, b6)
        b7.fonk4(b6, other)
    def fonk9(b6, child_node):
        child_node.b2 = b6
        child_node.fonk5()
if b9 = = "__main__":
    b10 = class1('A')
    b11 = class1('B')
    b12 = class1('C')
    b10.fonk2(b11)
    b10.fonk3(b12)
    b11.fonk8(b12)
    print(f"class1 A's b3 child: {b10.b3.b1}")
    print(f"class1 A's b4 child: {b10.b4.b1}")
