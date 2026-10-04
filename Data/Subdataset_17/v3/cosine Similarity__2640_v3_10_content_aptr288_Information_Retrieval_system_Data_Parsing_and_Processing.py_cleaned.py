import re
from nltk.stem import PorterStemmer
def extract_data(filepath, stop_word_list):
    ps = PorterStemmer()
    total_doc = ""
    final_word_list = []
    doc_num_list = []
    with open(filepath, 'r') as file:
        for line in file:
            striped_line = line.strip() + " "
            total_doc += striped_line
            if "<DOCNO>" in striped_line:
                doc_num_match = re.search(r'<DOCNO>(.*?)</DOCNO>', striped_line)
                if doc_num_match:
                    doc_num = doc_num_match.group(1)
                    doc_num_list.append(doc_num)
    text_blocks = re.findall(r'<TEXT>(.*?)</TEXT>', total_doc)
    for text in text_blocks:
        cleaned_text = clean_text(text)
        words = remove_stopwords(cleaned_text, stop_word_list)
        stemmed_words = stem_words(words, ps)
        final_word_list.extend(stemmed_words)
    return final_word_list, doc_num_list
def clean_text(text):
    text = text.strip()
    text = re.sub(r'\w*-*\d+-*\w*', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\W+', ' ', text)
    return text.lower()
def remove_stopwords(text, stop_word_list):
    words = re.split(r'\s+', text)
    return [word for word in words if word not in stop_word_list]
def stem_words(words, stemmer):
    return [stemmer.stem(word) for word in words if word]
def main():
    filepath = 'path_to_your_file'
    stop_word_list = ['your', 'stop', 'words', 'here']
    final_word_list, doc_num_list = extract_data(filepath, stop_word_list)
    print(f"Final Word List: {final_word_list}")
    print(f"Document Numbers: {doc_num_list}")
if __name__ == "__main__":
    main()