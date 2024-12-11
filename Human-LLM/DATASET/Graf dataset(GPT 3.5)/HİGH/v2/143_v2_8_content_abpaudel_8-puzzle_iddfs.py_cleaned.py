import itertools
class class1:
    b1 = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    def fonk1(self, b3, b2 = None):
        self.b3 = b3
        self.b2 = b2
        self.b4 = 0 if b2 is None else b2.b4 + 1
    def fonk2(self):
        return self.b3 = = self.b1
    def fonk3(self):
        b5 = []
        i, b6 = next((i, b6) for i, row in enumerate(self.b3) for b6, val in enumerate(row) if val == 0)
        b7 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in b7:
            x, b8 = i + move[0], b6 + move[1]
            if 0 <= x < 3 and 0 <= b8 < 3:
                b9 = [row.copy() for row in self.b3]
                b9[i][b6], b9[x][b8] = b9[x][b8], b9[i][b6]
                b5.append(class1(b9, self))
        return b5
class class2:
    def fonk4(self, b10):
        self.b10 = class1(b10)
        self.b11 = None
        self.b12 = set()
    def fonk5(self, b14):
        b13 = []
        while b14:
            b13.append(b14.b3)
            b14 = b14.b2
        self.b11 = b13[::-1]
    def fonk6(self):
        raise NotImplementedError("class2 class class3 implement fonk9() method")
class class4(class2):
    def fonk7(self, b10):
        super().fonk7(b10)
        self.b15 = []
    def fonk8(self, limit):
        self.b15.append(self.b10)
        while self.b15:
            b16 = self.b15.pop()
            self.b12.add(tuple(b16.b3))
            if b16.fonk2():
                self.fonk5(b16)
                return self.b11
            if b16.b4 < limit:
                for neighbor in b16.fonk3()[::-1]:
                    if tuple(neighbor.b3) not in self.b12:
                        self.b15.append(neighbor)
                        self.b12.add(tuple(neighbor.b3))
        return None
    def fonk9(self):
        for i in itertools.count():
            self.b15 = []
            self.b12 = set()
            self.b15.append(self.b10)
            b17 = self.fonk8(i)
            if b17 is not None:
                break
        return b17
def fonk10(b19):
    b10 = [[int(num) for num in row.split(',')] for row in b19.split()]
    return b10
def fonk11(output_file, b11):
    with open(output_file, 'w') as file:
        for b3 in b11:
            for row in b3:
                file.write(','.join(map(str, row)) + '\n')
            file.write('\n')
def fonk12(b18, b19):
    b18 = b18
    b19 = b19
    b10 = fonk10(b19)
    b20 = class4(b10)
    b11 = b20.fonk9()
    if b11:
        fonk11(f"{b18}_output.txt", b11)
        print("Solution found and written to output file.")
    else:
        print("No b11 found for the given initial b3.")
if b21 = = "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py b18 b10")
        sys.exit(1)
    b18 = sys.argv[1]
    b19 = sys.argv[2]
    fonk12(b18, b19)