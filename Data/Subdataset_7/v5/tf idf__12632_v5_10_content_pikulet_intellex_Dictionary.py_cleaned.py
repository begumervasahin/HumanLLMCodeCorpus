
from data_helper import store_data
class class1:
    a1 = 0
    a2 = 0
    a3 = 1
    a4 = 1
    def fonk1(self, b2):
        self.b1 = {}
        self.b2 = b2
        self.a5 = 0
    def fonk2(self, term):
        return term in self.b1
    def fonk3(self, term):
        return self.b1[term][class1.a3]
    def fonk4(self, term, term_id):
        self.b1[term] = [1, term_id]
    def fonk5(self):
        return self.b1
    def fonk6(self, term):
        self.b1[term][class1.a1] += 1
    def fonk7(self, term, idf):
        self.b1[term][class1.a2] = idf
    def fonk8(self, term, offset):
        self.b1[term][class1.a4] = offset
    def fonk9(self):
        store_data(self.b2, self.b1)