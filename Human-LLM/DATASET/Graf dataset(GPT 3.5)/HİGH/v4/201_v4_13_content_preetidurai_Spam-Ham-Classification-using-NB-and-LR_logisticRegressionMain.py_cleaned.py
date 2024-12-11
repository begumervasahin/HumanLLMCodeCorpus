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
            for word in mail_file_value.b12:
                self.b3.add(word)
    def fonk3(self):
        for word in self.b3:
            self.b6[word] = 0.0
    def fonk4(self, iteration_threshold):
        for _ in range(int(iteration_threshold)):
            for weight_word in self.b6:
                a1 = 0.0
                for mail in self.b1.values():
                    b7 = 1 if mail.true_class == 1 else 0
                    if weight_word in mail.b12:
                        a1 += mail.b13[weight_word] * (b7 - self.fonk5(1, mail))
                self.b6[weight_word] += (self.b4 * a1) - (self.b4 * self.b5 * self.b6[weight_word])
    def fonk5(self, b8, mail):
        a2 = 0.0
        for key, value in mail.b13.items():
            if key not in self.b6:
                self.b6[key] = 0.0
            a2 += self.b6[key] * value
        if b8 = = 1:
            return math.exp(a2) / (1 + math.exp(a2))
        elif b8 = = 0:
            return 1 / (1 + math.exp(a2))
    def fonk6(self, mail):
        b9 = {}
        b9[0] = self.fonk5(0, mail)
        b9[1] = self.fonk5(1, mail)
        return 0 if b9[0] > b9[1] else 1
    def fonk7(self, directory_path, given_class):
        for file in os.listdir(directory_path):
            b10 = os.path.join(directory_path, file)
            with open(b10, b11 = 'utf-8', errors="ignore") as mail_file:
                b12 = helper.get_words(mail_file.read())
                b13 = helper.get_word_freq(b12)
                self.b2[file] = m.Mail(b12, b13, given_class)
    def fonk8(self):
        a3 = 0
        for mail_value in self.b2.values():
            b14 = self.fonk6(mail_value)
            if b14 = = mail_value.true_class:
                a3 += 1
        b15 = (a3 / len(self.b2)) * 100
        print("Accuracy:", b15)
    def fonk9(self, directory_path, given_class):
        for file in os.listdir(directory_path):
            b10 = os.path.join(directory_path, file)
            with open(b10, b11 = 'utf-8', errors="ignore") as mail_file:
                b12 = helper.get_words(mail_file.read())
                b13 = helper.get_word_freq(b12)
                self.b1[file] = m.Mail(b12, b13, given_class)
def fonk10():
    if len(sys.argv) < 9:
        print("Insufficient arguments.")
        return
    b16 = class1(sys.argv[5], sys.argv[6])
    b17 = sys.argv[1]
    b18 = sys.argv[2]
    b19 = sys.argv[3]
    b20 = sys.argv[4]
    b16.fonk9(b17, 0)
    b16.fonk9(b18, 1)
    b16.fonk7(b19, 0)
    b16.fonk7(b20, 1)
    b16.fonk2()
    b16.fonk3()
    b16.fonk4(sys.argv[7])
    print("Accuracy without removing stopwords:")
    b16.fonk8()
    b21 = class1(sys.argv[5], sys.argv[6])
    b21.build_training_info_wo_stopwords(b17, 0, sys.argv[8])
    b21.build_training_info_wo_stopwords(b18, 1, sys.argv[8])
    b21.build_test_info_wo_stopwords(b19, 0, sys.argv[8])
    b21.build_test_info_wo_stopwords(b20, 1, sys.argv[8])
    b21.fonk2()
    b21.fonk3()
    b21.fonk4(sys.argv[7])
    print("Accuracy after removing stopwords:")
    b21.fonk8()
if b22 = = "__main__":
    fonk10()