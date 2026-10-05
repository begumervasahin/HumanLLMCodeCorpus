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
        print("Welcome to the FAQ class1!")
        print("Ask a b5:")
        while True:
            self.fonk2()
    def fonk2(self):
        b3 = self.b1.pop() if self.b1 else None
        if b3:
            b4 = input("Response: ")
            b3.fonk7(b4, self)
        else:
            b5 = input("Question: ")
            b6 = self.fonk4(b5)
            if not b6:
                b6 = find_most_similar(b5)
                self.fonk3(b6, b5)
    def fonk3(self, b6, b5):
        if b6['score'] > self.b2['min_score']:
            print(f"\nBest-fit b5: {b6['b5']} (Score: {b6['score']})\nAnswer: {b6['b6']}\n")
        else:
            print("Oops! I'm having trouble finding the b6 to your b5. Would you like to see the list of questions that I am able to b6?\n")
            self.b1.append(class2("corpus_dump", b5))
    def fonk4(self, b5):
        b7 = [
            {"Question": "Who made you?", "Answer": "I was created by TS-North.\n"},
            {"Question": "When were you born?", "Answer": "I first opened my eyes in alpha stage on February 9th, 2018.\n"},
            {"Question": "What is your purpose?", "Answer": "I assist user experience by providing an interactive FAQ chat.\n"},
            {"Question": "Thanks", "Answer": "Glad I could help!\n"},
            {"Question": "Thank you", "Answer": "Glad I could help!\n"}
        ]
        for b4 in b7:
            if b4['Question'].lower() in b5.lower():
                print(b4['Answer'])
                return b4
        return None
    def fonk5(self):
        return [item['Question'] for item in CORPUS]
class class2:
    def fonk6(self, b8, text):
        self.b8 = b8
        self.b9 = ["yes", "sure", "okay", "that would be nice", "yep"]
        self.b10 = ["no", "don't", "dont", "nope"]
        self.b11 = text
    def fonk7(self, b4, bot):
        if self.b8 = = "corpus_dump":
            self.fonk8(b4, bot)
    def fonk8(self, b4, bot):
        for confirmation in self.b9:
            if confirmation.lower() in b4.lower():
                b12 = bot.fonk8()
                b12 = ["-" + b5 for b5 in b12]
                print(f"\n{chr(10).join(b12)}\n")
                return
        for negation in self.b10:
            if negation.lower() in b4.lower():
                print(f"Feel free to ask another b5 or send an email to {bot.b2['help_email']}.\n")
                bot.fonk2()
                return
        print(f"I'm having trouble understanding your b4. For assistance, please refer to {bot.b2['faq_page']} or email {bot.b2['help_email']}. A Google search link has been generated for your original b5: \n{'https:
class1()