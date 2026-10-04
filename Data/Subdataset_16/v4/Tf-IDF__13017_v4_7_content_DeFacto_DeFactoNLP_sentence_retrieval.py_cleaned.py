import os
import json
import codecs
import nltk
def fonk1(relevant_docs, entities, wiki_split_docs_dir):
    b1 = []
    for doc_name in relevant_docs:
        b2 = os.path.join(wiki_split_docs_dir, f"{doc_name}.json")
        with codecs.open(b2, "r", "utf-8") as file:
            b3 = json.load(file)
        b4 = [b5['content'].strip() for b5 in b3["b4"]]
        for i, b5 in enumerate(b4):
            b5 = b5.replace("-LRB-", " ( ").replace("-RRB-", " ) ")
            if not b5:
                continue
            b1.append({
                'id': doc_name,
                'line_num': i,
                'sentence': b5
            })
    return b1
def fonk2(wiki_doc_dir, doc_filename, sentence_id):
    b2 = os.path.join(wiki_doc_dir, f"{doc_filename}.txt")
    with codecs.open(b2, "r", "utf-8") as file:
        b4 = file.read().split("\n")
    return b4[sentence_id].split("\t")[1]