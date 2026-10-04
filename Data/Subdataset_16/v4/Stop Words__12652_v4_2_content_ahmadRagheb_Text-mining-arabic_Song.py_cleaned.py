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
        b2 = [word_tokenize(sentence) for sentence in self.b1]
        return u", ".join(b2[0])
    def fonk3(self):
        b2 = [word_tokenize(sentence) for sentence in self.b1]
        return b2[0]
    def fonk4(self):
        b3 = self.b1[0]
        b4 = get_stop_words('ar')
        b5 = word_tokenize(b3)
        b6 = [token for token in b5 if token not in b4]
        return ' '.join(b6)
    def fonk5(self):
        b7 = ISRIStemmer()
        b5 = self.fonk3()
        b8 = [b7.stem(token) for token in b5]
        return ' '.join(b8)
    def fonk6(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        b9 = '/path/to/stanford-postagger.b9'
        b10 = '/path/to/arabic.b11'
        b11 = StanfordPOSTagger(b10, b9)
        b11.b12 = '-mx4096m'
        b13 = b11.tag(word_tokenize(self.b1[0]))
        return ' / '.join([f"{word} {tag}" for word, tag in b13])
with open("testfile.txt", "w", b14 = 'utf-8') as file:
    file.write("ÙÙØ³ Ø§ÙØ¹ÙØ¨ ÙÙ Ø£Ù ÙØ³ÙØ· Ù ÙÙÙ Ø§ÙØ¹ÙØ¨ Ø£Ù ÙØ§ ØªØ³ØªØ·ÙØ¹ Ø§ÙÙÙÙØ¶ ")
    file.write("Ù
Ù Ø§Ø­Ø¨ Ø§ÙÙÙ Ø Ø±Ø£Ù ÙÙ Ø´Ù Ø¬Ù
ÙÙØ§. ")
    file.write("Ø§ÙÙØ§Ø´ÙÙÙ ÙÙÙÙÙÙ: Ø§Ù Ø§ÙÙØ¬Ø§Ø­ ÙÙ Ù
Ø¬Ø±Ø¯ Ø­Ø¸ ")
    file.write("ÙØ§ ØªØ¨ØµÙ ÙÙ Ø§ÙØ¨Ø¦Ø± Ø ÙÙØ¯ ØªØ´Ø±Ø¨ Ù
ÙÙ ÙÙÙ
Ø§. ")
    file.write("ÙØ³Ø±ÙØ§ Ø¥Ø¹ÙØ§Ù
ÙÙ
 Ø¨Ø¥ÙØ¶Ù
Ø§Ù
 ÙØ±ÙØ¹ÙØ§ Ø§ÙØªØ§ÙÙØ© ÙØ®Ø¯Ù
Ø© Ø¹Ù
ÙØ§Ø¦ÙØ§ Ø§ÙÙØ±Ø§Ù
 ")
    file.write("Ø±Ø³Ù
ÙØ§Ù : Ø±ÙØ§Ù Ù
Ø¯Ø±ÙØ¯ Ø³ÙÙØ§Ø¬Ù Ø¨Ø§ÙØ±Ù Ù
ÙÙÙØ® ÙÙ Ø¯ÙØ± Ø§ÙØ±Ø¨Ø¹ Ø§ÙÙÙØ§Ø¦Ù ÙØ¯ÙØ±Ù Ø£Ø¨Ø·Ø§Ù Ø£ÙØ±ÙØ¨Ø§ ")
with open("testfile.txt", "r", b14 = 'utf-8') as file:
    b15 = file.read()
b16 = class1([b15])
print('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n\n')
print('\n------- tokenizer ------------\n')
print(b16.fonk3())
print('\n------- read ------------\n')
print(b16.fonk2())
print('\n------- stop words ------------\n')
print(b16.fonk4())
print('\n------- stemming ------------\n')
print(b16.fonk5())
print('\n------- part of speech ------------\n')
print(b16.fonk6())
print('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n\n')
print('\n------- tokenizer ------------\n')
print(b16.fonk3())
print('\n--------- read ------------\n')
print(b16.fonk2())
print('\n--------- stop words ------------\n')
b17 = [b16.fonk4()]
b18 = class1(b17)
print(b18.fonk4())
print('\n--------- stemming ------------\n')
b19 = [b18.fonk5()]
b20 = class1(b19)
print(b20.fonk5())
print('\n-------- part of speech ------------\n')
print(b16.fonk6())