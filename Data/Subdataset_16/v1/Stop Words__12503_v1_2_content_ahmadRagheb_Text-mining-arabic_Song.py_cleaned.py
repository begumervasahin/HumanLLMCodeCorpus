import nltk
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words
from nltk.stem.isri import ISRIStemmer
from nltk.tag import StanfordPOSTagger
import os
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        b2 = [word_tokenize(sent) for sent in self.b1]
        b3 = "\n".join([", ".join(sent) for sent in b2])
        return b3
    def fonk3(self):
        return word_tokenize(self.b1[0])
    def fonk4(self):
        b4 = self.b1[0]
        b5 = get_stop_words('ar')
        b6 = word_tokenize(b4)
        b7 = [token for token in b6 if token not in b5]
        return ' '.join(b7)
    def fonk5(self):
        b8 = ISRIStemmer()
        b6 = self.fonk3()
        b9 = [b8.stem(token) for token in b6]
        return ' '.join(b9)
    def fonk6(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        b10 = '/path/to/stanford-postagger.b10'
        b11 = '/path/to/arabic.b12'
        b12 = StanfordPOSTagger(b11, b10)
        b12.b13 = '-mx4096m'
        b14 = b12.tag(word_tokenize(self.b1[0]))
        return ' / '.join([f"{word} {tag}" for word, tag in b14])
with open("testfile.txt", "w", b15 = "utf-8") as file:
    file.write("ÙÙØ³ Ø§ÙØ¹ÙØ¨ ÙÙ Ø£Ù ÙØ³ÙØ· ÙÙÙÙ Ø§ÙØ¹ÙØ¨ Ø£Ù ÙØ§ ØªØ³ØªØ·ÙØ¹ Ø§ÙÙÙÙØ¶.\n")
    file.write("Ù
Ù Ø£Ø­Ø¨ Ø§ÙÙÙØ Ø±Ø£Ù ÙÙ Ø´ÙØ¡ Ø¬Ù
ÙÙØ§.\n")
    file.write("Ø§ÙÙØ§Ø´ÙÙÙ ÙÙÙÙÙÙ: Ø¥Ù Ø§ÙÙØ¬Ø§Ø­ ÙÙ Ù
Ø¬Ø±Ø¯ Ø­Ø¸.\n")
    file.write("ÙØ§ ØªØ¨ØµÙ ÙÙ Ø§ÙØ¨Ø¦Ø±Ø ÙÙØ¯ ØªØ´Ø±Ø¨ Ù
ÙÙ ÙÙÙ
Ø§.\n")
    file.write("ÙØ³Ø±ÙØ§ Ø¥Ø¹ÙØ§Ù
ÙÙ
 Ø¨Ø¥ÙØ¶Ù
Ø§Ù
 ÙØ±ÙØ¹ÙØ§ Ø§ÙØªØ§ÙÙØ© ÙØ®Ø¯Ù
Ø© Ø¹Ù
ÙØ§Ø¦ÙØ§ Ø§ÙÙØ±Ø§Ù
.\n")
    file.write("Ø±Ø³Ù
ÙØ§Ù: Ø±ÙØ§Ù Ù
Ø¯Ø±ÙØ¯ Ø³ÙÙØ§Ø¬Ù Ø¨Ø§ÙØ±Ù Ù
ÙÙÙØ® ÙÙ Ø¯ÙØ± Ø§ÙØ±Ø¨Ø¹ Ø§ÙÙÙØ§Ø¦Ù ÙØ¯ÙØ±Ù Ø£Ø¨Ø·Ø§Ù Ø£ÙØ±ÙØ¨Ø§.\n")
with open("testfile.txt", "r", b15 = "utf-8") as file:
    b16 = file.read()
b17 = class1([b16])
print('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n')
print('\n------- tokenizer ------------\n')
print(b17.fonk3())
print('\n------- read ------------\n')
print(b17.fonk2())
print('\n------- stop words ------------\n')
print(b17.fonk4())
print('\n------- b20 ------------\n')
print(b17.fonk5())
print('\n------- part of speech ------------\n')
print(b17.fonk6())
print('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n')
print('\n------- tokenizer ------------\n')
print(b17.fonk3())
print('\n--------- read ------------\n')
print(b17.fonk2())
print('\n--------- stop words ------------\n')
b18 = [b17.fonk4()]
b19 = class1(b18)
print(b19.fonk4())
print('\n--------- b20 ------------\n')
b20 = [b19.fonk5()]
b21 = class1(b20)
print(b21.fonk5())
print('\n-------- part of speech ------------\n')
print(b17.fonk6())