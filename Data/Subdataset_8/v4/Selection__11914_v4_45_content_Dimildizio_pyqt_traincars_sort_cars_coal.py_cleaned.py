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
        return f'Train with {len(self.cars)} cars'
    def add_car(self, item, num):
        if item == 'coal':
            car = Car(num, randint(1, 1000))
        else:
            car = Car(randint(1, 74), num)
        self.cars.append(car)
        return car
    def bubble_sort_to_right(self, param=True):
        pass
    def bubble_sort_to_left(self, param=True):
        pass
    def insertion_sort_to_right(self, param=True):
        pass
    def insertion_sort_to_left(self, param=True):
        pass
    def select_sort_to_right(self, param=True):
        pass
    def select_sort_to_left(self, param=True):
        pass
    def binary_search_to_right(self, value):
        pass
    def binary_search_to_left(self, value):
        pass
    def find_sn(self, value):
        pass
    def find(self, value, side=True):
        pass
    def find_by_type(self, value, mytype):
        pass
    def destroy(self, car):
        self.cars.remove(car)
        return car
class Depot:
    train = None
    @classmethod
    def generate(cls, value):
        cls.train = Train(value)
    @classmethod
    def boom(cls):
        cls.train = None