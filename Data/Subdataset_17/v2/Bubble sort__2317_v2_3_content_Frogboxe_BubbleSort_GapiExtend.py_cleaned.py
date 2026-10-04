from time import perf_counter as clk
from os import path
def test(*args):
    print(clk())
def type_of(text):
    if text == "int":
        return int
    elif text == "str":
        return str
    elif text == "flt":
        return float
    elif text == "Non":
        return pass_function
def root_check(root):
    return path.exists(root)
def load_dict(root, types):
    if not root_check(root):
        raise FileNotFoundError("File not found")
    result = {}
    with open(root, "r") as file:
        for line in file.readlines():
            line = line.strip()
            if line == "ENDKEK":
                return result
            key, val = line.split(":")
            key, val = types[0](key), types[1](val)
            result[key] = val
    return result
def save_dict(item, root):
    with open(root, "w") as file:
        for key, val in range_iter(item):
            file.write(f"{key}:{val}\n")
        file.write("ENDKEK")
def load_set(root):
    if not root_check(root):
        raise FileNotFoundError("File not found")
    result = []
    with open(root, "r") as file:
        current = {}
        for line in file.readlines():
            line = line.strip()
            if line == "ENDOBJ":
                result.append(current)
                current = {}
            elif line == "ENDKEK":
                return result
            else:
                cls, attr, val = (type_of(line.split(".")[0]),
                                  line.split(":")[0].split(".")[1],
                                  line.split(":")[1])
                current[attr] = cls(val)
    return result
def save_set(root, items):
    with open(root, "w") as file:
        for item in items:
            for key, val in range_iter(item):
                file.write(f"{type(val).__name__[:3]}.{key}:{val}\n")
            file.write("ENDOBJ\n")
        file.write("ENDKEK\n")
def load_list(root, _type):
    if not root_check(root):
        raise FileNotFoundError("File not found")
    result = []
    with open(root, "r") as file:
        for line in file.readlines():
            line = line.strip()
            if line == "ENDKEK":
                return result
            result.append(_type(line))
    return result
def save_list(item, root):
    with open(root, "w") as file:
        for obj in item:
            file.write(f"{obj}\n")
        file.write("ENDKEK")
def load_string(root):
    if not root_check(root):
        raise FileNotFoundError("File not found")
    with open(root, "r") as file:
        return "\n".join(file.readlines())
def save_string(item, root):
    with open(root, "w") as file:
        for letter in item:
            file.write(letter)
def exclude(_set, map_id, index=0):
    temp = set()
    for item in _set:
        if item[index] == map_id:
            temp.add(item)
    for item in temp:
        _set.remove(item)
    return _set
def range_iter(x, y=None, z=False):
    if y is None:
        if isinstance(x, int):
            for i in range(x):
                yield i
        elif isinstance(x, dict):
            for key, val in x.items():
                yield key, val
        else:
            for item, n in zip(x, range(len(x))):
                yield item, n
    elif not z:
        for ix in range(x):
            for iy in range(y):
                yield ix, iy
    elif z:
        for ix in range(x):
            for iy in range(y):
                yield ix, iy, (ix * x) + iy
class KeyMapper:
    @staticmethod
    def define_key_map():
        for char in range(26):
            setattr(KeyMapper, chr(char + 97).upper(), char + 97)
        for char in range(12):
            setattr(KeyMapper, f"F{char + 1}", char + 282)
    @staticmethod
    def populate(pop):
        KeyMapper.MAP = pop
        for key, val in range_iter(pop):
            setattr(KeyMapper, val, key)
    @staticmethod
    def is_number(k_key):
        k_key -= 48
        return 0 <= k_key <= 9
    @staticmethod
    def number(k_key):
        return k_key - 48
class MouseMapper:
    L_CLICK = 1
    M_CLICK = 2
    R_CLICK = 3
    ROLL_UP = 4
    ROLL_DN = 5
def color_to_rgba(col):
    col = int(col)
    r = col
    col -= r * (256 ** 3)
    g = col
    col -= g * (256 ** 2)
    b = col
    col -= b * 256
    a = col
    return (r, g, b, a)
def rgba_to_int(col):
    return sum(col[i] * (256 ** (3 - i)) for i in range(4))
class ColorMapper:
    @staticmethod
    def populate(pop):
        for key, val in range_iter(pop):
            setattr(ColorMapper, key, val)
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
def import_key_and_color_maps(key_map, color_map):
    KeyMapper.define_key_map()
    KeyMapper.populate(key_map)
    ColorMapper.populate(color_map)