from time import clock as clk
from time import sleep
from os import path
def test(*args):
    print(clk())
def type_of(text):
    type_map = {
        "int": int,
        "str": str,
        "flt": float,
        "Non": None
    }
    return type_map.get(text)
def root_check(root):
    return path.exists(root)
def load_dict(root, types):
    if not root_check(root):
        return FileNotFoundError
    ret = {}
    with open(root, "r") as f:
        for line in f:
            line = line.strip()
            if line == "ENDKEK":
                return ret
            key, val = line.split(":")
            key, val = types[0](key), types[1](val)
            ret[key] = val
    return ret
def save_dict(item, root):
    with open(root, "w") as f:
        for key, val in item.items():
            f.write(f"{key}:{val}\n")
        f.write("ENDKEK")
def load_set(root):
    if not root_check(root):
        return FileNotFoundError
    ret = []
    with open(root, "r") as f:
        curr = {}
        for line in f:
            line = line.strip()
            if line == "ENDOBJ":
                ret.append(curr)
                curr = {}
            elif line == "ENDKEK":
                return ret
            else:
                cls, attr, val = line.split(".")[0], line.split(":")[0].split(".")[1], line.split(":")[1]
                curr[attr] = type_of(cls)(val)
    return ret
def save_set(root, items):
    with open(root, "w") as f:
        for item in items:
            for key, val in item.items():
                f.write(f"{type(val).__name__[0:3]}.{key}:{val}\n")
            f.write("ENDOBJ\n")
        f.write("ENDKEK\n")
def load_list(root, _type):
    if not root_check(root):
        return FileNotFoundError
    ret = []
    with open(root, "r") as f:
        for line in f:
            line = line.strip()
            if line == "ENDKEK":
                return ret
            ret.append(_type(line))
    return ret
def save_list(item, root):
    with open(root, "w") as f:
        for obj in item:
            f.write(f"{obj}\n")
        f.write("ENDKEK")
def load_string(root):
    if not root_check(root):
        return FileNotFoundError
    with open(root, "r") as f:
        return f.read()
def save_string(item, root):
    with open(root, "w") as f:
        f.write(item)
def exclude(_set, map_id, index=0):
    return {item for item in _set if item[index] != map_id}
def range_gen(x, y=None, z=False):
    if y is None:
        if isinstance(x, int):
            for i in range(x):
                yield i
        elif isinstance(x, dict):
            for key, val in x.items():
                yield key, val
        else:
            for item in x:
                yield item
    elif not z:
        for ix in range(x):
            for iy in range(y):
                yield ix, iy
    else:
        for ix in range(x):
            for iy in range(y):
                yield ix, iy, (ix * y) + iy
class K:
    @staticmethod
    def define_key_map():
        for char in range_gen(26):
            setattr(K, chr(char + 97).upper(), char + 97)
        for char in range_gen(12):
            setattr(K, f"F{char + 1}", char + 282)
    @staticmethod
    def populate(pop):
        K.MAP = pop
        for key, val in pop.items():
            setattr(K, val, key)
    @staticmethod
    def is_number(k_key):
        return 48 <= k_key <= 57
    @staticmethod
    def number(k_key):
        return k_key - 48
class M:
    L_CLICK = 1
    M_CLICK = 2
    R_CLICK = 3
    ROLL_UP = 4
    ROLL_DN = 5
def col(col):
    col = int(col)
    r = col
    col -= r * (256 ** 3)
    g = col
    col -= g * (256 ** 2)
    b = col
    col -= b * 256
    a = col
    return (r, g, b, a)
def col_to_int(col):
    return sum(val * (256 ** (3 - idx)) for idx, val in enumerate(col))
class C:
    @staticmethod
    def populate(pop):
        for key, val in pop.items():
            setattr(C, key, val)
class GAPIError(Exception):
    pass
class SkellyWorld:
    def on_key_down(self, k_key, k_mod):
        pass
    def on_key_up(self, k_key):
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
    def on_click(self, m_pos, m_key):
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
class FileNotFoundError(Exception):
    pass
def pass_function(*args):
    pass
def import_data(key_map, col_map):
    K.define_key_map()
    K.populate(key_map)
    C.populate(col_map)