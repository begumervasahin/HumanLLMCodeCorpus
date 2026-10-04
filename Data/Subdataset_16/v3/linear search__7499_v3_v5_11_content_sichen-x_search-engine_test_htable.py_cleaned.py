class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [[] for _ in range(b1)]
    def fonk2(self, key):
        return hash(key) % self.b1
    def fonk3(self, key, value):
        b3 = self.fonk2(key)
        for item in self.b2[b3]:
            if item[0] == key:
                item[1] = value
                return
        self.b2[b3].append([key, value])
    def fonk4(self):
        b4 = []
        for bucket in self.b2:
            for key, value in bucket:
                b5 = f'set({list(value)})' if isinstance(value, set) else str(value)
                b4.append(f'{key}:{b5}')
        return '{' + ', '.join(b4) + '}'
    def fonk5(self):
        b6 = []
        for i, bucket in enumerate(self.b2):
            b7 = ', '.join(f'{key}:{value}' for key, value in bucket)
            b6.append(f'{i:04}->' + b7)
        return '\n'.join(b6)
def fonk6():
    b2 = class1(5)
    assert str(b2) == "{}"
    assert b2.fonk5() ==
def fonk7():
    b2 = class1(5)
    b2.fonk3("parrt", 99)
    assert str(b2) == "{parrt:99}"
    assert b2.fonk5() ==
def fonk8():
    b2 = class1(5)
    b2.fonk3("parrt", {99})
    assert str(b2) == "{parrt:set([99])}"
    assert b2.fonk5() ==
def fonk9():
    b2 = class1(5)
    for i in range(1, 11):
        b2.fonk3(i, i)
    assert str(b2) == "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    assert b2.fonk5() ==
def fonk10():
    b2 = class1(5)
    b2.fonk3("a", "x")
    b2.fonk3("b", "y")
    b2.fonk3("c", "z")
    b2.fonk3("f", "i")
    b2.fonk3("g", "j")
    b2.fonk3("k", "k")
    assert str(b2) == '{a:x, f:i, k:k, b:y, g:j, c:z}'
    assert b2.fonk5() ==
def fonk11():
    b2 = class1(5)
    b2.fonk3("parrt", [2, 99, 3942])
    b2.fonk3("tombu", [6, 3, 1024, 99, 102342])
    assert str(b2) == "{tombu:[6, 3, 1024, 99, 102342], parrt:[2, 99, 3942]}"
    assert b2.fonk5() ==
def fonk12():
    fonk6()
    fonk7()
    fonk8()
    fonk9()
    fonk10()
    fonk11()
    print("All tests passed!")
fonk12()