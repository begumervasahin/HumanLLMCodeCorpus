class PorterStemmer:
    def __init__(self):
        self.b = ""
        self.k = 0
        self.k0 = 0
        self.j = 0
    def cons(self, i):
        if self.b[i] in 'aeiou':
            return 0
        if self.b[i] == 'y':
            if i == self.k0:
                return 1
            else:
                return not self.cons(i - 1)
        return 1
    def m(self):
        n = 0
        i = self.k0
        while True:
            if i > self.j:
                return n
            if not self.cons(i):
                break
            i += 1
        i += 1
        while True:
            while True:
                if i > self.j:
                    return n
                if self.cons(i):
                    break
                i += 1
            i += 1
            n += 1
            while True:
                if i > self.j:
                    return n
                if not self.cons(i):
                    break
                i += 1
            i += 1
    def vowelinstem(self):
        for i in range(self.k0, self.j + 1):
            if not self.cons(i):
                return 1
        return 0
    def doublec(self, j):
        if j < (self.k0 + 1):
            return 0
        if self.b[j] != self.b[j-1]:
            return 0
        return self.cons(j)
    def cvc(self, i):
        if i < (self.k0 + 2) or not self.cons(i) or self.cons(i-1) or not self.cons(i-2):
            return 0
        ch = self.b[i]
        if ch in 'wx':
            return 0
        return 1
    def ends(self, s):
        length = len(s)
        if s[length - 1] != self.b[self.k]:
            return 0
        if length > (self.k - self.k0 + 1):
            return 0
        if self.b[self.k-length+1:self.k+1] != s:
            return 0
        self.j = self.k - length
        return 1
    def setto(self, s):
        length = len(s)
        self.b = self.b[:self.j+1] + s + self.b[self.j+length+1:]
        self.k = self.j + length
    def r(self, s):
        if self.m() > 0:
            self.setto(s)
    def step1ab(self):
        if self.b[self.k] == 's':
            if self.ends("sses"):
                self.k = self.k - 2
            elif self.ends("ies"):
                self.setto("i")
            elif self.b[self.k - 1] != 's':
                self.k = self.k - 1
        if self.ends("eed"):
            if self.m() > 0:
                self.k = self.k - 1
        elif (self.ends("ed") or self.ends("ing")) and self.vowelinstem():
            self.k = self.j
            if self.ends("at"):   self.setto("ate")
            elif self.ends("bl"): self.setto("ble")
            elif self.ends("iz"): self.setto("ize")
            elif self.doublec(self.k):
                self.k = self.k - 1
                ch = self.b[self.k]
                if ch in 'lsz':
                    self.k = self.k + 1
            elif (self.m() == 1 and self.cvc(self.k)):
                self.setto("e")
    def step1c(self):
        if (self.ends("y") and self.vowelinstem()):
            self.b = self.b[:self.k] + 'i' + self.b[self.k+1:]
    def step2(self):
        if self.b[self.k - 1] == 'a':
            if self.ends("ational"):   self.r("ate")
            elif self.ends("tional"):  self.r("tion")
        elif self.b[self.k - 1] == 'c':
            if self.ends("enci"):      self.r("ence")
            elif self.ends("anci"):    self.r("ance")
    def stem(self, word):
        self.b = word
        self.k = len(word) - 1
        self.k0 = 0
        if self.k > self.k0 + 1:
            self.step1ab()
            self.step1c()
        return self.b[self.k0:self.k+1]
if __name__ == "__main__":
    stemmer = PorterStemmer()
    words = ["caresses", "ponies", "ties", "caress", "cats", "feed", "agreed", "disabled",
             "matting", "mating", "meeting", "milling", "messing", "meetings"]
    for word in words:
        print(f"{word} -> {stemmer.stem(word)}")