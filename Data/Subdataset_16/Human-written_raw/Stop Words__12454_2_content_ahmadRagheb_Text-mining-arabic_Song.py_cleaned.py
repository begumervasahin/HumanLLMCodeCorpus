import nltk
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from nltk.tokenize import word_tokenize
import stop_words
from stop_words import get_stop_words
from nltk.stem.isri import ISRIStemmer
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
class class1(object):
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        b2 = self.b1
        b3 = [nltk.word_tokenize(i) for i in b2]
        for i in b3:
            b4 = u"" + u", ".join(i) + u""
        return b4
    def fonk3(self):
        b2 = self.b1
        b3 = [nltk.word_tokenize(i) for i in b2]
        b5 = []
        for i in b3[0]:
            b5.append(i)
        return b5
    def fonk4(self):
        b6 = self.b1[0]
        b7 = get_stop_words('ar')
        b8 = nltk.word_tokenize(b6)
        b9 = [i for i in b8 if not i in b7]
        b10 = ''
        for i in b9:
            b10 = b10 + ' ' + i
        return b10
    def fonk5(self):
        b11 = ISRIStemmer()
        b12 = self.fonk3()
        b13 = ""
        for i in b12:
            b13 = b13+' '+(b11.stem(i))
        return b13
    def fonk6(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        b14 = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-full-2015-12-09/stanford-postagger.b14'
        b15 = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-full-2015-12-09/models/arabic.b16'
        b16 = StanfordPOSTagger(b15, b14)
        b16.b17 = '-mx4096m'
        b18 = b16.tag(word_tokenize(self.b1[0]))
        b10 = ''
        for i in b18:
            b19 = i[0] + ' ' + i[1]
            b10 = b10 + b19 + ' / '
        return b10
b20 = open("testfile.txt", "w")
b20.write("ÙÙØ³ Ø§ÙØ¹ÙØ¨ ÙÙ Ø£Ù ÙØ³ÙØ· Ù ÙÙÙ Ø§ÙØ¹ÙØ¨ Ø£Ù ÙØ§ ØªØ³ØªØ·ÙØ¹ Ø§ÙÙÙÙØ¶ ")
b20.write("Ù
Ù Ø§Ø­Ø¨ Ø§ÙÙÙ Ø Ø±Ø£Ù ÙÙ Ø´Ù Ø¬Ù
ÙÙØ§. ")
b20.write("Ø§ÙÙØ§Ø´ÙÙÙ ÙÙÙÙÙÙ: Ø§Ù Ø§ÙÙØ¬Ø§Ø­ ÙÙ Ù
Ø¬Ø±Ø¯ Ø­Ø¸ ")
b20.write("ÙØ§ ØªØ¨ØµÙ ÙÙ Ø§ÙØ¨Ø¦Ø± Ø ÙÙØ¯ ØªØ´Ø±Ø¨ Ù
ÙÙ ÙÙÙ
Ø§. ")
b20.write(" ÙØ³Ø±ÙØ§ Ø¥Ø¹ÙØ§Ù
ÙÙ
 Ø¨Ø¥ÙØ¶Ù
Ø§Ù
 ÙØ±ÙØ¹ÙØ§ Ø§ÙØªØ§ÙÙØ© ÙØ®Ø¯Ù
Ø© Ø¹Ù
ÙØ§Ø¦ÙØ§ Ø§ÙÙØ±Ø§Ù
  ")
b20.write(" Ø±Ø³Ù
ÙØ§Ù : Ø±ÙØ§Ù Ù
Ø¯Ø±ÙØ¯ Ø³ÙÙØ§Ø¬Ù Ø¨Ø§ÙØ±Ù Ù
ÙÙÙØ® ÙÙ Ø¯ÙØ± Ø§ÙØ±Ø¨Ø¹ Ø§ÙÙÙØ§Ø¦Ù ÙØ¯ÙØ±Ù Ø£Ø¨Ø·Ø§Ù Ø£ÙØ±ÙØ¨Ø§ ")
b20.close()
b20 = open("testfile.txt","r")
b21 = str(b20.read())
b21 = unicode(b21)
b22 = class1([b21])
print ('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n\n')
print ('\n------- tokenizer ------------\n')
print(b22.fonk3())
print ('\n------- read ------------\n')
print (b22.fonk2())
print ('\n------- stop words ------------\n')
print(b22.fonk4())
print ('\n------- b25 ------------\n')
print (b22.fonk5())
print ('\n------- part of speach ------------\n')
print (b22.fonk6())
print ('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n\n ')
print ('\n------- tokenizer ------------\n')
print(b22.fonk3())
print ('\n--------- read ------------\n')
print (b22.fonk2())
print ('\n--------- stop words ------------\n')
b23 = []
b23.append(b22.fonk4())
b24 = class1(b23)
print (b24.fonk4())
print ('\n--------- b25 ------------\n')
b25 = []
b25.append(b24.fonk5())
b26 = class1(b25)
print (b26.fonk5())
print ('\n-------- part of speach ------------\n')
print (b22.fonk6())