
def fonk1(b2, data):
    with open(b2, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
class class1:
    a1 = 0
    a2 = 1
    a3 = 0
    a4 = 1
    def fonk2(self, b2):
        self.b1 = {}
        self.b2 = b2
        self.a5 = 0
    def fonk3(self, term):
        return term in self.b1
    def fonk4(self, term):
        return self.b1[term][class1.a3]
    def fonk5(self, term, term_id):
        self.b1[term] = [1, term_id]
    def fonk6(self):
        return self.b1
    def fonk7(self, term):
        if term in self.b1:
            self.b1[term][class1.a1] += 1
        else:
            self.b1[term] = [1, None]
    def fonk8(self, term, idf):
        self.b1[term][class1.a2] = idf
    def fonk9(self, term, offset):
        self.b1[term][class1.a4] = offset
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