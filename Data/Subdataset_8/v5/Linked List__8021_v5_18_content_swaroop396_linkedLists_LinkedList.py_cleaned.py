class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(new_node)
    def display(self):
        current = self.head
        while current:
            print(current.get_data(), end=" ")
            current = current.get_next()
            if current:
                print("-->", end=" ")
        print()
    def length(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        return size
    def index(self, data):
        current = self.head
        position = 0
        while current:
            if current.get_data() == data:
                return position
            else:
                position += 1
                current = current.get_next()
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return found
    def max_value(self):
        current = self.head
        max_val = current.get_data()
        while current:
            if current.get_data() > max_val:
                max_val = current.get_data()
            current = current.get_next()
        return max_val
    def min_value(self):
        current = self.head
        min_val = current.get_data()
        while current:
            if current.get_data() < min_val:
                min_val = current.get_data()
            current = current.get_next()
        return min_val
    def push(self, data):
        self.add_to_end(data)
    def pop(self):
        current = self.head
        previous = None
        while current.get_next():
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = None
        else:
            previous.set_next(None)
            data = current.get_data()
            del current
            return data
    def at_index(self, position):
        current = self.head
        pos = 0
        while pos != position:
            current = current.get_next()
            pos += 1
        return current.get_data()
    def copy(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.add_to_end(current.get_data())
            current = current.get_next()
        return new_list
    def clear(self):
        self.head = None
    def remove_position(self, position):
        data = self.at_index(position)
        self.remove(data)
        return data
    def to_string(self, separator=""):
        current = self.head
        result = ""
        while current:
            result += str(current.get_data())
            current = current.get_next()
            if current:
                result += separator
        return result
    def count(self, element):
        current = self.head
        count = 0
        while current:
            if current.get_data() == element:
                count += 1
            current = current.get_next()
        return count
    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result
    def to_set(self):
        current = self.head
        result = set()
        while current:
            result.add(current.get_data())
            current = current.get_next()
        return result
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_node
        self.head = prev
    def sort(self):
        current = self.head
        while current:
            min_node = current
            next_node = current.get_next()
            while next_node:
                if next_node.get_data() < min_node.get_data():
                    min_node = next_node
                next_node = next_node.get_next()
            temp = current.get_data()
            current.update_data(min_node.get_data())
            min_node.update_data(temp)
            current = current.get_next()
    def sorted(self):
        new_list = self.copy()
        new_list.sort()
        return new_list
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def update_data(self, data):
        self.data = data
    def set_next(self, node):
        self.next_node = node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
myList = LinkedList()
myList.add_to_start(5)
myList.add_to_start(4)
myList.add_to_start(3)
myList.add_to_start(2)
myList.add_to_start(1)
myList.display()
myList.add_to_end(12)
myList.add_to_end(13)
myList.add_to_end(3)
myList.display()
print(myList.length())
print(myList.index(3))
print(myList.at_index(5))
print(myList.remove(12))
myList.remove_position(2)
myList.display()
print(myList.max_value())
print(myList.min_value())
myList.push(31)
myList.display()
print(myList.pop())
myList.display()
myList2 = myList.copy()
myList2.display()
myList2.clear()
myList2.display()
print(myList.to_string(","))
print(myList.count(3))
new_list = myList.to_list()
print(new_list)
new_set = myList.to_set()
print(new_set)
myList.reverse()
myList.display()
myList3 = myList.sorted()
myList3.display()
myList.sort()
myList.display()