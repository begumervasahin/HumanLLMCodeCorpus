class Wing:
    def __init__(self, ratio: float):
        self.ratio = ratio
    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun!")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")
class Duck:
    def __init__(self, wing_ratio: float = 1.8):
        self._wing = Wing(wing_ratio)
    def walk(self):
        print("Waddle waddle waddle")
    def swim(self):
        print("Come on in, the water is lovely")
    def quack(self):
        print("Quack Quack")
    def fly(self):
        self._wing.fly()
class Mallard(Duck):
    pass
class Penguin:
    def __init__(self):
        self.fly = self.aviate
    def walk(self):
        print("Waddle waddle, I waddle too")
    def swim(self):
        print("Come on in, but it's a bit chilly this far south")
    def quack(self):
        print("Are you having a laugh? I'm a penguin!")
    def aviate(self):
        print("I won the lottery and bought a Learjet")
class Flock:
    def __init__(self):
        self._ducks = []
    def add_duck(self, duck: Duck) -> None:
        if hasattr(duck, 'fly') and callable(duck.fly):
            self._ducks.append(duck)
        else:
            raise TypeError(f"Cannot add duck, are you sure it is not a {type(duck).__name__}?")
    def migrate(self):
        problem = None
        for duck in self._ducks:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem
def test_duck(duck: Duck):
    duck.walk()
    duck.swim()
    duck.quack()
if __name__ == "__main__":
    donald = Duck()
    donald.fly()