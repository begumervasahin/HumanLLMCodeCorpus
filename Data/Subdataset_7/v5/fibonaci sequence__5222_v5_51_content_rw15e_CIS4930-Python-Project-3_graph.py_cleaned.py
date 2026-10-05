class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
    def fonk2(self, vertex_name):
        if vertex_name in self.b1:
            print(f"A b4 with name '{vertex_name}' already exists.")
        else:
            self.b1.append(vertex_name)
    def fonk3(self, start_vertex, end_vertex):
        if end_vertex not in self.b1:
            self.b1.append(end_vertex)
        if start_vertex not in self.b1:
            self.b1.append(start_vertex)
        if (start_vertex, end_vertex) not in self.b2:
            self.b2.append((start_vertex, end_vertex))
    def fonk4(self, vertex_name):
        if vertex_name in self.b1:
            self.b1.remove(vertex_name)
            self.b2 = [edge for edge in self.b2 if vertex_name not in edge]
        else:
            print(f"Vertex '{vertex_name}' not found.")
    def fonk5(self, start_vertex, end_vertex):
        if (start_vertex, end_vertex) in self.b2:
            self.b2.remove((start_vertex, end_vertex))
        else:
            print(f"Edge '{start_vertex}' -> '{end_vertex}' not found.")
    def fonk6(self):
        print("Vertices:", ", ".join(self.b1))
    def fonk7(self):
        print("Edges:")
        for edge in self.b2:
            print(f"{edge[0]} -> {edge[1]}")
    def fonk8(self, start_vertex, end_vertex):
        return (start_vertex, end_vertex) in self.b2
    def fonk9(self, start_vertex, end_vertex):
        b3 = []
        for b4 in self.b1:
            if b4 = = start_vertex:
                try:
                    b5 = " <-> ".join(self.b1[self.b1.index(b4):self.b1.index(b4) + 6])
                    b3.append(b5)
                except IndexError:
                    pass
        if b3:
            print("\n".join(b3))
class class2(class1):
    def fonk10(self, start_vertex, end_vertex):
        super().fonk10(start_vertex, end_vertex)
        if (end_vertex, start_vertex) not in self.b2:
            self.b2.append((end_vertex, start_vertex))
    def fonk11(self, start_vertex, end_vertex):
        super().fonk11(start_vertex, end_vertex)
        if (end_vertex, start_vertex) in self.b2:
            self.b2.remove((end_vertex, start_vertex))
    def fonk12(self):
        print("Edges:")
        for edge in self.b2:
            print(f"{edge[0]} <-> {edge[1]}")
    def fonk13(self, start_vertex, end_vertex):
        b3 = []
        for b4 in self.b1:
            if b4 = = start_vertex:
                try:
                    b5 = " <-> ".join(self.b1[self.b1.index(b4):self.b1.index(b4) + 6])
                    b3.append(b5)
                except IndexError:
                    pass
        if b3:
            print("\n".join(b3))