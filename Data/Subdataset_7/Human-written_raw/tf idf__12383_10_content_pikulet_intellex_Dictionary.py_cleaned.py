from data_helper import store_data
'''
A dictionary class class1 keeps track of b1 --> document_frequency/ idf, termID/ term_offset.
termID is a sequential value to access the posting list of the term at indexing time
term_offset is the exact position (in bytes) of the term posting list in postings.txt
'''
class class2():
    a1 = 0
    a2 = 0
    a3 = 1
    a4 = 1
    def fonk1(self, b2):
        self.b1 = {}
        self.b2 = b2
        self.a5 = 0
    def fonk2(self, t):
        return t in self.b1
    def fonk3(self, t):
        return self.b1[t][class2.a3]
    def fonk4(self, t, termID):
        self.b1[t] = [1, termID]
    def fonk5(self):
        return self.b1
    def fonk6(self, t):
        self.b1[t][class2.a1] += 1
    def fonk7(self, t, idf):
        self.b1[t][class2.a2] = idf
    def fonk8(self, t, offset):
        self.b1[t][class2.a4] = offset
    def fonk9(self):
        store_data(self.b2, self.b1)