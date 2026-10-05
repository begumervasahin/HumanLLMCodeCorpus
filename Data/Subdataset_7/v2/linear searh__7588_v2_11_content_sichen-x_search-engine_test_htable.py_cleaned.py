class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [[] for _ in range(b1)]
    def fonk2(self):
        b3 = []
        for b5 in self.b2:
            for key, value in b5:
                b3.append(f"{key}:{value}")
        return "{" + ", ".join(b3) + "}"
    def fonk3(self, key, value):
        b4 = hash(key) % self.b1
        b5 = self.b2[b4]
        for i, (b6, _) in enumerate(b5):
            if b6 = = key:
                b5[i] = (key, value)
                return
        b5.append((key, value))
    def fonk4(self, key):
        b4 = hash(key) % self.b1
        for b6, v in self.b2[b4]:
            if b6 = = key:
                return v
        raise KeyError(key)
    def fonk5(self, key, value):
        self.fonk3(key, value)
    def fonk6(self):
        b7 = ""
        for i, b5 in enumerate(self.b2):
            b7 += f"{str(i).zfill(4)}->"
            if b5:
                b7 += ", ".join(f"{b6}:{v}" for b6, v in b5)
            b7 += "\n"
        return b7
def fonk7():
    b8 = class1(5)
    assert str(b8) == "{}"
    assert b8.fonk6() ==
def fonk8():
    b8 = class1(5)
    b8["parrt"] = 99
    assert str(b8) == "{parrt:99}"
    assert b8.fonk6() ==
def fonk9():
    b8 = class1(5)
    b8["parrt"] = set([99])
    assert str(b8) == "{parrt:{99}}"
    assert b8.fonk6() ==
def fonk10():
    b8 = class1(5)
    for i in range(1, 11):
        b8[i] = i
    b9 = str(b8)
    assert b9 = = "{1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}"
    b9 = b8.fonk6()
    assert b9 = =
def fonk11():
    b8 = class1(5)
    b8["a"] = "x"
    b8["b"] = "y"
    b8["c"] = "z"
    b8["f"] = "i"
    b8["g"] = "j"
    b8["b6"] = "b6"
    b9 = str(b8)
    assert b9 = = "{a:x, b:y, c:z, f:i, g:j, b6:b6}"
    b9 = b8.fonk6()
    assert b9 = =
def fonk12():
    b8 = class1(5)
    b8["parrt"] = [2, 99, 3942]
    b8["tombu"] = [6, 3, 1024, 99, 102342]
    assert str(b8) == "{parrt:[2, 99, 3942], tombu:[6, 3, 1024, 99, 102342]}"
    assert b8.fonk6() ==
if b10 = = "__main__":
    fonk7()
    fonk8()
    fonk9()
    fonk10()
    fonk11()
    fonk12()
    print("All tests passed!")