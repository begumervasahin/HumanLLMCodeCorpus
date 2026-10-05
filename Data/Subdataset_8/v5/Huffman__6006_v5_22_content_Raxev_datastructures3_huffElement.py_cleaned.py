from comparable import Comparable
class HuffElement(Comparable):
    def __init__(self, char):
        self.character = char
        self.frequency = 0
        self.code = ""
    def increment_frequency(self):
        self.frequency += 1
    def get_frequency(self):
        return self.frequency
    def set_frequency(self, count):
        self.frequency = count
    def get_huffman_code(self):
        return self.code
    def set_huffman_code(self, code):
        self.code = code
    def get_character(self):
        return self.character
    def set_character(self, char):
        self.character = char
    def compare(self, other_huff_elem):
        if self.frequency > other_huff_elem.get_frequency():
            return 1
        elif self.frequency < other_huff_elem.get_frequency():
            return -1
        else:
            return 0
    def __str__(self):
        return f"Character: {self.character}, Code: {self.code}, Frequency: {self.frequency}"