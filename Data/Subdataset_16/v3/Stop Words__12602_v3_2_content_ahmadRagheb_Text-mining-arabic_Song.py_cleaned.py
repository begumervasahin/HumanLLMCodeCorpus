import nltk
from nltk.tokenize import word_tokenize
from b5 import get_stop_words
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
        b4 = word_tokenize(self.b1[0])
        b5 = get_stop_words('ar')
        b6 = [token for token in b4 if token not in b5]
        return ' '.join(b6)
    def fonk5(self):
        b7 = ISRIStemmer()
        b4 = self.fonk3()
        b8 = [b7.fonk5(token) for token in b4]
        return ' '.join(b8)
    def fonk6(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        b9 = '/path/to/stanford-postagger.b9'
        b10 = '/path/to/arabic.b11'
        b11 = StanfordPOSTagger(b10, b9)
        b11.b12 = '-mx4096m'
        b13 = b11.tag(word_tokenize(self.b1[0]))
        return ' / '.join([f"{word} {tag}" for word, tag in b13])
def fonk7(b15):
    with open(b15, "w", b14 = "utf-8") as file:
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
def fonk8(b15):
    with open(b15, "r", b14 = "utf-8") as file:
        return file.read()
b15 = "testfile.txt"
fonk7(b15)
b16 = fonk8(b15)
b17 = class1([b16])
print('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n')
print('\n------- Tokenizer ------------\n')
print(b17.fonk3())
print('\n------- Read from List ------------\n')
print(b17.fonk2())
print('\n------- Stop Words Removal ------------\n')
print(b17.fonk4())
print('\n------- Stemming ------------\n')
print(b17.fonk5())
print('\n------- Part of Speech ------------\n')
print(b17.fonk6())
print('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n')
print('\n------- Tokenizer ------------\n')
print(b17.fonk3())
print('\n--------- Read from List ------------\n')
print(b17.fonk2())
print('\n--------- Stop Words Removal ------------\n')
b18 = [b17.fonk4()]
b19 = class1(b18)
print(b19.fonk4())
print('\n--------- Stemming ------------\n')
b20 = [b19.fonk5()]
b21 = class1(b20)
print(b21.fonk5())
print('\n-------- Part of Speech ------------\n')
print(b17.fonk6())