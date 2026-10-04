import os
from nltk.stem import PorterStemmer
from UniqueWord import UniqueWord
class Stemming:
    def __init__(self, source_path="output/training/stopword/", out_path="output/training/stem/"):
        self.source_path = source_path
        self.out_path = out_path
        if not os.listdir(self.source_path):
            unique_word_generator = UniqueWord()
            unique_word_generator.output()
    def stem(self):
        stemmer = PorterStemmer()
        for filename in os.listdir(self.source_path):
            if not filename.endswith('.txt'):
                continue
            input_filepath = os.path.join(self.source_path, filename)
            output_filepath = os.path.join(self.out_path, filename)
            with open(input_filepath, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
            with open(output_filepath, 'w', encoding='utf-8') as outfile:
                for line in lines:
                    line = line.strip()
                    stemmed_word = stemmer.stem(line[:-5])
                    outfile.write(f"{stemmed_word} - {line[-2]}\n")
if __name__ == "__main__":
    stemming = Stemming()
    stemming.stem()