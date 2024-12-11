import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b1 = self.b1
        for start_idx in range(len(b1)):
            b3 = b1[start_idx]
            b4 = start_idx
            for i in range(start_idx + 1, len(b1)):
                if b1[i] < b3:
                    b3 = b1[i]
                    b4 = i
            b1[start_idx], b1[b4] = b1[b4], b1[start_idx]
            if self.b2:
                self.fonk3(start_idx, b4)
        return b1
    def fonk3(self, i, j):
        b1 = [str(elm) + '*' if idx in (i, j) else str(elm) for idx, elm in enumerate(self.b1)]
        b5 = '|' + ' | '.join(b1) + ' |'
        print(b5)
        input("Press Enter to continue...")