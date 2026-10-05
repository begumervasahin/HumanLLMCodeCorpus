from typing import Set
class Cell:
    def __init__(self, row: int, col: int, grid: int, value: int, is_immutable: bool = False):
        self.row = row
        self.col = col
        self.grid = grid
        self._value = value
        self.is_immutable = is_immutable
        if self.value == 0:
            self._possibilities = set(range(1, 10))
        else:
            self._possibilities = set()
    @property
    def is_empty(self) -> bool:
        return self.value == 0
    @property
    def value(self) -> int:
        return self._value
    @value.setter
    def value(self, value: int):
        if value in range(0, 10) and not self.is_immutable:
            self._value = value
    @property
    def possibilities(self) -> Set[int]:
        return self._possibilities
    @possibilities.setter
    def possibilities(self, possibilities: Set[int]):
        self._possibilities = possibilities
    def __repr__(self) -> str:
        if self.is_empty:
            return '.'
        else:
            return str(self.value)
if __name__ == "__main__":
    cell = Cell(0, 0, 0, 5)
    print("Initial Cell Value:", cell)
    print("Is Empty:", cell.is_empty)
    print("Possibilities:", cell.possibilities)
    cell.value = 3
    print("\nUpdated Cell Value:", cell)
    print("Is Empty:", cell.is_empty)
    cell.possibilities = {1, 2, 4, 6}
    print("\nUpdated Possibilities:", cell.possibilities)