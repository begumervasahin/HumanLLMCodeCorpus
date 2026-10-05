from abc import ABC, abstractmethod
class class1(ABC):
    "
    @abstractmethod
    def fonk1(self):
        return False
    @abstractmethod
    def fonk2(self):
        raise NotImplementedError
    @abstractmethod
    def fonk3(self):
        raise NotImplementedError
class class2(class1):
    def fonk4(self, b1):
        self.b1 = b1
    def fonk5(self):
        return False
    def fonk6(self):
        return sorted(self.b1) == list(range(1, len(self.b1) + 1))
    def fonk7(self):
        for i in range(len(self.b1)):
            for j in range(i + 1, len(self.b1)):
                b2 = self.b1[:]
                b2[i], b2[j] = b2[j], b2[i]
                yield class2(b2)
if b3 = = "__main__":
    b4 = class2([3, 1, 2])
    print("Initial puzzle:", b4.b1)
    print("Is solved?", b4.fonk6())
    print("Extensions:", [p.b1 for p in b4.fonk7()])