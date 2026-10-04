class HuffElement(Comparable):
    def __init__(self, char: str):
        self._char = char
        self._frequency = 0
        self._code = ""
    def increment_frequency(self):
        self._frequency += 1
    @property
    def frequency(self) -> int:
        return self._frequency
    @frequency.setter
    def frequency(self, count: int):
        self._frequency = count
    @property
    def code(self) -> str:
        return self._code
    @code.setter
    def code(self, huffman_code: str):
        self._code = huffman_code
    @property
    def char(self) -> str:
        return self._char
    @char.setter
    def char(self, character: str):
        self._char = character
    def compare(self, other: 'HuffElement') -> int:
        if self._frequency > other.frequency:
            return 1
        elif self._frequency < other.frequency:
            return -1
        return 0
    def __str__(self) -> str:
        return f"Char: {self._char} Code: {self._code} Frequency: {self._frequency}"