from random import randint, choice
class Car:
    def __init__(self, coal, serial):
        self.serial = serial
        self.coal = coal
    def __repr__(self):
        return f'Car(coal={self.coal}, serial={self.serial})'
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
        cars_info = '\n'.join([f'\t{car}' for car in self.cars])
        return f'This is a train with {len(self.cars)} cars:\n{cars_info}'
    def add_car(self, item, num):
        if item == 'coal':
            car = Car(num, randint(1, 1000))
        else:
            car = Car(randint(1, 74), num)
        self.cars.append(car)
        return car
    def bubble_sort_to_right(self, sort_by_coal=True):
        attribute = 'coal' if sort_by_coal else 'serial'
        for i in range(len(self.cars) - 1, 0, -1):
            end = True
            for j in range(i):
                if getattr(self.cars[j], attribute) > getattr(self.cars[j + 1], attribute):
                    self.cars[j], self.cars[j + 1] = self.cars[j + 1], self.cars[j]
                    end = False
            if end:
                break
class Depot:
    train = None
    @classmethod
    def generate(cls, value):
        cls.train = Train(value)
    @classmethod
    def boom(cls):
        cls.train = None