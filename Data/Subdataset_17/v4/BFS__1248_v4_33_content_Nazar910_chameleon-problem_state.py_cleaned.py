from collections import deque
class State:
    def __init__(self, **chameleon_count):
        self.__red_count = chameleon_count['red']
        self.__green_count = chameleon_count['green']
        self.__blue_count = chameleon_count['blue']
        self.__parent = None
    @property
    def red_count(self):
        return self.__red_count
    @property
    def blue_count(self):
        return self.__blue_count
    @property
    def green_count(self):
        return self.__green_count
    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, obj):
        self.__parent = obj
    def has_red_ones(self):
        return bool(self.__red_count)
    def has_only_red_ones(self):
        return self.has_red_ones() and not self.has_green_ones() and not self.has_blue_ones()
    def has_green_ones(self):
        return bool(self.__green_count)
    def has_only_green_ones(self):
        return self.has_green_ones() and not self.has_red_ones() and not self.has_blue_ones()
    def has_blue_ones(self):
        return bool(self.__blue_count)
    def has_only_blue_ones(self):
        return self.has_blue_ones() and not self.has_green_ones() and not self.has_red_ones()
    def has_only_one_color(self):
        return self.has_only_blue_ones() or self.has_only_green_ones() or self.has_only_red_ones()
    def red_meets_green(self):
        if self.__red_count < 1 or self.__green_count < 1:
            raise ValueError('Invalid green or red count')
        return self.__create_new_state(self.__red_count - 1, self.__green_count - 1, self.__blue_count + 2)
    def green_meets_blue(self):
        if self.__blue_count < 1 or self.__green_count < 1:
            raise ValueError('Invalid green or blue count')
        return self.__create_new_state(self.__red_count + 2, self.__green_count - 1, self.__blue_count - 1)
    def blue_meets_red(self):
        if self.__red_count < 1 or self.__blue_count < 1:
            raise ValueError('Invalid blue or red count')
        return self.__create_new_state(self.__red_count - 1, self.__green_count + 2, self.__blue_count - 1)
    def get_path(self):
        path = deque([str(self)])
        parent = self.parent
        while parent:
            path.appendleft(str(parent))
            parent = parent.parent
        return path
    def __create_new_state(self, red, green, blue):
        new_state = State(red=red, green=green, blue=blue)
        new_state.parent = self
        return new_state
    def __str__(self):
        return f'(red={self.red_count}, green={self.green_count}, blue={self.blue_count})'
if __name__ == "__main__":
    initial_state = State(red=13, green=16, blue=17)
    print("Initial state:", initial_state)
    next_state = initial_state.red_meets_green()
    print("Next state:", next_state)
    print("Path to next state:", list(next_state.get_path()))