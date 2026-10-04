class Wing:
    def __init__(self, ratio: float) -> None:
        self.ratio = ratio
    def fly(self) -> None:
        if self.ratio > 1:
            print("Weee, this is fun!")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying.")
        else:
            print("I think I'll just walk.")
class Duck:
    def __init__(self) -> None:
        self._wing = Wing(1.8)
    def walk(self) -> None:
        print("Waddle, waddle, waddle.")
    def swim(self) -> None:
        print("Come on in, the water is lovely.")
    def quack(self) -> None:
        print("Quack, quack!")
    def fly(self) -> None:
        self._wing.fly()
class Mallard(Duck):
    pass
class Penguin:
    def __init__(self) -> None:
        self.fly = self.aviate
    def walk(self) -> None:
        print("Waddle, waddle, I waddle too.")
    def swim(self) -> None:
        print("Come on in, but it's a bit chilly this far south.")
    def quack(self) -> None:
        print("Are you having a laugh? I'm a penguin!")
    def aviate(self) -> None:
        print("I won the lottery and bought a Learjet!")
class Flock:
    def __init__(self) -> None:
        self.flock = []
    def add_duck(self, duck: Duck) -> None:
        if callable(getattr(duck, "fly", None)):
            self.flock.append(duck)
        else:
            raise TypeError(f"Cannot add {type(duck).__name__}, it doesn't fly!")
    def migrate(self) -> None:
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down.")
                problem = e
        if problem:
            raise problem
def test_duck(duck: Duck) -> None:
    duck.walk()
    duck.swim()
    duck.quack()
if __name__ == "__main__":
    donald = Duck()
    donald.fly()