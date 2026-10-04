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
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def read_from_list(self):
        example = self.lyrics
        tokenized_sents = [nltk.word_tokenize(i) for i in example]
        for i in tokenized_sents:
            as_list = u"" + u", ".join(i) + u""
        return as_list
    def tokenizer(self):
        example = self.lyrics
        tokenized_sents = [nltk.word_tokenize(i) for i in example]
        xsd=[]
        for i in tokenized_sents[0]:
            xsd.append(i)
        return xsd
    def stop_words_remove(self):
        doc_a = self.lyrics[0]
        sw = get_stop_words('ar')
        tokens = nltk.word_tokenize(doc_a)
        stopped_tokens = [i for i in tokens if not i in sw]
        s = ''
        for i in stopped_tokens:
            s = s + ' ' + i
        return s
    def steamming(self):
        st = ISRIStemmer()
        lis = self.tokenizer()
        xx=""
        for i in lis:
            xx=xx+' '+(st.stem(i))
        return xx
    def part_of_speeach(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        jar = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-full-2015-12-09/stanford-postagger.jar'
        model = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-full-2015-12-09/models/arabic.tagger'
        tagger = StanfordPOSTagger(model, jar)
        tagger.java_options = '-mx4096m'
        text = tagger.tag(word_tokenize(self.lyrics[0]))
        s = ''
        for i in text:
            f = i[0] + ' ' + i[1]
            s = s + f + ' / '
        return s
file = open("testfile.txt", "w")
file.write("ÙÙØ³ Ø§ÙØ¹ÙØ¨ ÙÙ Ø£Ù ÙØ³ÙØ· Ù ÙÙÙ Ø§ÙØ¹ÙØ¨ Ø£Ù ÙØ§ ØªØ³ØªØ·ÙØ¹ Ø§ÙÙÙÙØ¶ ")
file.write("Ù
Ù Ø§Ø­Ø¨ Ø§ÙÙÙ Ø Ø±Ø£Ù ÙÙ Ø´Ù Ø¬Ù
ÙÙØ§. ")
file.write("Ø§ÙÙØ§Ø´ÙÙÙ ÙÙÙÙÙÙ: Ø§Ù Ø§ÙÙØ¬Ø§Ø­ ÙÙ Ù
Ø¬Ø±Ø¯ Ø­Ø¸ ")
file.write("ÙØ§ ØªØ¨ØµÙ ÙÙ Ø§ÙØ¨Ø¦Ø± Ø ÙÙØ¯ ØªØ´Ø±Ø¨ Ù
ÙÙ ÙÙÙ
Ø§. ")
file.write(" ÙØ³Ø±ÙØ§ Ø¥Ø¹ÙØ§Ù
ÙÙ
 Ø¨Ø¥ÙØ¶Ù
Ø§Ù
 ÙØ±ÙØ¹ÙØ§ Ø§ÙØªØ§ÙÙØ© ÙØ®Ø¯Ù
Ø© Ø¹Ù
ÙØ§Ø¦ÙØ§ Ø§ÙÙØ±Ø§Ù
  ")
file.write(" Ø±Ø³Ù
ÙØ§Ù : Ø±ÙØ§Ù Ù
Ø¯Ø±ÙØ¯ Ø³ÙÙØ§Ø¬Ù Ø¨Ø§ÙØ±Ù Ù
ÙÙÙØ® ÙÙ Ø¯ÙØ± Ø§ÙØ±Ø¨Ø¹ Ø§ÙÙÙØ§Ø¦Ù ÙØ¯ÙØ±Ù Ø£Ø¨Ø·Ø§Ù Ø£ÙØ±ÙØ¨Ø§ ")
file.close()
file = open("testfile.txt","r")
rawsong=str(file.read())
rawsong= unicode(rawsong)
my_song= Song([rawsong])
print ('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n\n')
print ('\n------- tokenizer ------------\n')
print(my_song.tokenizer())
print ('\n------- read ------------\n')
print (my_song.read_from_list())
print ('\n------- stop words ------------\n')
print(my_song.stop_words_remove())
print ('\n------- steamming ------------\n')
print (my_song.steamming())
print ('\n------- part of speach ------------\n')
print (my_song.part_of_speeach())
print ('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n\n ')
print ('\n------- tokenizer ------------\n')
print(my_song.tokenizer())
print ('\n--------- read ------------\n')
print (my_song.read_from_list())
print ('\n--------- stop words ------------\n')
song_stop_word_removed=[]
song_stop_word_removed.append(my_song.stop_words_remove())
my2 =Song(song_stop_word_removed)
print (my2.stop_words_remove())
print ('\n--------- steamming ------------\n')
steamming=[]
steamming.append(my2.steamming())
my3=Song(steamming)
print (my3.steamming())
print ('\n-------- part of speach ------------\n')
print (my_song.part_of_speeach())