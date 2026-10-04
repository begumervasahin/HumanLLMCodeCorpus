class HuffElement:
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
    def frequency(self, value: int):
        self._frequency = value
    @property
    def code(self) -> str:
        return self._code
    @code.setter
    def code(self, value: str):
        self._code = value
    @property
    def char(self) -> str:
        return self._char
    @char.setter
    def char(self, value: str):
        self._char = value
    def compare(self, other: 'HuffElement') -> int:
        if self._frequency > other.frequency:
            return 1
        elif self._frequency < other.frequency:
            return -1
        else:
            return 0
    def __str__(self) -> str:
        return f"Char: '{self._char}', Code: '{self._code}', Frequency: {self._frequency}"