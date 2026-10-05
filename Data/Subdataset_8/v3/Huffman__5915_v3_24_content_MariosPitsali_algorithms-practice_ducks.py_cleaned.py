class Wing:
    def __init__(self, aspect_ratio):
        self.aspect_ratio = aspect_ratio
    def fly(self):
        if self.aspect_ratio > 1:
            print("Weee, this is fun!")
        elif self.aspect_ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")
class Duck:
    def __init__(self, wing_aspect_ratio=1.8):
        self.wing = Wing(wing_aspect_ratio)
    def walk(self):
        print("Waddle waddle waddle")
    def swim(self):
        print("Come on in the water is lovely")
    def quack(self):
        print("Quack Quack")
    def fly(self):
        self.wing.fly()
class Mallard(Duck):
    pass
class Penguin:
    def __init__(self):
        self.fly = self.aviate
    def walk(self):
        print("Waddle waddle I waddle too")
    def swim(self):
        print("Come on in but it's a bit chilly this far south")
    def quack(self):
        print("Are you having a laugh on a penguin?")
    def aviate(self):
        print("I won the lottery and bought a learjet")
class Flock:
    def __init__(self):
        self.ducks = []
    def add_duck(self, duck: Duck) -> None:
        if isinstance(duck, Duck):
            self.ducks.append(duck)
        else:
            raise TypeError(f"Cannot add duck, expected Duck instance, got {type(duck).__name__}")
    def migrate(self):
        for duck in self.ducks:
            duck.fly()
            print("One duck down")
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()
if __name__ == "__main__":
    donald = Duck()
    donald.fly()