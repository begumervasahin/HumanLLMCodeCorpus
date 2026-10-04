import os
import json
import codecs
import nltk
def get_relevant_sentences(relevant_docs, entities, wiki_split_docs_dir):
    relevant_sentences = []
    for doc_name in relevant_docs:
        file_path = os.path.join(wiki_split_docs_dir, f"{doc_name}.json")
        with codecs.open(file_path, "r", "utf-8") as file:
            doc_data = json.load(file)
        lines = [line['content'].strip() for line in doc_data["lines"]]
        for i, line in enumerate(lines):
            line = line.replace("-LRB-", " ( ").replace("-RRB-", " ) ")
            if not line:
                continue
            relevant_sentences.append({
                'id': doc_name,
                'line_num': i,
                'sentence': line
            })
    return relevant_sentences
def get_sentence(wiki_doc_dir, doc_filename, sentence_id):
    file_path = os.path.join(wiki_doc_dir, f"{doc_filename}.txt")
    with codecs.open(file_path, "r", "utf-8") as file:
        lines = file.read().split("\n")
    return lines[sentence_id].split("\t")[1]