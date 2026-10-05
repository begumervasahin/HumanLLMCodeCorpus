import os
import json
import codecs
def fonk1(b7, b8, b9):
    b1 = []
    for relevant_doc in b7:
        with codecs.open(os.path.join(b9, f"{relevant_doc}.json"), "r", "utf-8") as file:
            b2 = json.load(file)
            b3 = b2["lines"]
            for line in b3:
                b4 = line.get('b4', '').strip()
                if b4:
                    b4 = b4.replace("-LRB-", " ( ").replace("-RRB-", " ) ")
                    b5 = {'id': relevant_doc, 'line_num': line['line_num'], 'b10': b4}
                    b1.append(b5)
    return b1
def fonk2(wiki_doc_dir, doc_filename, sentence_id):
    with codecs.open(os.path.join(wiki_doc_dir, f"{doc_filename}.txt"), "r", "utf-8") as doc:
        b6 = doc.read().splitlines()
        return b6[sentence_id].split("\t")[1] if sentence_id < len(b6) else None
b7 = ["doc1", "doc2"]
b8 = ["entity1", "entity2"]
b9 = "path/to/wiki/split/docs"
b1 = fonk1(b7, b8, b9)
print(b1)
b10 = fonk2("path/to/wiki/docs", "example_doc", 3)
print(b10)