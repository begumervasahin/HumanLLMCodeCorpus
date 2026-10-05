import os
import sys
import zipfile
import json
import bisect
import nltk
from nltk.stem import WordNetLemmatizer
WORD_NAMESPACE = '{http:
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
ENGLISH_STOPWORDS = set(["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"])
def get_docx_text(path):
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = nltk.etree.ElementTree.XML(xml_content)
    paragraphs = []
    for paragraph in tree.iter(PARA):
        texts = [node.text for node in paragraph.iter(TEXT) if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    return '\n\n'.join(paragraphs)
def remove_stopwords(wordlist):
    return [word for word in wordlist if word not in ENGLISH_STOPWORDS]
def add_to_postings(postings, docid):
    bisect.insort(postings, docid)
    return postings
def main(input_docs_dir):
    if not os.path.exists(input_docs_dir):
        print("Input directory not found.")
        return
    INDEX_FILE = "INDEX_FILE.INDEX"
    indexDictionary = {}
    lemmatizer = WordNetLemmatizer()
    for filename in os.listdir(input_docs_dir):
        if filename.endswith(".docx"):
            doc_text = get_docx_text(os.path.join(input_docs_dir, filename))
            word_tokens = nltk.word_tokenize(doc_text)
            word_tokens = remove_stopwords(word_tokens)
            for word in word_tokens:
                lem_word = lemmatizer.lemmatize(word.lower())
                if lem_word not in indexDictionary:
                    indexDictionary[lem_word] = {'df': 0, 'postings': []}
                if filename not in indexDictionary[lem_word]['postings']:
                    indexDictionary[lem_word]['df'] += 1
                    indexDictionary[lem_word]['postings'] = add_to_postings(indexDictionary[lem_word]['postings'], filename)
    with open(INDEX_FILE, 'w') as indexFile:
        json.dump(indexDictionary, indexFile, sort_keys=True)
    print("Index file created at", INDEX_FILE)
    print("Index stats\n" + '-'*50)
    print("Number of terms:", len(indexDictionary))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing argument. Expected input docs directory as argument.\nEg: python create_index.py data")
        sys.exit()
    input_docs_dir = sys.argv[1]
    main(input_docs_dir)