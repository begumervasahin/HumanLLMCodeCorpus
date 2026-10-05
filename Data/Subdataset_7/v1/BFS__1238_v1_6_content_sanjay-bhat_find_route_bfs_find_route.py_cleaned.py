import sys
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                city1, city2, b2 = line.strip().split()
                self.fonk3(city1, city2, int(b2))
                self.fonk3(city2, city1, int(b2))
    def fonk3(self, city1, city2, b2):
        if city1 not in self.b1:
            self.b1[city1] = []
        self.b1[city1].append((city2, b2))
    def fonk4(self, source, destination):
        b3 = [(source, [source])]
        while b3:
            (b4, path) = b3.pop(0)
            if b4 = = destination:
                return path
            for (b11, _) in self.b1.get(b4, []):
                if b11 not in path:
                    b3.append((b11, path + [b11]))
        return None
def fonk5():
    if len(sys.argv) != 4:
        print("Usage: python find_route.py <b5> <b6> <b7>")
        return
    b5 = sys.argv[1]
    b6 = sys.argv[2]
    b7 = sys.argv[3]
    b8 = class1()
    b8.fonk2(b5)
    b9 = b8.fonk4(b6, b7)
    if b9:
        a1 = 0
        b10 = "route:\n"
        for i in range(len(b9) - 1):
            b4 = b9[i]
            b11 = b9[i + 1]
            for (b12, b2) in b8.b1[b4]:
                if b12 = = b11:
                    b10 += f"{b4} to {b11}, {b2} km\n"
                    a1 += b2
                    break
        b10 = f"b2: {a1} km\n" + b10
        print(b10)
    else:
        print("No route found between the given cities.")
if b13 = = "__main__":
    fonk5()