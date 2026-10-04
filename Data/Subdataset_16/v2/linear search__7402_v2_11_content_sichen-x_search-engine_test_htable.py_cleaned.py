class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [[] for _ in range(b1)]
    def fonk2(self, key):
        return fonk2(key) % self.b1
    def fonk3(self, key, value):
        b3 = self.fonk2(key)
        for i, (b4, v) in enumerate(self.b2[b3]):
            if b4 = = key:
                self.b2[b3][i] = (key, value)
                return
        self.b2[b3].append((key, value))
    def fonk4(self):
        b5 = [f"{b4}:{v}" for bucket in self.b2 for b4, v in bucket]
        return "{" + ", ".join(b5) + "}"
    def fonk5(self):
        b6 = []
        for i, bucket in enumerate(self.b2):
            b7 = ", ".join(f"{b4}:{v}" for b4, v in bucket)
            b6.append(f"{i:04}->" + b7)
        return "\n".join(b6)
def fonk6(b8, key, value):
    b8.fonk3(key, value)
def fonk7(b8):
    return str(b8)
def fonk8(b8):
    return b8.fonk5()
def fonk9():
    b8 = class1(5)
    assert fonk7(b8) == "{}"
    assert fonk8(b8) ==
def fonk10():
    b8 = class1(5)
    fonk6(b8, "parrt", 99)
    assert fonk7(b8) == "{parrt:99}"
    assert fonk8(b8) ==
def fonk11():
    b8 = class1(5)
    fonk6(b8, "parrt", {99})
    assert fonk7(b8) == "{parrt:{99}}"
    assert fonk8(b8) ==
def fonk12():
    b8 = class1(5)
    for i in range(1, 11):
        fonk6(b8, i, i)
    b9 = fonk7(b8)
    assert b9 = = "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    b9 = fonk8(b8)
    assert b9 = =
def fonk13():
    b8 = class1(5)
    fonk6(b8, "a", "x")
    fonk6(b8, "b", "y")
    fonk6(b8, "c", "z")
    fonk6(b8, "f", "i")
    fonk6(b8, "g", "j")
    fonk6(b8, "b4", "b4")
    b9 = fonk7(b8)
    assert b9 = = "{a:x, f:i, b4:b4, b:y, g:j, c:z}", "found " + b9
    b9 = fonk8(b8)
    assert b9 = =
def fonk14():
    b8 = class1(5)
    fonk6(b8, "parrt", [2, 99, 3942])
    fonk6(b8, "tombu", [6, 3, 1024, 99, 102342])
    assert fonk7(b8) == "{tombu:[6, 3, 1024, 99, 102342], parrt:[2, 99, 3942]}"
    assert fonk8(b8) ==
if b10 = = "__main__":
    fonk9()
    fonk10()
    fonk11()
    fonk12()
    fonk13()
    fonk14()
    print("All tests passed.")