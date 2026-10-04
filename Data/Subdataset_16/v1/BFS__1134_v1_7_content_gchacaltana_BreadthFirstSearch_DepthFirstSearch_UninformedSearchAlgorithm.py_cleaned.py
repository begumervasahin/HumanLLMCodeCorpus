class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, b8):
        self.b2.append(b8)
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
    def fonk6(self, b9):
        self.b5.append(b9)
    def fonk7(self):
        return self.b5.pop(0)
    def fonk8(self):
        return len(self.b5)
    def fonk9(self, b1):
        for b9 in self.b3:
            if b9.b1 = = b1:
                return b9
    def fonk10(self):
        if self.fonk8() == 0:
            raise Exception("The b5 is empty")
    def fonk11(self, b6):
        if b6 = = self.b4:
            raise Exception("City found: %s" % b6)
    def fonk12(self):
        pass
    def fonk13(self, b9):
        b7 = b9.fonk3()
        for child in b7:
            b8 = self.fonk9(child.b1)
            if isinstance(b8, class1):
                self.fonk16(b8)
class class3(class2):
    def fonk14(self, b9):
        self.b5.append(b9)
    def fonk15(self):
        while True:
            self.fonk10()
            b9 = self.fonk7()
            self.fonk11(b9.b1)
            self.fonk13(b9)
class class4(class2):
    def fonk16(self, b9):
        self.b5.insert(0, b9)
    def fonk17(self):
        while True:
            self.fonk10()
            b9 = self.fonk7()
            self.fonk11(b9.b1)
            self.fonk13(b9)
import json
from class1 import class1
from class2 import class3, class4
def fonk18(b11):
    b10 = {}
    for city, connections in b11.items():
        if city not in b10:
            b10[city] = class1(city)
        for connection in connections:
            if connection not in b10:
                b10[connection] = class1(connection)
            b10[city].fonk2(b10[connection])
    return list(b10.values())
def fonk19():
    b11 = {
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
    b10 = fonk18(b11)
    print("Breadth-First Search")
    b12 = class3(b10, "Arequipa")
    try:
        b12.fonk17()
    except Exception as e:
        print(e)
    print("\nDepth-First Search")
    b13 = class4(b10, "Arequipa")
    try:
        b13.fonk17()
    except Exception as e:
        print(e)
if b14 = = "__main__":
    fonk19()