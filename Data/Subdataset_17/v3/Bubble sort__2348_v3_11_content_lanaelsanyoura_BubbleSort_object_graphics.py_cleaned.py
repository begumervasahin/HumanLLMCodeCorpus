import random
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def find_val(self, value):
        if value < self.data:
            if self.left is None:
                return f"{value} Not Found"
            return self.left.find_val(value)
        elif value > self.data:
            if self.right is None:
                return f"{value} Not Found"
            return self.right.find_val(value)
        else:
            return f"{self.data} is found"
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()
class TextBox:
    def __init__(self, rect_params, rect_fill, text_fill, text_size, text, selected, default):
        self.selected = selected
        self.x, self.y, self.width, self.height = rect_params
        self.rect_fill = rect_fill
        self.text_fill = text_fill
        self.text_size = text_size
        self.text = text
        self.selected_stroke = selected
        self.default_stroke = default
        self.rect_stroke = default
    def draw_box(self):
        transparency = 200 if len(self.rect_fill) == 3 else self.rect_fill[3]
        fill(self.rect_fill[0], self.rect_fill[1], self.rect_fill[2], transparency)
        self.rect_stroke = self.selected_stroke if self.selected else self.default_stroke
        stroke(self.rect_stroke)
        rect(self.x, self.y, self.width, self.height)
        fill(self.text_fill)
        textSize(self.text_size)
        text(self.text, self.x + 5, self.y + 25)
if __name__ == "__main__":
    root = Node(14)
    root.insert(6)
    root.insert(18)
    root.insert(3)
    print(root.find_val(7))
    print(root.find_val(14))
    root.print_tree()
