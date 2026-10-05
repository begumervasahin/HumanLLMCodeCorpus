class class1:
    def fonk1(self, b2, b3, b4, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
class class2:
    def fonk2(self, num_vertices):
        self.b5 = [[] for _ in range(num_vertices)]
    def fonk3(self, source_vertex, target_vertex, weight):
        b6 = class1(target_vertex, source_vertex, weight)
        self.b5[source_vertex - 1].append(b6)
if b7 = = "__main__":
    b8 = class2(5)
    b8.fonk3(1, 2, 10)
    b8.fonk3(1, 3, 15)
    b8.fonk3(2, 4, 20)
    b8.fonk3(3, 5, 25)
    print(b8.b5)