class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, b7):
        self.b2.append(b7)
    def fonk3(self):
        return self.b2
class class2:
    def fonk4(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
        self.fonk5()
    def fonk5(self):
        self.b5 = []
        self.b5.append(self.b3[0])
    def fonk6(self, b8):
        self.b5.append(b8)
    def fonk7(self):
        return self.b5.pop(0)
    def fonk8(self):
        return len(self.b5)
    def fonk9(self, b1):
        for b8 in self.b3:
            if b8.b1 = = b1:
                return b8
    def fonk10(self):
        if self.fonk8() == 0:
            raise Exception("The b5 is empty")
    def fonk11(self, b6):
        if b6 = = self.b4:
            raise Exception(f"City found: {b6}")
    def fonk12(self):
        pass
    def fonk13(self, b8):
        for child in b8.fonk3():
            b7 = self.fonk9(child.b1)
            if isinstance(b7, class1):
                self.fonk15(b7)
class class3(class2):
    def fonk14(self):
        while True:
            self.fonk10()
            b8 = self.fonk7()
            self.fonk11(b8.b1)
            self.fonk13(b8)
class class4(class2):
    def fonk15(self, b8):
        self.b5.insert(0, b8)
    def fonk16(self):
        while True:
            self.fonk10()
            b8 = self.fonk7()
            self.fonk11(b8.b1)
            self.fonk13(b8)
def fonk17(b9):
    b3 = {}
    for city, connections in b9.items():
        if city not in b3:
            b3[city] = class1(city)
        for connection in connections:
            if connection not in b3:
                b3[connection] = class1(connection)
            b3[city].fonk2(b3[connection])
    return list(b3.values())
def fonk18():
    b9 = {
        "Tumbes": {"Trujillo": None, "Moyobamba": None, "Iquitos": None},
        "Trujillo": {"Lima": None, "Huancayo": None},
        "Moyobamba": {"Huancayo": None},
        "Iquitos": {"Huancayo": None, "Cusco": None},
        "Lima": {"Nazca": None},
        "Huancayo": {"Arequipa": None, "Puno": None},
        "Nazca": {"Arequipa": None},
        "Puno": {"Arequipa": None},
        "Cusco": {"Arequipa": None},
        "Arequipa": {"Arequipa": None}
    }
    b3 = fonk17(b9)
    print("Breadth-First Search")
    b10 = class3(b3, "Arequipa")
    try:
        b10.fonk16()
    except Exception as e:
        print(e)
    print("\nDepth-First Search")
    b11 = class4(b3, "Arequipa")
    try:
        b11.fonk16()
    except Exception as e:
        print(e)
if b12 = = "__main__":
    fonk18()