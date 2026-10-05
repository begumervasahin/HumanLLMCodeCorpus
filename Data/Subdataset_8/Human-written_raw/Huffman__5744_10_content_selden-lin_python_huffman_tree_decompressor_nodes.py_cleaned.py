
class HuffmanNode:
    def __init__(self, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.left, self.right = left, right
        self.number = None
    def __eq__(self, other):
        return (type(self) == type(other) and self.symbol == other.symbol and
                self.left == other.left and self.right == other.right)
    def __lt__(self, other):
        return False
    def __repr__(self):
        return 'HuffmanNode({}, {}, {})'.format(self.symbol,
                                                self.left, self.right)
    def is_leaf(self):
        return not self.left and not self.right
class ReadNode:
    def __init__(self, l_type, l_data, r_type, r_data):
        self.l_type, self.l_data = l_type, l_data
        self.r_type, self.r_data = r_type, r_data
    def __repr__(self):
        return 'ReadNode({}, {}, {}, {})'.format(
            self.l_type, self.l_data, self.r_type, self.r_data)
if __name__ == '__main__':
    import doctest
    doctest.testmod()