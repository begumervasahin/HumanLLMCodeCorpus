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
        return f'Train with {len(self.cars)} cars'
    def bubble_sort(self, to_right=True):
        param = 'coal' if to_right else 'serial'
        reverse = False if to_right else True
        for i in range(len(self.cars)):
            for j in range(len(self.cars) - 1 - i):
                if getattr(self.cars[j], param) > getattr(self.cars[j + 1], param):
                    self.cars[j], self.cars[j + 1] = self.cars[j + 1], self.cars[j]
    def insertion_sort(self, to_right=True):
        param = 'coal' if to_right else 'serial'
        for i in range(1, len(self.cars)):
            current_car = self.cars[i]
            j = i - 1
            while j >= 0 and getattr(self.cars[j], param) > getattr(current_car, param):
                self.cars[j + 1] = self.cars[j]
                j -= 1
            self.cars[j + 1] = current_car
    def binary_search(self, value, to_right=True):
        self.bubble_sort(to_right)
        low, high = 0, len(self.cars) - 1
        while low <= high:
            mid = (low + high)
            if self.cars[mid] == value:
                return self.cars[mid]
            elif self.cars[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return False
    def find_by_serial(self, value):
        self.insertion_sort()
        low, high = 0, len(self.cars) - 1
        while low <= high:
            mid = (low + high)
            if self.cars[mid].serial == value:
                return self.cars[mid]
            elif self.cars[mid].serial < value:
                low = mid + 1
            else:
                high = mid - 1
        return False
    def find(self, value, to_right=True):
        if to_right:
            return self.binary_search(value, to_right=True)
        else:
            return self.binary_search(value, to_right=False)
    def find_by_type(self, value, mytype):
        if mytype == 'coal':
            return self.find(value, to_right=True)
        elif mytype == 'serial':
            return self.find_by_serial(value)
        else:
            try:
                return self.cars[value]
            except IndexError:
                return False
    def destroy(self, car):
        self.cars.remove(car)
        return car
class Depot:
    train = None
    @classmethod
    def generate_train(cls, num_cars):
        cls.train = Train(num_cars)
    @classmethod
    def destroy_train(cls):
        cls.train = None
Depot.generate_train(10)
print(Depot.train)
print(Depot.train.find(5))
Depot.destroy_train()
print(Depot.train)