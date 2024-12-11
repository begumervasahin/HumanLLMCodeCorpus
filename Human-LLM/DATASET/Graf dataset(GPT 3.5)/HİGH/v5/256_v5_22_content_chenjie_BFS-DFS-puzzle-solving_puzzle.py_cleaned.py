from abc import ABC, abstractmethod
class class1(ABC):
    @abstractmethod
    def fonk1(self) -> bool:
        return False
    @abstractmethod
    def fonk2(self) -> bool:
        raise NotImplementedError
    @abstractmethod
    def fonk3(self):
        raise NotImplementedError