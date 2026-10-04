class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, child_node):
        self.b2.append(child_node)
    def fonk3(self):
        return self.b2
class class2:
    def fonk4(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
        self.b5 = [self.b3[0]]
    def fonk5(self, b7):
        self.b5.append(b7)
    def fonk6(self):
        return self.b5.pop(0)
    def fonk7(self):
        if not self.b5:
            raise Exception("The b5 is empty")
    def fonk8(self, b6):
        if b6 = = self.b4:
            raise Exception(f"City found: {b6}")
    def fonk9(self, b7):
        for child in b7.fonk3():
            self.fonk12(child)
    def fonk10(self):
        pass
class class3(class2):
    def fonk11(self):
        while True:
            self.fonk7()
            b7 = self.fonk6()
            self.fonk8(b7.b1)
            self.fonk9(b7)
class class4(class2):
    def fonk12(self, b7):
        self.b5.insert(0, b7)
    def fonk13(self):
        while True:
            self.fonk7()
            b7 = self.fonk6()
            self.fonk8(b7.b1)
            self.fonk9(b7)
def fonk14(b8):
    b3 = {}
    for city, connections in b8.items():
        if city not in b3:
            b3[city] = class1(city)
        for connection in connections:
            if connection not in b3:
                b3[connection] = class1(connection)
            b3[city].fonk2(b3[connection])
    return list(b3.values())
def fonk15():
    b8 = {
        "Tumbes": ["Trujillo", "Moyobamba", "Iquitos"],
        "Trujillo": ["Lima", "Huancayo"],
        "Moyobamba": ["Huancayo"],
        "Iquitos": ["Huancayo", "Cusco"],
        "Lima": ["Nazca"],
        "Huancayo": ["Arequipa", "Puno"],
        "Nazca": ["Arequipa"],
        "Puno": ["Arequipa"],
        "Cusco": ["Arequipa"],
        "Arequipa": []
    }
    b3 = fonk14(b8)
    print("Breadth-First Search")
    b9 = class3(b3, "Arequipa")
    try:
        b9.fonk13()
    except Exception as e:
        print(e)
    print("\nDepth-First Search")
    b10 = class4(b3, "Arequipa")
    try:
        b10.fonk13()
    except Exception as e:
        print(e)
if b11 = = "__main__":
    fonk15()