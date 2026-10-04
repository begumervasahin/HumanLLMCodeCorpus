import nltk
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words
from nltk.stem.isri import ISRIStemmer
from nltk.tag import StanfordPOSTagger
import os
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def read_from_list(self):
        tokenized_sents = [word_tokenize(sent) for sent in self.lyrics]
        as_list = "\n".join([", ".join(sent) for sent in tokenized_sents])
        return as_list
    def tokenizer(self):
        return word_tokenize(self.lyrics[0])
    def stop_words_remove(self):
        doc_a = self.lyrics[0]
        sw = get_stop_words('ar')
        tokens = word_tokenize(doc_a)
        stopped_tokens = [token for token in tokens if token not in sw]
        return ' '.join(stopped_tokens)
    def stemming(self):
        st = ISRIStemmer()
        tokens = self.tokenizer()
        stemmed_tokens = [st.stem(token) for token in tokens]
        return ' '.join(stemmed_tokens)
    def part_of_speech(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        jar = '/path/to/stanford-postagger.jar'
        model = '/path/to/arabic.tagger'
        tagger = StanfordPOSTagger(model, jar)
        tagger.java_options = '-mx4096m'
        tagged_text = tagger.tag(word_tokenize(self.lyrics[0]))
        return ' / '.join([f"{word} {tag}" for word, tag in tagged_text])
with open("testfile.txt", "w", encoding="utf-8") as file:
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
with open("testfile.txt", "r", encoding="utf-8") as file:
    rawsong = file.read()
my_song = Song([rawsong])
print('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n')
print('\n------- Tokenizer ------------\n')
print(my_song.tokenizer())
print('\n------- Read ------------\n')
print(my_song.read_from_list())
print('\n------- Stop Words Removal ------------\n')
print(my_song.stop_words_remove())
print('\n------- Stemming ------------\n')
print(my_song.stemming())
print('\n------- Part of Speech ------------\n')
print(my_song.part_of_speech())
print('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n')
print('\n------- Tokenizer ------------\n')
print(my_song.tokenizer())
print('\n--------- Read ------------\n')
print(my_song.read_from_list())
print('\n--------- Stop Words Removal ------------\n')
song_stop_word_removed = [my_song.stop_words_remove()]
my_song_stage2 = Song(song_stop_word_removed)
print(my_song_stage2.stop_words_remove())
print('\n--------- Stemming ------------\n')
stemming = [my_song_stage2.stemming()]
my_song_stage3 = Song(stemming)
print(my_song_stage3.stemming())
print('\n-------- Part of Speech ------------\n')
print(my_song.part_of_speech())