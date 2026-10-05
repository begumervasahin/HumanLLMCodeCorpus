from abc import ABC, abstractmethod
class Puzzle(ABC):
    @abstractmethod
    def fail_fast(self) -> bool:
        return False
    @abstractmethod
    def is_solved(self) -> bool:
        raise NotImplementedError
    @abstractmethod
    def extensions(self):
        raise NotImplementedError