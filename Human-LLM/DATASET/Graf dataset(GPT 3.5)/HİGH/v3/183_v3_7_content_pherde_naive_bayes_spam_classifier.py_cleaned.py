import re
import glob
import math
import random
from collections import Counter, defaultdict
from machine_learning import split_data
class class1:
    def fonk1(self, b1 = 0.5):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, training_set):
        b3 = sum(1 for b7, b15 in training_set if b15)
        b4 = len(training_set) - b3
        b5 = self.fonk4(training_set)
        self.b2 = self.fonk6(b5, b3, b4, self.b1)
    def fonk3(self, b7):
        return self.fonk7(self.b2, b7)
    def fonk4(self, training_set):
        b6 = defaultdict(lambda: [0, 0])
        for b7, b15 in training_set:
            for word in self.fonk5(b7):
                b6[word][0 if b15 else 1] += 1
        return b6
    def fonk5(self, b7):
        b7 = b7.lower()
        b8 = re.findall(r"[a-z0-9']+", b7)
        return set(b8)
    def fonk6(self, b6, total_spams, total_non_spams, b1 = 0.5):
        return [(word,
                 (spam_count + b1) / (total_spams + 2 * b1),
                 (non_spam_count + b1) / (total_non_spams + 2 * b1))
                 for word, (spam_count, non_spam_count) in b6.items()]
    def fonk7(self, b2, b7):
        b9 = self.fonk5(b7)
        b10 = log_prob_if_not_spam = 0.0
        for word, b11, b12 in b2:
            if word in b9:
                b10 += math.log(b11)
                log_prob_if_not_spam += math.log(b12)
            else:
                b10 += math.log(1.0 - b11)
                log_prob_if_not_spam += math.log(1.0 - b12)
        b11 = math.exp(b10)
        b12 = math.exp(log_prob_if_not_spam)
        return b11 / (b11 + b12)
def fonk8(path):
    b13 = []
    b14 = re.compile(r"^Subject:\s+")
    for file_path in glob.glob(path):
        b15 = "ham" not in file_path
        with open(file_path, 'r', b16 = 'ISO-8859-1') as file:
            for line in file:
                if line.startswith("Subject:"):
                    b17 = b14.sub("", line).strip()
                    b13.append((b17, b15))
    return b13
def fonk9(word_prob):
    word, b11, b12 = word_prob
    return b11 / (b11 + b12)
def fonk10(path):
    b13 = fonk8(path)
    random.seed(0)
    train_data, b18 = split_data(b13, 0.75)
    b19 = class1()
    b19.fonk2(train_data)
    b20 = [(b17, b15, b19.fonk3(b17)) for b17, b15 in b18]
    b6 = Counter((b15, spam_probability > 0.5) for _, b15, spam_probability in b20)
    print(b6)
    b20.sort(b21 = lambda row: row[2])
    b22 = list(filter(lambda row: not row[1], b20))[-5:]
    b23 = list(filter(lambda row: row[1], b20))[:5]
    print("b22", b22)
    print("b23", b23)
    b24 = sorted(b19.b2, b21=p_spam_given_word)
    b25 = b24[-5:]
    b26 = b24[:5]
    print("b25", b25)
    print("b26", b26)
if b27 = = "__main__":
    fonk10(r"./emails/*/*")