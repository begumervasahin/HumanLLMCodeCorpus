class class1(object):
    def fonk1(b11):
        b11.b1 = None
    def fonk2(b11, b2):
        if b11.b1:
            b11.b1.fonk10(b2)
        else:
            b11.b1 = class2(b2)
    def fonk3(b11, b2):
        if b11.b1:
            return b11.b1.fonk11(b2)
        else:
            raise ValueError
    def fonk4(b11):
        if b11.b1:
            return b11.b1.fonk14()
        else:
            return []
    def fonk5(b11):
        if b11.b1:
            return b11.b1.fonk15()
        else:
            return []
    def fonk6(b11, b2):
        if b11.b1:
            b11.b1 = b11.b1.fonk16(b2)
        else:
            raise ValueError
    def fonk7(b11, b2):
        if b11.b1:
            b11.b1 = b11.b1.fonk17(b2)
        else:
            raise ValueError
    def fonk8(b11):
        if b11.b1:
            return iter(b11.b1)
        else:
            return iter([])
class class2(object):
    def fonk9(b11, b2):
        b11.b2 = b2
        b11.b3 = None
        b11.b4 = None
    def fonk10(b11, b2):
        if b2 < b11.b2:
            if b11.b3:
                b11.b3.fonk10(b2)
            else:
                b11.b3 = class2(b2)
        elif b2 >= b11.b2:
            if b11.b4:
                b11.b4.fonk10(b2)
            else:
                b11.b4 = class2(b2)
    def fonk11(b11, b2):
        if b2 < b11.b2:
            if b11.b3:
                return b11.b3.fonk11(b2)
            else:
                raise ValueError
        elif b2 > b11.b2:
            if b11.b4:
                return b11.b4.fonk11(b2)
            else:
                raise ValueError
        elif b2 = = b11.b2:
            return b11
    def fonk12(b11):
        if b11.b4:
            return b11.b4.fonk12()
        else:
            return b11
    def fonk13(b11):
        if b11.b3:
            return b11.b3.fonk13()
        else:
            return b11
    def fonk14(b11):
        if b11.b3:
            b5 = b11.b3.fonk14()
        else:
            b5 = []
        b6 = b11.b2
        if b11.b4:
            b7 = b11.b4.fonk14()
        else:
            b7 = []
        return b5 + [b6] + b7
    def fonk15(b11):
        b8 = []
        b9 = class3(b11)
        while True:
            try:
                b2 = next(b9)
            except StopIteration:
                break
            else:
                b8.append(b2)
        return b8
    def fonk16(b11, b2):
        if b2 < b11.b2:
            if b11.b3:
                b11.b3 = b11.b3.fonk16(b2)
            else:
                raise ValueError
        elif b2 > b11.b2:
            if b11.b4:
                b11.b4 = b11.b4.fonk16(b2)
            else:
                raise ValueError
        elif b2 = = b11.b2:
            b10 = b11
            if b10.b3:
                b11 = b10.b3.fonk12()
                b11.b3 = b10.b3.fonk18()
                b11.b4 = b10.b4
            else:
                b11 = b10.b4
            b10.b3 = None
            b10.b4 = None
        return b11
    def fonk17(b11, b2):
        if b2 < b11.b2:
            if b11.b3:
                b11.b3 = b11.b3.fonk17(b2)
            else:
                raise ValueError
        elif b2 > b11.b2:
            if b11.b4:
                b11.b4 = b11.b4.fonk17(b2)
            else:
                raise ValueError
        elif b2 = = b11.b2:
            b10 = b11
            if b10.b4:
                b11 = b10.b4.fonk13()
                b11.b4 = b10.b4.fonk19()
                b11.b3 = b10.b3
            else:
                b11 = b10.b3
            b10.b3 = None
            b10.b4 = None
        return b11
    def fonk18(b11):
        if b11.b4:
            b11.b4 = b11.b4.fonk18()
        else:
            b11 = b11.b3
        return b11
    def fonk19(b11):
        if b11.b3:
            b11.b3 = b11.b3.fonk19()
        else:
            b11 = b11.b4
        return b11
    def fonk20(b11):
        raise NotImplementedError
class class3(object):
    def fonk21(b11, b1):
        b12 = class2(None)
        b12.b4 = b1
        b11.b13 = [b12]
    def fonk22(b11):
        if b11.fonk25().b4:
            b11.fonk23()
        else:
            b11.fonk24()
        return b11.fonk25().b2
    def fonk23(b11):
        b11.b13.append(b11.fonk25().b4)
        while b11.fonk25().b3:
            b11.b13.append(b11.fonk25().b3)
    def fonk24(b11):
        try:
            while b11.b13.pop() == b11.fonk25().b4:
                pass
        except IndexError:
            raise StopIteration
    def fonk25(b11):
        return b11.b13[-1]
    def fonk26(b11):
        return b11
def fonk27(binary_search_node):
    return iter(binary_search_node.fonk14())
def fonk28(binary_search_node):
    return class3(binary_search_node)
def fonk29(binary_search_node):
    b14 = binary_search_node
    if b14.b3:
        yield from b14.b3
    yield b14.b2
    if b14.b4:
        yield from b14.b4