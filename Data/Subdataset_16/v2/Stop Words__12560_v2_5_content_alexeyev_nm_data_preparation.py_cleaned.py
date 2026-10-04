import logging
import re
from pymystem3 import Mystem
logging.basicConfig(b1 = logging.INFO, format='%(asctime)s %(message)s')
logging.info("Loading mystem")
b2 = Mystem()
logging.info("Loaded mystem")
def fonk1(gr):
    b3 = re.search(r'\(([^\)]*)\)', gr)
    if b3:
        b4 = b3.group(1)
        for option in b4.split('|'):
            yield gr.replace(f"({b4})", option)
    else:
        yield gr
def fonk2(input_path):
    b5 = set()
    with open(input_path, "r", b6 = "utf-8") as input_file:
        logging.info("File opened")
        for line in input_file:
            for word in b2.analyze(line):
                if 'analysis' in word:
                    for analysis in word['analysis']:
                        for gramm_info in fonk1(analysis['gr']):
                            b7 = "\t".join([gramm_info, analysis['lex'], word['text'].lower()]) + "\n"
                            b5.add(b7)
    return b5
def fonk3(b5, output_path):
    with open(output_path, "w", b6 = "utf-8") as output_file:
        for line in b5:
            output_file.write(line)
def fonk4(input_path):
    b8 = {}
    with open(input_path, "r", b6 = "utf-8") as input_file:
        for line in input_file:
            if line.strip():
                desc, normal, b9 = line.strip().split("\t")
                if desc not in b8:
                    b8[desc] = []
                b8[desc].append((normal, b9))
    return b8
def fonk5(b8, output_path):
    with open(output_path, "w", b6 = "utf-8") as writer:
        for desc, pairs in b8.items():
            for p0 in pairs:
                for p1 in pairs:
                    if p0 != p1:
                        writer.write("\t".join([p0[0], p0[1], p1[0], p1[1]]) + "\n")
def fonk6():
    b10 = "data/test.txt"
    b11 = "data/pairs_with_grammar.tsv"
    b12 = "data/relations.pairs.tsv"
    b5 = fonk2(b10)
    fonk3(b5, b11)
    b8 = fonk4(b11)
    logging.info("Pairs acquired")
    fonk5(b8, b12)
    logging.info("Relations pairs acquired")
if b13 = = "__main__":
    fonk6()