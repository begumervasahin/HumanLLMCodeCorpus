from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = "news_test.txt"
class class1:
    def fonk1(self):
        self.b3 = []
        self.b4 = []
        self.b5 = []
        self.b6 = {}
        self.b7 = []
    def fonk2(self, file_name):
        with open(file_name, b8 = 'utf-8') as f:
            b9 = f.readlines()
            for article in b9:
                category, b10 = article.split("\t", 1)
                self.b3.append(category)
                self.b4.append(b10.strip())
    def fonk3(self):
        self.b5 = list(set(self.b3))
    def fonk4(self, category_name):
        return [i for i, b11 in enumerate(self.b3) if b11 = = category_name][:a1]
    def fonk5(self, category, b15):
        b12 = Counter(b15)
        b12.update({word: 0 for word in b12.keys()})
        for i in self.fonk4(category):
            b13 = Counter(self.b4[i].split())
            for key in b13:
                if key in b12:
                    b12[key] += b13[key]
        return b12
    def fonk6(self, category):
        return len(self.fonk4(category)) / len(self.b3)
    def fonk7(self, category):
        b6 = 0
        b7 = set()
        for i in self.fonk4(category):
            b13 = Counter(self.b4[i].split())
            b6 += len(b13)
            b7.update(b13.keys())
        return b6, list(b7)
    def fonk8(self):
        self.fonk2(b1)
        self.fonk3()
        for category_name in self.b5:
            b6, b7 = self.fonk7(category_name)
            self.b6[category_name] = b6
            self.b7.extend(b7)
        self.b7 = list(set(self.b7))
    def fonk9(self, test_data):
        b14 = []
        for test_article in test_data:
            b15 = Counter(test_article.split())
            b16 = []
            for category_name in self.b5:
                b12 = self.fonk5(category_name, b15)
                b17 = [10000 * (b12[word] + 1) / (self.b6[category_name] + len(self.b7))
                                     for word in b12]
                b18 = self.fonk6(category_name) * np.prod(b17)
                b16.append(b18)
            b19 = self.b5[np.argmax(b16)]
            b14.append(b19)
        return b14
if b20 = = "__main__":
    b21 = class1()
    b21.fonk8()
    b22 = []
    with open(b2, b8 = 'utf-8') as f:
        b23 = f.readlines()
        b22.extend(article.strip() for article in b23)
    b14 = b21.fonk9(b22)
    with open('answer.txt', 'w', b8 = "utf8") as answerfile:
        for prediction in b14:
            answerfile.write(prediction + '\n')