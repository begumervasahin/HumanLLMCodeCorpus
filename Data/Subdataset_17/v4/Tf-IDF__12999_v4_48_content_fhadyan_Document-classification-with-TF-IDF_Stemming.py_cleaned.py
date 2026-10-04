import os
from nltk.stem.porter import PorterStemmer
import nltk
from UniqueWord import UniqueWord
class Stemming:
    def __init__(self):
        self.source_path = "output/training/stopword/"
        self.output_path = "output/training/stem/"
        if not os.listdir(self.source_path):
            u = UniqueWord()
            u.output()
    def stem(self):
        stemmer = PorterStemmer()
        for filename in os.listdir(self.source_path):
            if not filename.endswith('.txt'):
                continue
            source_file_path = os.path.join(self.source_path, filename)
            output_file_path = os.path.join(self.output_path, filename)
            with open(source_file_path, 'r') as source_file, open(output_file_path, 'wb') as output_file:
                lines = source_file.readlines()
                for line in lines:
                    stemmed_word = stemmer.stem(line[:-5])
                    output_line = f"{stemmed_word} - {line[-2]}\n"
                    output_file.write(output_line.encode('utf-8'))
if __name__ == "__main__":
    stemmer = Stemming()
    stemmer.stem()