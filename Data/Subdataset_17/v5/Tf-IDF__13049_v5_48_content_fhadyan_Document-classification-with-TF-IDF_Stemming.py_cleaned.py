import os
from nltk.stem.porter import PorterStemmer
from UniqueWord import UniqueWord
class Stemming:
    def __init__(self):
        self.source_path = "output/training/stopword/"
        self.output_path = "output/training/stem/"
        self.ensure_source_directory_not_empty()
    def ensure_source_directory_not_empty(self):
        if not os.listdir(self.source_path):
            unique_word_processor = UniqueWord()
            unique_word_processor.output()
    def stem_files(self):
        stemmer = PorterStemmer()
        for filename in os.listdir(self.source_path):
            if not filename.endswith('.txt'):
                continue
            self.process_file(stemmer, filename)
    def process_file(self, stemmer, filename):
        source_file_path = os.path.join(self.source_path, filename)
        output_file_path = os.path.join(self.output_path, filename)
        with open(source_file_path, 'r') as source_file, open(output_file_path, 'wb') as output_file:
            lines = source_file.readlines()
            for line in lines:
                stemmed_word = stemmer.stem(line[:-5])
                output_line = f"{stemmed_word} - {line[-2]}\n"
                output_file.write(output_line.encode('utf-8'))
if __name__ == "__main__":
    stemming_processor = Stemming()
    stemming_processor.stem_files()