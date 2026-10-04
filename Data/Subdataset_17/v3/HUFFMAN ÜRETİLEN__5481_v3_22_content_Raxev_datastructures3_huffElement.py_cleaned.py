class Comparable:
    def compare(self, other):
        raise NotImplementedError("Subclasses should implement this method!")
class HuffElement(Comparable):
    def __init__(self, char: str):
        self.char = char
        self.frequency = 0
        self.code = ""
    def increment_frequency(self) -> None:
        self.frequency += 1
    def compare(self, other: 'HuffElement') -> int:
        if not isinstance(other, HuffElement):
            raise ValueError("Comparison must be with another HuffElement.")
        return (self.frequency > other.frequency) - (self.frequency < other.frequency)
    def __str__(self) -> str:
        return f"Char: '{self.char}', Code: '{self.code}', Frequency: {self.frequency}"
if __name__ == "__main__":
    huff_element = HuffElement('a')
    huff_element.increment_frequency()
    huff_element.code = '101'
    print(huff_element)