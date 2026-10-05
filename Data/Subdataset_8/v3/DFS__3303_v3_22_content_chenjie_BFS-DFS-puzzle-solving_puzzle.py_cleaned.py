from abc import ABC, abstractmethod
class Puzzle(ABC):
    @abstractmethod
    def fail_fast(self):
        return False
    @abstractmethod
    def is_solved(self):
        raise NotImplementedError
    @abstractmethod
    def extensions(self):
        raise NotImplementedError
class NumberPuzzle(Puzzle):
    def __init__(self, numbers):
        self.numbers = numbers
    def fail_fast(self):
        return False
    def is_solved(self):
        return sorted(self.numbers) == list(range(1, len(self.numbers) + 1))
    def extensions(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                new_numbers = self.numbers[:]
                new_numbers[i], new_numbers[j] = new_numbers[j], new_numbers[i]
                yield NumberPuzzle(new_numbers)
if __name__ == "__main__":
    initial_puzzle = NumberPuzzle([3, 1, 2])
    print("Initial puzzle:", initial_puzzle.numbers)
    print("Is solved?", initial_puzzle.is_solved())
    print("Extensions:", [p.numbers for p in initial_puzzle.extensions()])