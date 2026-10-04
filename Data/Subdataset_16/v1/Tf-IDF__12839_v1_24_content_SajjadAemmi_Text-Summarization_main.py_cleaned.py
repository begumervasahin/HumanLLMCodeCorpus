import argparse
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = ""
        self.a1 = 0
    def fonk2(self):
        pass
    def fonk3(self):
        pass
    def fonk4(self):
        pass
    def fonk5(self):
        pass
    def fonk6(self):
        pass
    def fonk7(self):
        pass
    def fonk8(self):
        with open(self.b4, 'w') as file:
            file.write(self.b5)
if b6 = = "__main__":
    b7 = argparse.ArgumentParser()
    b7.add_argument("--input", b8 = "io/input/big_text.txt", type=str, help="input big text")
    b7.add_argument("--stop-words", b8 = "io/input/stop_words.txt", type=str, help="input stop words")
    b7.add_argument("--important-words", b8 = "io/input/important_words.txt", type=str, help="input important words")
    b7.add_argument("--output", b8 = "io/output/small_text.txt", type=str, help="output small text")
    b9 = b7.parse_args()
    b10 = class1(b9.input, b9.stop_words, b9.important_words, b9.output)
    b10.fonk2()
    b10.fonk3()
    b10.fonk4()
    b10.fonk5()
    b10.fonk6()
    b10.a1 = int(input("Enter the maximum number of words for the output text: "))
    b10.fonk7()
    print(b10.b5)
    b10.fonk8()