import math
import random
import re
import glob
from collections import Counter, defaultdict
from machine_learning import split_data
def fonk1(b1):
    b1 = b1.lower()
    return set(re.findall(r"[a-z0-9']+", b1))
def fonk2(training_set):
    b2 = defaultdict(lambda: [0, 0])
    for b1, b14 in training_set:
        for word in fonk1(b1):
            b2[word][0 if b14 else 1] += 1
    return b2
def fonk3(b2, total_spams, total_non_spams, b3 = 0.5):
    return [(w,
             (spam + b3) / (total_spams + 2 * b3),
             (non_spam + b3) / (total_non_spams + 2 * b3))
            for w, (spam, non_spam) in b2.items()]
def fonk4(b8, b1):
    b4 = fonk1(b1)
    b5 = log_prob_if_not_spam = 0.0
    for word, b6, b7 in b8:
        if word in b4:
            b5 += math.log(b6)
            log_prob_if_not_spam += math.log(b7)
        else:
            b5 += math.log(1.0 - b6)
            log_prob_if_not_spam += math.log(1.0 - b7)
    b6 = math.exp(b5)
    b7 = math.exp(log_prob_if_not_spam)
    return b6 / (b6 + b7)
class class1:
    def fonk5(self, b3 = 0.5):
        self.b3 = b3
        self.b8 = []
    def fonk6(self, training_set):
        b9 = sum(b14 for b1, b14 in training_set)
        b10 = len(training_set) - b9
        b11 = fonk2(training_set)
        self.b8 = fonk3(b11, b9, b10, self.b3)
    def fonk7(self, b1):
        return fonk4(self.b8, b1)
def fonk8(path):
    b12 = []
    b13 = re.compile(r"^Subject:\s+")
    for fn in glob.glob(path):
        b14 = "ham" not in fn
        with open(fn, 'r', b15 = 'ISO-8859-1') as file:
            for line in file:
                if line.startswith("Subject:"):
                    b16 = b13.sub("", line).strip()
                    b12.append((b16, b14))
    return b12
def fonk9(word_prob):
    word, b6, b7 = word_prob
    return b6 / (b6 + b7)
def fonk10(path):
    b12 = fonk8(path)
    random.seed(0)
    train_data, b17 = split_data(b12, 0.75)
    b18 = class1()
    b18.fonk6(train_data)
    b19 = [(b16, b14, b18.fonk7(b16)) for b16, b14 in b17]
    b2 = Counter((b14, spam_probability > 0.5) for _, b14, spam_probability in b19)
    print(b2)
    b19.sort(b20 = lambda row: row[2])
    b21 = list(filter(lambda row: not row[1], b19))[-5:]
    b22 = list(filter(lambda row: row[1], b19))[:5]
    print("b21", b21)
    print("b22", b22)
    b23 = sorted(b18.b8, b20=p_spam_given_word)
    b24 = b23[-5:]
    b25 = b23[:5]
    print("b24", b24)
    print("b25", b25)
if b26 = = "__main__":
    fonk10(r"./emails/*/*")