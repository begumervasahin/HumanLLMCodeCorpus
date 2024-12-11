import LRHelper as helper
import Mail as m
import os
import math
import sys
class class1:
    def fonk1(self, b4, b5):
        self.b1 = {}
        self.b2 = {}
        self.b3 = set()
        self.b4 = float(b4)
        self.b5 = float(b5)
        self.b6 = {}
    def fonk2(self):
        for mail_file_key, mail_file_value in self.b1.items():
            self.b3.update(mail_file_value.b16)
    def fonk3(self):
        self.b6 = {word: 0.0 for word in self.b3}
    def fonk4(self, iteration_threshold):
        for _ in range(int(iteration_threshold)):
            for weight_word in self.b6:
                a1 = 0.0
                for mail in self.b1.values():
                    b7 = 1 if mail.true_class == 1 else 0
                    if weight_word in mail.b16:
                        a1 += mail.b17[weight_word] * (b7 - self.fonk5(1, mail))
                self.b6[weight_word] += (self.b4 * a1) - (self.b4 * self.b5 * self.b6[weight_word])
    def fonk5(self, b9, mail):
        b8 = sum(self.b6.get(b11, 0.0) * value for b11, value in mail.b17.items())
        if b9 = = 1:
            return math.exp(b8) / (1 + math.exp(b8))
        elif b9 = = 0:
            return 1 / (1 + math.exp(b8))
    def fonk6(self, mail):
        b10 = {0: self.fonk5(0, mail), 1: self.fonk5(1, mail)}
        return max(b10, b11 = b10.get)
    def fonk7(self, directory_path, given_class, b12 = True):
        b13 = self.b1 if b12 else self.b2
        for file in os.listdir(directory_path):
            b14 = os.path.join(directory_path, file)
            with open(b14, b15 = 'utf-8', errors="ignore") as mail_file:
                b16 = helper.get_words(mail_file.read())
                b17 = helper.get_word_freq(b16)
                b13[file] = m.Mail(b16, b17, given_class)
    def fonk8(self):
        b18 = sum(1 for mail_value in self.b2.values() if self.fonk6(mail_value) == mail_value.true_class)
        b19 = (b18 / len(self.b2)) * 100
        print("Accuracy:", b19)
def fonk9():
    if len(sys.argv) < 9:
        print("Insufficient arguments.")
        return
    b20 = class1(sys.argv[5], sys.argv[6])
    spam_training_path, ham_training_path, spam_test_path, b21 = sys.argv[1:5]
    b20.fonk7(spam_training_path, 0)
    b20.fonk7(ham_training_path, 1)
    b20.fonk7(spam_test_path, 0, False)
    b20.fonk7(b21, 1, False)
    b20.fonk2()
    b20.fonk3()
    b20.fonk4(sys.argv[7])
    print("Accuracy without removing stopwords:")
    b20.fonk8()
    b22 = class1(sys.argv[5], sys.argv[6])
    b22.fonk7(sys.argv[8], 0, True)
    b22.fonk7(sys.argv[8], 1, True)
    b22.fonk7(sys.argv[8], 0, False)
    b22.fonk7(sys.argv[8], 1, False)
    b22.fonk2()
    b22.fonk3()
    b22.fonk4(sys.argv[7])
    print("Accuracy after removing stopwords:")
    b22.fonk8()
if b23 = = "__main__":
    fonk9()