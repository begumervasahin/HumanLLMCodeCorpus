from collections import defaultdict
class class1:
    def fonk1(self, b2):
        self.b1 = defaultdict(list)
        self.b2 = b2
    def fonk2(self, u, b10):
        self.b1[u].append(b10)
    def fonk3(self, b7, b8):
        b3 = [False] * self.b2
        b4 = [b7]
        b3[b7] = True
        while b4:
            b5 = b4.pop(0)
            print(b5, b6 = " ")
            if b5 = = b8:
                print("Goal found.")
                return
            for neighbor in self.b1[b5]:
                if not b3[neighbor]:
                    b4.append(neighbor)
                    b3[neighbor] = True
        print("Search failed.")
def fonk4():
    with open('input.txt', 'r') as input_file:
        b2 = int(input_file.readline())
        b7 = int(input_file.readline())
        b8 = int(input_file.readline())
        b9 = class1(b2)
        for line in input_file:
            u, b10 = map(int, line.split())
            b9.fonk2(u, b10)
    b9.fonk3(b7, b8)
if b11 = = "__main__":
    fonk4()