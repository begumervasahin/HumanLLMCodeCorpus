from pymystem3 import Mystem
import logging
import re
logging.basicConfig(b1 = logging.DEBUG,
                    b2 = '%(asctime)s %(message)s',
                    b3 = [logging.StreamHandler()])
logging.info("Loading mystem")
b4 = Mystem()
logging.info("Loaded mystem")
def fonk1(gr):
    b5 = re.search('\(([^\)]*)\)', gr, re.IGNORECASE)
    if b5:
        b6 = b5.group(1)
        for stuff in b6.split('|'):
            yield gr.replace("(" + b6 + ")", stuff)
    else:
        yield gr
b7 = set([])
with open("data/test.txt", "r") as input_file:
    logging.info("file opened")
    for line in input_file:
        for w in b4.analyze(line):
            if 'analysis' in w:
                for item in w['analysis']:
                    for gramm_info in fonk1(item['gr']):
                        b7.add("\t".join(
                            [gramm_info, item['lex'], w['text'].lower()]).encode("utf-8") + "\n")
with open("data/pairs_with_grammar.tsv", "w+") as f:
    for line in b7:
        f.write(line)
b8 = {}
for line in open("data/pairs_with_grammar.tsv", "r+"):
    if line.strip():
        desc, normal, b9 = line.strip().split("\t")
        if desc not in b8:
            b8[desc] = []
        b8[desc].append((normal, b9))
logging.info("Pairs acquired")
b10 = open("data/relations.pairs.tsv", "w+")
for desc in b8:
    for b11 in b8[desc]:
        for p1 in b8[desc]:
            if not b11 = = p1:
                b10.write("\t".join([b11[0], b11[1], p1[0], p1[1]]) + "\n")
b10.close()
logging.info("Relations pairs acquired")