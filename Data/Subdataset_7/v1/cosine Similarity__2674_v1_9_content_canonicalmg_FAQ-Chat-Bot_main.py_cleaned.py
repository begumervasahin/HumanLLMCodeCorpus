from similarity import find_most_similar
from b12 import CORPUS
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = {
            "min_score": 0.2,
            "help_email": "fakeEmail@notArealEmail.com",
            "faq_page": "www.NotActuallyAnFAQ.com"
        }
        print("Ask a question:")
        while True:
            self.fonk2()
    def fonk2(self):
        b3 = None
        if self.b1:
            b3 = self.b1.pop()
        if b3:
            b4 = input("Response: ")
            b3.fonk7(b4, self)
        else:
            b4 = input("Question: ")
            b5 = self.fonk4(b4)
            if not b5:
                b5 = find_most_similar(b4)
                self.fonk3(b5, b4)
    def fonk3(self, b5, b4):
        if b5['score'] > self.b2['min_score']:
            print("\nBest-fit question: %s (Score: %s)\nAnswer: %s\n" % (b5['question'],
                                                                          b5['score'],
                                                                          b5['b5']))
        else:
            print("Woops! I'm having trouble finding the b5 to your question. "
                  "Would you like to see the list of questions that I am able to b5?\n")
            self.b1.append(class2("corpus_dump", b4))
    def fonk4(self, b4):
        b6 = [
            {
                "Question": "Who made you?",
                "Answer": "I was created by TS-North.\n"
            },
            {
                "Question": "When were you born?",
                "Answer": "I first opened my eyes in alpha stage February 9th, 2018.\n"
            },
            {
                "Question": "What is your purpose?",
                "Answer": "I assist user experience by providing an interactive FAQ chat.\n"
            },
            {
                "Question": "Thanks",
                "Answer": "Glad I could help!\n"
            },
            {
                "Question": "Thank you",
                "Answer": "Glad I could help!\n"
            }
        ]
        for each_question in b6:
            if each_question['Question'].lower() in b4.lower():
                print(each_question['Answer'])
                return each_question
    def fonk5(self):
        b7 = []
        for each_item in CORPUS:
            b7.append(each_item['Question'])
        return b7
class class2:
    def fonk6(self, b8, b4):
        self.b8 = b8
        self.b9 = ["yes", "sure", "okay", "that would be nice", "yep"]
        self.b10 = ["no", "don't", "dont", "nope"]
        self.b11 = b4
    def fonk7(self, b4, bot):
        if self.b8 = = "corpus_dump":
            self.fonk8(b4, bot)
    def fonk8(self, b4, bot):
        for each_confirmation in self.b9:
            for each_word in b4.split(" "):
                if each_confirmation.lower() == each_word.lower():
                    b12 = bot.fonk5()
                    b12 = ["-" + s for s in b12]
                    print("%s%s%s" % ("\n", "\n".join(b12), "\n"))
                    return 0
        for each_negation in self.b10:
            for each_word in b4.split(" "):
                if each_negation.lower() == each_word.lower():
                    print("Feel free to ask another question or send an email to %s.\n" % bot.b2['help_email'])
                    bot.fonk2()
                    return 0
        print("I'm having trouble understanding what you are saying. At the time, my ability is quite limited, "
              "please refer to %s or email %s if I was not able to b5 your question. "
              "For convenience, a google link has been generated below: \n%s\n" % (bot.b2['faq_page'],
                                                                                   bot.b2['help_email'],
                                                                                   "https:
                                                                                   ("+".join(self.b11.split(" ")))))
        return 0
class1()