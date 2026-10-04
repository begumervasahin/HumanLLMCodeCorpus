import os
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
import re
class UniqueWord:
    def __init__(self, input_path='dataset/training101/', output_path='output/training/unique/'):
        self.input_path = input_path
        self.output_path = output_path
    def process_file(self, filename):
        fullname = os.path.join(self.input_path, filename)
        raw_text = self.extract_text_from_xml(fullname)
        cleaned_text = self.clean_text(raw_text)
        word_freq = self.tokenize_and_count(cleaned_text)
        self.write_output(filename, word_freq)
    def extract_text_from_xml(self, filepath):
        tree = ET.parse(filepath)
        return ET.tostring(tree.getroot(), encoding='iso-8859-1', method='text').decode('utf-8')
    def clean_text(self, text):
        return re.sub(r'[^a-zA-Z\s]', '', text)
    def tokenize_and_count(self, text):
        tokens = nltk.word_tokenize(text, language='english')
        return FreqDist(tokens)
    def write_output(self, filename, word_freq):
        output_filename = os.path.join(self.output_path, filename.replace('.xml', '.txt'))
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for word, count in word_freq.items():
                output_file.write(f"{word} - {count}\n")
    def output(self):
        os.makedirs(self.output_path, exist_ok=True)
        for filename in os.listdir(self.input_path):
            if filename.endswith('.xml'):
                self.process_file(filename)
if __name__ == '__main__':
    res = UniqueWord()
    res.output()