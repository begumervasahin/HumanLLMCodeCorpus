from collections import Counter, defaultdict
from machine_learning import split_data
import math, random, re, glob
def fonk1(b1):
    b1 = b1.lower()
    b2 = re.findall("[a-z0-9']+", b1)
    return set(b2)
def fonk2(training_set):
    b3 = defaultdict(lambda: [0, 0])
    for b1, b15 in training_set:
        for word in fonk1(b1):
            b3[word][0 if b15 else 1] += 1
    return b3
def fonk3(b3, total_spams, total_non_spams, b4 = 0.5):
    return [(w,
             (spam + b4) / (total_spams + 2 * b4),
             (non_spam + b4) / (total_non_spams + 2 * b4))
             for w, (spam, non_spam) in b3.items()]
def fonk4(b9, b1):
    b5 = fonk1(b1)
    b6 = log_prob_if_not_spam = 0.0
    for word, b7, b8 in b9:
        if word in b5:
            b6 += math.log(b7)
            log_prob_if_not_spam += math.log(b8)
        else:
            b6 += math.log(1.0 - b7)
            log_prob_if_not_spam += math.log(1.0 - b8)
    b7 = math.exp(b6)
    b8 = math.exp(log_prob_if_not_spam)
    return b7 / (b7 + b8)
class class1:
    def fonk5(self, b4 = 0.5):
        self.b4 = b4
        self.b9 = []
    def fonk6(self, training_set):
        b10 = len([b15
                         for b1, b15 in training_set
                         if b15])
        b11 = len(training_set) - b10
        b12 = fonk2(training_set)
        self.b9 = fonk3(b12,
                                             b10,
                                             b11,
                                             self.b4)
    def fonk7(self, b1):
        return fonk4(self.b9, b1)
def fonk8(path):
    b13 = []
    b14 = re.compile(r"^Subject:\s+")
    for fn in glob.glob(path):
        b15 = "ham" not in fn
        with open(fn,'r',b16 = 'ISO-8859-1') as file:
            for line in file:
                if line.startswith("Subject:"):
                    b17 = b14.sub("", line).strip()
                    b13.append((b17, b15))
    return b13
def fonk9(word_prob):
    word, b7, b8 = word_prob
    return b7 / (b7 + b8)
def fonk10(path):
    b13 = fonk8(path)
    random.seed(0)
    train_data, b18 = split_data(b13, 0.75)
    b19 = class1()
    b19.fonk6(train_data)
    b20 = [(b17, b15, b19.fonk7(b17))
              for b17, b15 in b18]
    b3 = Counter((b15, spam_probability > 0.5)
                     for _, b15, spam_probability in b20)
    print(b3)
    b20.sort(b21 = lambda row: row[2])
    b22 = list(filter(lambda row: not row[1], b20))[-5:]
    b23 = list(filter(lambda row: row[1], b20))[:5]
    print("b22", b22)
    print("b23", b23)
    b24 = sorted(b19.b9, b21=p_spam_given_word)
    b25 = b24[-5:]
    b26 = b24[:5]
    print("b25", b25)
    print("b26", b26)
if b27 = = "__main__":
    fonk10(r"./emails/*/*")