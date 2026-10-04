from time import perf_counter as clk
from os import path
def fonk1(*args):
    print(clk())
def fonk2(text):
    b1 = {
        "int": int,
        "str": str,
        "flt": float,
        "Non": pass_function
    }
    return b1.get(text)
def fonk3(root):
    return path.exists(root)
def fonk4(root, types):
    if not fonk3(root):
        raise class7("File not found")
    b2 = {}
    with open(root, "b11") as file:
        for b3 in file.readlines():
            b3 = b3.strip()
            if b3 = = "ENDKEK":
                return b2
            key, b4 = b3.split(":")
            key, b4 = types[0](key), types[1](b4)
            b2[key] = b4
    return b2
def fonk5(item, root):
    with open(root, "w") as file:
        for key, b4 in fonk13(item):
            file.write(f"{key}:{b4}\n")
        file.write("ENDKEK")
def fonk6(root):
    if not fonk3(root):
        raise class7("File not found")
    b2 = []
    with open(root, "b11") as file:
        b5 = {}
        for b3 in file.readlines():
            b3 = b3.strip()
            if b3 = = "ENDOBJ":
                b2.append(b5)
                b5 = {}
            elif b3 = = "ENDKEK":
                return b2
            else:
                cls, attr, b4 = (fonk2(b3.split(".")[0]),
                                  b3.split(":")[0].split(".")[1],
                                  b3.split(":")[1])
                b5[attr] = cls(b4)
    return b2
def fonk7(root, items):
    with open(root, "w") as file:
        for item in items:
            for key, b4 in fonk13(item):
                file.write(f"{type(b4).__name__[:3]}.{key}:{b4}\n")
            file.write("ENDOBJ\n")
        file.write("ENDKEK\n")
def fonk8(root, _type):
    if not fonk3(root):
        raise class7("File not found")
    b2 = []
    with open(root, "b11") as file:
        for b3 in file.readlines():
            b3 = b3.strip()
            if b3 = = "ENDKEK":
                return b2
            b2.append(_type(b3))
    return b2
def fonk9(item, root):
    with open(root, "w") as file:
        for obj in item:
            file.write(f"{obj}\n")
        file.write("ENDKEK")
def fonk10(root):
    if not fonk3(root):
        raise class7("File not found")
    with open(root, "b11") as file:
        return "\n".join(file.readlines())
def fonk11(item, root):
    with open(root, "w") as file:
        file.write(item)
def fonk12(_set, map_id, b6 = 0):
    b7 = set()
    for item in _set:
        if item[b6] == map_id:
            b7.add(item)
    _set.difference_update(b7)
    return _set
def fonk13(x, b8 = None, z=False):
    if b8 is None:
        if isinstance(x, int):
            for i in range(x):
                yield i
        elif isinstance(x, dict):
            for key, b4 in x.items():
                yield key, b4
        else:
            for item, n in zip(x, range(len(x))):
                yield item, n
    elif not z:
        for ix in range(x):
            for iy in range(b8):
                yield ix, iy
    elif z:
        for ix in range(x):
            for iy in range(b8):
                yield ix, iy, (ix * x) + iy
class class1:
    @staticmethod
    def fonk14():
        for char in range(26):
            setattr(class1, chr(char + 97).upper(), char + 97)
        for char in range(12):
            setattr(class1, f"F{char + 1}", char + 282)
    @staticmethod
    def fonk15(pop):
        class1.b9 = pop
        for key, b4 in fonk13(pop):
            setattr(class1, b4, key)
    @staticmethod
    def fonk16(k_key):
        k_key -= 48
        return 0 <= k_key <= 9
    @staticmethod
    def fonk17(k_key):
        return k_key - 48
class class2:
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    a5 = 5
def fonk18(b10):
    b10 = int(b10)
    b11 = b10
    b10 -= b11 * (256 ** 3)
    b12 = b10
    b10 -= b12 * (256 ** 2)
    b13 = b10
    b10 -= b13 * 256
    b14 = b10
    return (b11, b12, b13, b14)
def fonk19(b10):
    return sum(b10[i] * (256 ** (3 - i)) for i in range(4))
class class3:
    @staticmethod
    def fonk20(pop):
        for key, b4 in fonk13(pop):
            setattr(class3, key, b4)
class class4(Exception):
    pass
class class5:
    def fonk21(self, k_key, k_mod):
        pass
    def fonk22(self, k_key):
        pass
    def fonk23(self):
        pass
    def fonk24(self):
        pass
    def fonk25(self):
        pass
    def fonk26(self):
        pass
    def fonk27(self):
        pass
class class6:
    def fonk28(self, m_pos, m_key):
        pass
    def fonk29(self):
        pass
    @property
    def fonk30(self):
        return self.b15
    @texture.setter
    def fonk31(self, texture):
        self.b15 = texture
        self.on_change()
class class7(Exception):
    pass
def fonk32(*args):
    pass
def fonk33(key_map, color_map):
    class1.fonk14()
    class1.fonk20(key_map)
    class3.fonk20(color_map)