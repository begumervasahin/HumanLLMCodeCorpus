class class1:
    def fonk1(b10):
        b10.b1 = None
    def fonk2(b10, b2):
        if b10.b1:
            b10.b1.fonk10(b2)
        else:
            b10.b1 = class2(b2)
    def fonk3(b10, b2):
        if b10.b1:
            return b10.b1.fonk11(b2)
        raise ValueError("Tree is empty")
    def fonk4(b10):
        if b10.b1:
            return b10.b1.fonk12()
        return []
    def fonk5(b10):
        if b10.b1:
            return b10.b1.fonk13()
        return []
    def fonk6(b10, b2):
        if b10.b1:
            b10.b1 = b10.b1.fonk14(b2)
        else:
            raise ValueError("Tree is empty")
    def fonk7(b10, b2):
        if b10.b1:
            b10.b1 = b10.b1.fonk15(b2)
        else:
            raise ValueError("Tree is empty")
    def fonk8(b10):
        if b10.b1:
            return iter(b10.b1)
        return iter([])
class class2:
    def fonk9(b10, b2):
        b10.b2 = b2
        b10.b3 = None
        b10.b4 = None
    def fonk10(b10, b2):
        if b2 < b10.b2:
            if b10.b3:
                b10.b3.fonk10(b2)
            else:
                b10.b3 = class2(b2)
        elif b2 >= b10.b2:
            if b10.b4:
                b10.b4.fonk10(b2)
            else:
                b10.b4 = class2(b2)
    def fonk11(b10, b2):
        if b2 < b10.b2:
            if b10.b3:
                return b10.b3.fonk11(b2)
            raise ValueError("Value not found")
        elif b2 > b10.b2:
            if b10.b4:
                return b10.b4.fonk11(b2)
            raise ValueError("Value not found")
        return b10
    def fonk12(b10):
        b5 = b10.b3.fonk12() if b10.b3 else []
        b6 = b10.b4.fonk12() if b10.b4 else []
        return b5 + [b10.b2] + b6
    def fonk13(b10):
        b7 = []
        b8 = class3(b10)
        while True:
            try:
                b2 = next(b8)
                b7.append(b2)
            except StopIteration:
                break
        return b7
    def fonk14(b10, b2):
        if b2 < b10.b2:
            if b10.b3:
                b10.b3 = b10.b3.fonk14(b2)
            raise ValueError("Value not found")
        elif b2 > b10.b2:
            if b10.b4:
                b10.b4 = b10.b4.fonk14(b2)
            raise ValueError("Value not found")
        else:
            return b10.fonk16()
    def fonk15(b10, b2):
        if b2 < b10.b2:
            if b10.b3:
                b10.b3 = b10.b3.fonk15(b2)
            raise ValueError("Value not found")
        elif b2 > b10.b2:
            if b10.b4:
                b10.b4 = b10.b4.fonk15(b2)
            raise ValueError("Value not found")
        else:
            return b10.fonk16()
    def fonk16(b10):
        b9 = b10
        if b9.b3:
            b10 = b9.b3.search_max()
            b10.b3 = b9.b3.fonk17()
            b10.b4 = b9.b4
        else:
            b10 = b9.b4
        b9.b3 = None
        b9.b4 = None
        return b10
    def fonk17(b10):
        if b10.b4:
            b10.b4 = b10.b4.fonk17()
        else:
            b10 = b10.b3
        return b10
    def fonk18(b10):
        if b10.b3:
            b10.b3 = b10.b3.fonk18()
        else:
            b10 = b10.b4
        return b10
class class3:
    def fonk19(b10, b1):
        b11 = class2(None)
        b11.b4 = b1
        b10.b12 = [b11]
    def fonk20(b10):
        if b10.fonk23().b4:
            b10.fonk21()
        else:
            b10.fonk22()
        return b10.fonk23().b2
    def fonk21(b10):
        b10.b12.append(b10.fonk23().b4)
        while b10.fonk23().b3:
            b10.b12.append(b10.fonk23().b3)
    def fonk22(b10):
        try:
            while b10.b12.pop() == b10.fonk23().b4:
                pass
        except IndexError:
            raise StopIteration
    def fonk23(b10):
        return b10.b12[-1]
    def fonk24(b10):
        return b10
def fonk25(binary_search_node):
    return iter(binary_search_node.fonk12())
def fonk26(binary_search_node):
    return class3(binary_search_node)
def fonk27(binary_search_node):
    b13 = binary_search_node
    if b13.b3:
        yield from b13.b3
    yield b13.b2
    if b13.b4:
        yield from b13.b4
b14 = class1()
b15 = [5, 3, 7, 1, 4, 6, 8]
for b2 in b15:
    b14.fonk10(b2)
print("Binary Search Tree:")
print(b14.fonk12())
print("Sequential traversal:")
print(b14.fonk13())
print("Searching for 3:", b14.fonk11(3).b2)
print("Searching for 10:")
try:
    print(b14.fonk11(10).b2)
except ValueError as e:
    print(e)
b14.fonk14(5)
print("After deleting 5 from b3:")
print(b14.fonk12())
b14.fonk15(7)
print("After deleting 7 from b4:")
print(b14.fonk12())