class PorterStemmer:
    def __init__(self):
        self.word = ""
        self.current_index = 0
        self.start_index = 0
        self.end_index = 0
    def is_consonant(self, index):
        if self.word[index] in 'aeiou':
            return False
        if self.word[index] == 'y':
            if index == self.start_index:
                return True
            else:
                return not self.is_consonant(index - 1)
        return True
    def count_consonant_sequences(self):
        count = 0
        index = self.start_index
        while True:
            if index > self.end_index:
                return count
            if not self.is_consonant(index):
                break
            index += 1
        index += 1
        while True:
            while True:
                if index > self.end_index:
                    return count
                if self.is_consonant(index):
                    break
                index += 1
            index += 1
            count += 1
            while True:
                if index > self.end_index:
                    return count
                if not self.is_consonant(index):
                    break
                index += 1
            index += 1
    def has_vowel_in_stem(self):
        for index in range(self.start_index, self.end_index + 1):
            if not self.is_consonant(index):
                return True
        return False
    def has_double_consonant(self, j):
        if j < (self.start_index + 1):
            return False
        if self.word[j] != self.word[j - 1]:
            return False
        return self.is_consonant(j)
    def is_cvc_sequence(self, index):
        if index < (self.start_index + 2) or not self.is_consonant(index) \
                or self.is_consonant(index - 1) or not self.is_consonant(index - 2):
            return False
        ch = self.word[index]
        if ch in 'wx':
            return False
        return True
    def ends_with_string(self, suffix):
        length = len(suffix)
        if suffix[length - 1] != self.word[self.end_index]:
            return False
        if length > (self.end_index - self.start_index + 1):
            return False
        if self.word[self.end_index - length + 1:self.end_index + 1] != suffix:
            return False
        self.current_index = self.end_index - length
        return True
    def replace_suffix(self, replacement):
        length = len(replacement)
        self.word = self.word[:self.end_index + 1] + replacement + self.word[self.end_index + length + 1:]
        self.current_index = self.end_index + length
    def apply_replacement_rule(self, suffix, replacement):
        if self.ends_with_string(suffix):
            self.replace_suffix(replacement)
    def step1ab(self):
        if self.word[self.current_index] == 's':
            if self.ends_with_string("sses"):
                self.current_index -= 2
            elif self.ends_with_string("ies"):
                self.replace_suffix("i")
            elif self.word[self.current_index - 1] != 's':
                self.current_index -= 1
        if self.ends_with_string("eed"):
            if self.count_consonant_sequences() > 0:
                self.current_index -= 1
        elif (self.ends_with_string("ed") or self.ends_with_string("ing")) and self.has_vowel_in_stem():
            self.current_index = self.end_index
            if self.ends_with_string("at"):
                self.replace_suffix("ate")
            elif self.ends_with_string("bl"):
                self.replace_suffix("ble")
            elif self.ends_with_string("iz"):
                self.replace_suffix("ize")
            elif self.has_double_consonant(self.current_index):
                self.current_index -= 1
                ch = self.word[self.current_index]
                if ch in 'lsz':
                    self.current_index += 1
            elif (self.count_consonant_sequences() == 1 and self.is_cvc_sequence(self.current_index)):
                self.replace_suffix("e")
    def step1c(self):
        if (self.ends_with_string("y") and self.has_vowel_in_stem()):
            self.word = self.word[:self.current_index] + 'i' + self.word[self.current_index + 1:]
    def step2(self):
        if self.word[self.current_index - 1] == 'a':
            self.apply_replacement_rule("ational", "ate")
            self.apply_replacement_rule("tional", "tion")
        elif self.word[self.current_index - 1] == 'c':
            self.apply_replacement_rule("enci", "ence")
            self.apply_replacement_rule("anci", "ance")
    def stem(self, word):
        self.word = word
        self.current_index = len(word