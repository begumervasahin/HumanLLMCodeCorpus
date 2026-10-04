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
    def tokenize(self):
        return word_tokenize(self.lyrics[0])
    def remove_stop_words(self):
        tokens = word_tokenize(self.lyrics[0])
        stop_words = get_stop_words('ar')
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return ' '.join(filtered_tokens)
    def stem(self):
        stemmer = ISRIStemmer()
        tokens = self.tokenize()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return ' '.join(stemmed_tokens)
    def pos_tag(self):
        os.environ["JAVA_HOME"] = "/usr/bin/java"
        jar = '/path/to/stanford-postagger.jar'
        model = '/path/to/arabic.tagger'
        tagger = StanfordPOSTagger(model, jar)
        tagger.java_options = '-mx4096m'
        tagged_text = tagger.tag(word_tokenize(self.lyrics[0]))
        return ' / '.join([f"{word} {tag}" for word, tag in tagged_text])
def write_sample_lyrics_to_file(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
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
def read_lyrics_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
file_path = "testfile.txt"
write_sample_lyrics_to_file(file_path)
raw_song = read_lyrics_from_file(file_path)
my_song = Song([raw_song])
print('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n')
print('\n------- Tokenizer ------------\n')
print(my_song.tokenize())
print('\n------- Read from List ------------\n')
print(my_song.read_from_list())
print('\n------- Stop Words Removal ------------\n')
print(my_song.remove_stop_words())
print('\n------- Stemming ------------\n')
print(my_song.stem())
print('\n------- Part of Speech ------------\n')
print(my_song.pos_tag())
print('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n')
print('\n------- Tokenizer ------------\n')
print(my_song.tokenize())
print('\n--------- Read from List ------------\n')
print(my_song.read_from_list())
print('\n--------- Stop Words Removal ------------\n')
song_stop_word_removed = [my_song.remove_stop_words()]
my_song_stage2 = Song(song_stop_word_removed)
print(my_song_stage2.remove_stop_words())
print('\n--------- Stemming ------------\n')
stemmed = [my_song_stage2.stem()]
my_song_stage3 = Song(stemmed)
print(my_song_stage3.stem())
print('\n-------- Part of Speech ------------\n')
print(my_song.pos_tag())