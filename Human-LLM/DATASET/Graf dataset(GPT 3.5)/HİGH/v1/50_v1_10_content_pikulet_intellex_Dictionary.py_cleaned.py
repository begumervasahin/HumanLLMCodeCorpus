
def fonk1(file_path, data):
    with open(file_path, 'w') as b2:
        for key, value in data.items():
            b2.write(f"{key}: {value}\n")
class class1:
    a1 = 0
    a2 = 0
    a3 = 1
    a4 = 1
    def fonk2(self, b2):
        self.b1 = {}
        self.b2 = b2
        self.a5 = 0
    def fonk3(self, t):
        return t in self.b1
    def fonk4(self, t):
        return self.b1[t][class1.a3]
    def fonk5(self, t, termID):
        self.b1[t] = [1, termID]
    def fonk6(self):
        return self.b1
    def fonk7(self, t):
        if t in self.b1:
            self.b1[t][class1.a1] += 1
        else:
            self.b1[t] = [1, None]
    def fonk8(self, t, idf):
        self.b1[t][class1.a2] = idf
    def fonk9(self, t, offset):
        self.b1[t][class1.a4] = offset
    def fonk10(self):
        fonk1(self.b2, self.b1)
if b3 = = "__main__":
    b4 = class1("terms_data.txt")
    b1 = ["apple", "banana", "orange"]
    for idx, term in enumerate(b1):
        b4.fonk5(term, idx)
    for term in b1:
        b4.fonk7(term)
    b4.fonk8("apple", 0.5)
    b4.fonk9("apple", 100)
    b4.fonk10()