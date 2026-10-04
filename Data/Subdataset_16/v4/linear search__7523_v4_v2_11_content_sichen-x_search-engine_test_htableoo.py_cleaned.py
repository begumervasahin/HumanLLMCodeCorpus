class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [[] for _ in range(b1)]
    def fonk2(self):
        b3 = []
        for bucket in self.b2:
            for key, value in bucket:
                b3.append(f"{key}:{value}")
        return "{" + ", ".join(b3) + "}"
    def fonk3(self):
        b4 = ""
        for i, bucket in enumerate(self.b2):
            b4 += f"{str(i).zfill(4)} -> "
            if bucket:
                b3 = ", ".join([f"{key}:{value}" for key, value in bucket])
                b4 += b3
            b4 += "\n"
        return b4
    def fonk4(self, key):
        return hash(key) % self.b1
    def fonk5(self, key, value):
        b5 = self.fonk4(key)
        for i, (b6, existing_value) in enumerate(self.b2[b5]):
            if b6 = = key:
                self.b2[b5][i] = (key, value)
                return
        self.b2[b5].append((key, value))
def fonk6():
    b7 = class1(5)
    assert str(b7) == "{}"
    assert b7.fonk3() ==
def fonk7():
    b7 = class1(5)
    b7.fonk5("parrt", 99)
    assert str(b7) == "{parrt:99}"
    assert b7.fonk3() ==
def fonk8():
    b7 = class1(5)
    for i in range(1, 11):
        b7.fonk5(i, i)
    b8 = str(b7)
    assert b8 = = "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    b8 = b7.fonk3()
    assert b8 = =
def fonk9():
    b7 = class1(5)
    b7.fonk5("parrt", {2, 99, 3942})
    b7.fonk5("tombu", {6, 3, 1024, 99, 102342})
    assert str(b7) == "{tombu:{1024, 99, 3, 102342, 6}, parrt:{2, 99, 3942}}"
    assert b7.fonk3() ==
if b9 = = "__main__":
    fonk6()
    fonk7()
    fonk8()
    fonk9()
    print("All tests passed!")