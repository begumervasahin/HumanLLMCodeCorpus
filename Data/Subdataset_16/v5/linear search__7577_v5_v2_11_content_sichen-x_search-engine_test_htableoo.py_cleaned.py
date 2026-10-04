class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [[] for _ in range(b1)]
    def fonk2(self):
        b3 = [f"{key}:{value}" for bucket in self.b2 for key, value in bucket]
        return "{" + ", ".join(b3) + "}"
    def fonk3(self):
        b4 = ""
        for b5, bucket in enumerate(self.b
 b4 += f"{str(b5).zfill(4)} -> "
            if bucket:
                b4 += ", ".join(f"{key}:{value}" for key, value in bucket)
            b4 += "\n"
        return b4
    def fonk4(self, key):
        return hash(key) % self.b1
    def fonk5(self, key, value):
        b5 = self.fonk4(key)
        for i, (b6, _) in enumerate(self.b2[b5]):
            if b6 = = key:
                self.b2[b5][i] = (key, value)
                return
        self.b2[b5].append((key, value))
def fonk6():
    b7 = class1(5)
    assert str(b7) == "{}"
    assert b7.fonk3() == "0000 ->\n0001 ->\n0002 ->\n0003 ->\n0004 ->\n"
def fonk7():
    b7 = class1(5)
    b7.fonk5("parrt", 99)
    assert str(b7) == "{parrt:99}"
    assert b7.fonk3() == "0000 ->\n0001 ->\n0002 ->\n0003 -> parrt:99\n0004 ->\n"
def fonk8():
    b7 = class1(5)
    for i in range(1, 11):
        b7.fonk5(i, i)
    assert str(b7) == "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    assert b7.fonk3() == (
        "0000 -> 5:5, 10:10\n"
        "0001 -> 1:1, 6:6\n"
        "0002 -> 2:2, 7:7\n"
        "0003 -> 3:3, 8:8\n"
        "0004 -> 4:4, 9:9\n"
    )
def fonk9():
    b7 = class1(5)
    b7.fonk5("parrt", {2, 99, 3942})
    b7.fonk5("tombu", {6, 3, 1024, 99, 102342})
    assert str(b7) == "{tombu:{1024, 99, 3, 102342, 6}, parrt:{2, 99, 3942}}"
    assert b7.fonk3() == (
        "0000 ->\n"
        "0001 -> tombu:{1024, 99, 3, 102342, 6}\n"
        "0002 ->\n"
        "0003 -> parrt:{2, 99, 3942}\n"
        "0004 ->\n"
    )
if b8 = = "__main__":
    fonk6()
    fonk7()
    fonk8()
    fonk9()
    print("All tests passed!")