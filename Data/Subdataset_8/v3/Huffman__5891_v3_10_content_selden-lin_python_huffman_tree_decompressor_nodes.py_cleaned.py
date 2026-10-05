class HuffmanNode:
    def __init__(self, symbol=None, left=None, right=None) -> None:
        self.symbol = symbol
        self.left = left
        self.right = right
        self.number = None
    def __eq__(self, other: object) -> bool:
        return (
            type(self) == type(other)
            and self.symbol == other.symbol
            and self.left == other.left
            and self.right == other.right
        )
    def __lt__(self, other: object) -> bool:
        return False
    def __repr__(self) -> str:
        return f'HuffmanNode({self.symbol}, {self.left}, {self.right})'
    def is_leaf(self) -> bool:
        return not self.left and not self.right
class ReadNode:
    def __init__(self, l_type: str, l_data: object, r_type: str, r_data: object) -> None:
        self.l_type = l_type
        self.l_data = l_data
        self.r_type = r_type
        self.r_data = r_data
    def __repr__(self) -> str:
        return f'ReadNode({self.l_type}, {self.l_data}, {self.r_type}, {self.r_data})'
if __name__ == '__main__':
    import doctest
    doctest.testmod()