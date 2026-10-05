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
        self.b6 = []
        self.b7 = []
        self.b8 = {}
        self.a3 = 0
    def fonk2(self):
        with open(b1, b9 = 'utf-8') as file:
            b10 = file.readlines()
            for article in b10:
                category, b11 = article.split("\t", 1)
                self.b3.append(category)
                self.b4.append(b11.strip())
    def fonk3(self, category_name):
        return [i for i, b12 in enumerate(self.b3) if b12 = = category_name]
    def fonk4(self, category):
        a4 = 0
        b6 = []
        for i in self.fonk3(category):
            b13 = dict(Counter(self.b4[i].split()))
            a4 += len(b13.keys())
            b6.extend(b13.keys())
        return a4, list(set(b6))
    def fonk5(self):
        for category_name in self.b5:
            a4, b14 = self.fonk4(category_name)
            self.b6.extend(b14)
            self.b7.append(a4)
    def fonk6(self, category):
        return len(self.fonk3(category)) / len(self.b3)
    def fonk7(self, category, b22):
        b15 = Counter(b22)
        b15.update({word: 0 for word in self.b6})
        for i in self.fonk3(category):
            b13 = dict(Counter(self.b4[i].split()))
            for word in b13:
                if word in b15:
                    b15[word] += b13[word]
        return b15
    def fonk8(self, b15, category):
        b16 = {}
        for word, count in b15.items():
            b16[word] = 10000 * (count + 1) / (self.b8[category] + self.a3)
        return b16
    def fonk9(self, b22):
        b17 = []
        for category_name in self.b5:
            b15 = self.fonk7(category_name, b22)
            b18 = self.fonk8(b15, category_name)
            a5 = 1
            for word, cond_prob in b18.items():
                a5 *= cond_prob
            a5 *= self.fonk6(category_name)
            b17.append(a5)
        max_probability, b19 = max((prob, idx) for (idx, prob) in enumerate(b17))
        return self.b5[b19]
    def fonk10(self):
        b20 = []
        with open(b2, b9 = 'utf-8') as file:
            b21 = file.readlines()
        with open('answer.txt', 'w', b9 = "utf8") as answer_file:
            for article in b21:
                b22 = Counter(article.split())
                b23 = self.fonk9(b22)
                answer_file.write(b23 + '\n')
    def fonk11(self):
        self.b5 = list(set(self.b3))
        self.fonk5()
        self.b8 = dict(zip(self.b5, self.b7))
        self.a3 = len(set(self.b6))
if b24 = = '__main__':
    b25 = class1()
    b25.fonk2()
    b25.fonk11()
    b25.fonk10()