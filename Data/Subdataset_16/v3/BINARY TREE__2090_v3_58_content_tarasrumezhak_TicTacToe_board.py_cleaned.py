from typing import Union, List, Tuple
class class1:
    def fonk1(self):
        self.b1 = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = "O"
        self.b6 = "X"
    def fonk2(self) -> Union[None, str]:
        def fonk3(lst: List[Union[None, str]]) -> bool:
            return all(b7 = = lst[0] and b7 is not None for b7 in lst)
        for i in range(3):
            if fonk3(self.b1[i]):
                return self.b1[i][0]
            if fonk3([self.b1[0][i], self.b1[1][i], self.b1[2][i]]):
                return self.b1[0][i]
        if fonk3([self.b1[0][0], self.b1[1][1], self.b1[2][2]]):
            return self.b1[0][0]
        if fonk3([self.b1[2][0], self.b1[1][1], self.b1[0][2]]):
            return self.b1[2][0]
        if not self.fonk8():
            return 'Draw!'
        return None
    def fonk4(self) -> str:
        b8 = "------------- y:\n"
        for i in range(3):
            b8 += "| "
            for j in range(3):
                b8 += (self.b1[i][j] or " ") + " | "
            b8 += f"{i + 1}\n-------------\n"
        b8 += "b7: 1   2   3"
        return b8
    def fonk5(self, sign: str, b7: int, y: int):
        if 1 <= b7 <= 3 and 1 <= y <= 3:
            if self.b1[b7 - 1][y - 1] is not None:
                raise IndexError("The position is already used")
            self.b1[b7 - 1][y - 1] = sign
        else:
            raise IndexError("Out of bounds")
    def fonk6(self, coords: Tuple[int, int]) -> bool:
        return self.b1[coords[0]][coords[1]] is None
    def fonk7(self) -> List[Tuple[int, int]]:
        return [(row + 1, col + 1) for row in range(3) for col in range(3) if self.fonk6((row, col))]
    def fonk8(self) -> bool:
        return any(self.fonk6((row, col)) for row in range(3) for col in range(3))
if b9 = = '__main__':
    b1 = class1()
    b1.fonk5("O", 1, 1)
    b1.fonk5("O", 2, 2)
    b1.fonk5("O", 3, 3)
    print(b1)
    print(b1.fonk2())
    print(b1.fonk7())