import json
import math
import os
import re
import sys
from collections import defaultdict, Counter
class PorterStemmer:
    def __init__(self):
        self.b = ""
        self.k = 0
        self.k0 = 0
        self.j = 0
    def cons(self, i):
        if self.b[i] in 'aeiou':
            return False
        if self.b[i] == 'y':
            if i == self.k0:
                return True
            else:
                return not self.cons(i - 1)
        return True
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
                return True
        return False
    def doublec(self, j):
        if j < (self.k0 + 1):
            return False
        if self.b[j] != self.b[j - 1]:
            return False
        return self.cons(j)
    def cvc(self, i):
        if i < (self.k0 + 2) or not self.cons(i) or self.cons(i - 1) or not self.cons(i - 2):
            return False
        ch = self.b[i]
        if ch in 'wx':
            return False
        return True
    def ends(self, s):
        length = len(s)
        if s[length - 1] != self.b[self.k]:
            return False
        if length > (self.k - self.k0 + 1):
            return False
        if self.b[self.k - length + 1:self.k + 1] != s:
            return False
        self.j = self.k - length
        return True
    def setto(self, s):
        length = len(s)
        self.b = self.b[:self.j + 1] + s + self.b[self.j + length + 1:]
        self.k = self.j + length
    def r(self, s):
        if self.m() > 0:
            self.setto(s)
    def step1ab(self):
        if self.b[self.k] == 's':
            if self.ends("sses"):
                self.k -= 2
            elif self.ends("ies"):
                self.setto("i")
            elif self.b[self.k - 1] != 's':
                self.k -= 1
        if self.ends("eed"):
            if self.m() > 0:
                self.k -= 1
        elif (self.ends("ed") or self.ends("ing")) and self.vowelinstem():
            self.k = self.j
            if self.ends("at"):
                self.setto("ate")
            elif self.ends("bl"):
                self.setto("ble")
            elif self.ends("iz"):
                self.setto("ize")
            elif self.doublec(self.k):
                self.k -= 1
                ch = self.b[self.k]
                if ch in 'lsz':
                    self.k += 1
            elif (self.m() == 1 and self.cvc(self.k)):
                self.setto("e")
    def step1c(self):
        if self.ends("y") and self.vowelinstem():
            self.b = self.b[:self.k] + 'i' + self.b[self.k + 1:]
    def step2(self):
        if self.b[self.k - 1] == 'a':
            if self.ends("ational"):
                self.r("ate")
            elif self.ends("tional"):
                self.r("tion")
        elif self.b[self.k - 1] == 'c':
            if self.ends("enci"):
                self.r("ence")
            elif self.ends("anci"):
                self.r("ance")
    def step3(self):
        if self.b[self.k] == 'e':
            if self.ends("icate"):
                self.r("ic")
            elif self.ends("ative"):
                self.r("")
            elif self.ends("alize"):
                self.r("al")
    def step4(self):
        if self.b[self.k - 1] == 'a':
            if self.ends("al"):
                pass
        elif self.b[self.k - 1] == 'c':
            if self.ends("ance") or self.ends("ence"):
                pass
    def step5(self):
        self.j = self.k
        if self.b[self.k] == 'e':
            a = self.m()
            if a > 1 or (a == 1 and not self.cvc(self.k - 1)):
                self.k -= 1
        if self.b[self.k] == 'l' and self.doublec(self.k) and self.m() > 1:
            self.k -= 1
    def stem(self, p, i, j):
        self.b = p
        self.k = j
        self.k0 = i
        if self.k <= self.k0 + 1:
            return self.b
        self.step1ab()
        self.step1c()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        return self.b[self.k0:self.k + 1]
class IRSystem:
    def __init__(self):
        self.titles = []
        self.docs = []
        self.vocab = []
        self.alphanum = re.compile('[^a-zA-Z0-9]')
        self.p = PorterStemmer()
    def get_unique_words(self):
        unique = set()
        for doc in self.docs:
            for word in doc:
                unique.add(word)
        return unique
    def read_raw_data(self, dirname):
        print("Stemming Documents...")
        titles = []
        docs = []
        os.mkdir('%s/stemmed' % dirname)
        title_pattern = re.compile('(.*) \d+\.txt')
        filenames = [filename for filename in os.listdir('%s/raw' % dirname) if filename.endswith(".txt") and not filename.startswith(".")]
        for i, filename in enumerate(filenames):
            title = title_pattern.search(filename).group(1)
            print(f"    Doc {i+1} of {len(filenames)}: {title}")
            titles.append(title)
            contents = []
            with open('%s/raw/%s' % (dirname, filename), 'r') as f:
                with open('%s/stemmed/%s.txt' % (dirname, title), 'w') as of:
                    for line in f:
                        line = line.lower().split()