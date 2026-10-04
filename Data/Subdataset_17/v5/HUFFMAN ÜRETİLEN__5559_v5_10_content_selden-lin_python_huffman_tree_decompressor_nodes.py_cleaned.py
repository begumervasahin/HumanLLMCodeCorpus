class HuffmanNode:
    def __init__(self, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right
        self.number = None
    def __eq__(self, other):
        if not isinstance(other, HuffmanNode):
            return False
        return (
            self.symbol == other.symbol and
            self.left == other.left and
            self.right == other.right
        )
    def __lt__(self, other):
        return False
    def __repr__(self):
        return (
            f"HuffmanNode(symbol={self.symbol}, "
            f"left={self.left}, right={self.right})"
        )
    def is_leaf(self):
        return self.left is None and self.right is None
class ReadNode:
    def __init__(self, l_type, l_data, r_type, r_data):
        self.l_type = l_type
        self.l_data = l_data
        self.r_type = r_type
        self.r_data = r_data
    def __repr__(self):
        return (
            f"ReadNode(l_type={self.l_type}, l_data={self.l_data}, "
            f"r_type={self.r_type}, r_data={self.r_data})"
        )
if __name__ == '__main__':
    import doctest
    doctest.testmod()