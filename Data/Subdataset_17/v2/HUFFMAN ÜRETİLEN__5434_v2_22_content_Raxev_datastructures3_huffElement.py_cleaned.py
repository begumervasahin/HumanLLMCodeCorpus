class Comparable:
    def compare(self, other):
        raise NotImplementedError("Subclasses should implement this method!")
class HuffElement(Comparable):
    def __init__(self, char: str):
        self._char = char
        self._frequency = 0
        self._code = ""
    def increment_frequency(self) -> None:
        self._frequency += 1
    def get_frequency(self) -> int:
        return self._frequency
    def set_frequency(self, frequency: int) -> None:
        self._frequency = frequency
    def get_code(self) -> str:
        return self._code
    def set_code(self, code: str) -> None:
        self._code = code
    def get_char(self) -> str:
        return self._char
    def set_char(self, char: str) -> None:
        self._char = char
    def compare(self, other: 'HuffElement') -> int:
        return (self._frequency > other.get_frequency()) - (self._frequency < other.get_frequency())
    def __str__(self) -> str:
        return f"Char: {self._char} | Code: {self._code} | Frequency: {self._frequency}"
if __name__ == "__main__":
    huff_element = HuffElement('a')
    huff_element.increment_frequency()
    huff_element.set_code('101')
    print(huff_element)