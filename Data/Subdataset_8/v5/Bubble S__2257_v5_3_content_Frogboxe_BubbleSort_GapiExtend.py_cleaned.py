from time import time as clock
from time import sleep
from os import path
def print_current_time(*args):
    print(clock())
def type_of(text):
    types = {"int": int, "str": str, "flt": float, "Non": Pass}
    return types.get(text)
def root_check(root):
    return path.exists(root)
def load_dictionary(root, types):
    if not root_check(root):
        raise FileNotFound
    ret = dict()
    with open(root, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "ENDKEK":
                return ret
            key, val = line.split(":")
            key, val = types[0](key), types[1](val)
            ret[key] = val
    return ret
def save_dictionary(item, root):
    with open(root, "w") as f:
        for key, val in item.items():
            f.write(f"{key}:{val}\n")
        f.write("ENDKEK")
def load_set(root):
    if not root_check(root):
        raise FileNotFound
    ret = []
    with open(root, "r") as f:
        curr = dict()
        for line in f.readlines():
            line = line.strip()
            if line == "ENDOBJ":
                ret.append(curr)
                curr = dict()
            elif line == "ENDKEK":
                return ret
            else:
                cls, attr, val = (type_of(line.split(".")[0]),
                                  line.split(":")[0].split(".")[1],
                                  line.split(":")[1])
                curr[attr] = cls(val)
def save_set(root, items):
    with open(root, "w") as f:
        for item in items:
            for key, val in item.items():
                f.write(f"{type(val).__name__[0:3]}.{key}:{val}\n")
            f.write("ENDOBJ\n")
        f.write("ENDKEK\n")
def load_list(root, _type):
    if not root_check(root):
        raise FileNotFound
    ret = []
    with open(root, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "ENDKEK":
                return ret
            ret.append(_type(line))
def save_list(item, root):
    with open(root, "w") as f:
        for obj in item:
            f.write(f"{obj}\n")
        f.write("ENDKEK")
def load_string(root):
    if not root_check(root):
        raise FileNotFound
    with open(root, "r") as f:
        ret = "".join(f.readlines())
    return ret
def save_string(item, root):
    with open(root, "w") as f:
        for letter in item:
            f.write(letter)
def exclude(_set, mapID, index=0):
    tmp = set()
    for item in _set:
        if item[index] == mapID:
            tmp.add(item)
    _set -= tmp
    return _set
def generate_range(x, y=None, z=False):
    if y is None:
        if isinstance(x, int):
            yield from range(x)
        elif isinstance(x, dict):
            yield from x.items()
        else:
            for n, item in enumerate(x):
                yield item, n
    elif not z:
        for ix in range(x):
            for iy in range(y):
                yield ix, iy
    elif z:
        for ix in range(x):
            for iy in range(y):
                yield ix, iy, (ix * x) + iy
class KeyMapping:
    @staticmethod
    def define_key_map():
        for char in generate_range(26):
            setattr(KeyMapping, chr(char + 97).upper(), char + 97)
        for char in generate_range(12):
            setattr(KeyMapping, f"F{char + 1}", char + 282)
    @staticmethod
    def populate(pop):
        KeyMapping.MAP = pop
        for key, val in generate_range(pop):
            setattr(KeyMapping, val, key)
    @staticmethod
    def is_number(kKey):
        kKey -= 48
        return 0 <= kKey <= 9
    @staticmethod
    def number(kKey):
        return kKey - 48
class MouseMapping:
    L_CLICK = 1
    M_CLICK = 2
    R_CLICK = 3
    ROLL_UP = 4
    ROLL_DN = 5
def get_color(col):
    col = int(col)
    r = col
    col -= r * (256 ** 3)
    g = col
    col -= g * (256 ** 2)
    b = col
    col -= b * 256
    a = col
    return (r, g, b, a)
def color_to_int(col):
    _int = 0
    for i in range(4):
        _int += col[i] * (256 ** (3 - i))
    return _int
class ColourMapping:
    @staticmethod
    def populate(pop):
        for key, val in generate_range(pop):
            setattr(ColourMapping, key, val)
class GAPIError(Exception):
    pass
class SkellyWorld:
    def on_key_down(self, kKey, kMod):
        pass
    def on_key_up(self, kKey):
        pass
    def on_frame(self):
        pass
    def update(self):
        pass
    def on_logic(self):
        pass
    def pre_init(self):
        pass
    def post_init(self):
        pass
class SkellyElement:
    def on_click(self, mPos, mKey):
        pass
    def update(self):
        pass
    @property
    def texture(self):
        return self._texture
    @texture.setter
    def texture(self, texture):
        self._texture = texture
        self.on_change()
class FileNotFound(Exception):
    pass
def Pass(*args):
    pass
def IMPORT(keyMap, colMap):
    KeyMapping.define_key_map()
    KeyMapping.populate(keyMap)
    ColourMapping.populate(colMap)