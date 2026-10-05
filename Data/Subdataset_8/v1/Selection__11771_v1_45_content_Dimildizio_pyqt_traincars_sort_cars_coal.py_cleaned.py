from random import randint, choice
class Car:
    def __init__(self, coal, serial):
        self.serial = serial
        self.coal = coal
    def __repr__(self):
        return f'Car(serial={self.serial}, coal={self.coal})'
    def __eq__(self, another):
        return self.coal == another
    def __gt__(self, another):
        return self.coal > another
    def __lt__(self, another):
        return self.coal < another
    def __ge__(self, another):
        return self.coal >= another
    def __le__(self, another):
        return self.coal <= another
    def __ne__(self, another):
        return self.coal != another
class Train:
    def __init__(self, cars):
        self.cars = [Car(randint(1, 74), randint(1, 1000)) for _ in range(cars)]
    def __repr__(self):
        text = f'This is a train with {len(self.cars)} cars: '
        for car in self.cars:
            text += '\n\t' + str(car)
        return text
    def add_car(self, item, num):
        if item == 'coal':
            car = Car(num, randint(1, 1000))
        else:
            car = Car(randint(1, 74), num)
        self.cars.append(car)
        return car
class Depot:
    train = None
    @classmethod
    def generate(cls, value):
        cls.train = Train(value)
    @classmethod
    def boom(cls):
        cls.train = None
