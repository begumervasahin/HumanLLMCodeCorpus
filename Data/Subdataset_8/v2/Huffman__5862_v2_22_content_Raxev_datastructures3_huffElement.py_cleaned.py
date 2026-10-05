class Comparable:
    def compare(self, other):
        raise NotImplementedError("Subclasses must implement compare method.")
class HuffElement(Comparable):
    def __init__(self, char):
        self._ch = char
        self._ch_freq = 0
        self._code = ""
    def inc_freq(self):
        self._ch_freq += 1
    def get_freq(self):
        return self._ch_freq
    def set_freq(self, count):
        self._ch_freq = count
    def get_code(self):
        return self._code
    def set_code(self, code):
        self._code = code
    def get_char(self):
        return self._ch
    def set_char(self, char):
        self._ch = char
    def compare(self, other_huff_elem):
        if self._ch_freq > other_huff_elem.get_freq():
            return 1
        elif self._ch_freq < other_huff_elem.get_freq():
            return -1
        else:
            return 0
    def __str__(self):
        return "Character: " + self._ch + ", Code: " + self._code + ", Frequency Count: " + str(self._ch_freq)
if __name__ == "__main__":
    huff_elem = HuffElement('a')
    print(huff_elem)
