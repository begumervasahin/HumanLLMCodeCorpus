import logging
import re
from pymystem3 import Mystem
logging.basicConfig(b1 = logging.DEBUG, format='%(asctime)s %(message)s', handlers=[logging.StreamHandler()])
logging.info("Loading Mystem")
b2 = Mystem()
logging.info("Mystem loaded")
def fonk1(grammar):
    b3 = re.search(r'\(([^)]*)\)', grammar, re.IGNORECASE)
    if b3:
        b4 = b3.group(1)
        for option in b4.split('|'):
            yield grammar.replace(f"({b4})", option)
    else:
        yield grammar
b5 = "data/test.txt"
b6 = "data/pairs_with_grammar.tsv"
b7 = "data/relations.pairs.tsv"
b8 = set()
with open(b5, "r") as input_file:
    logging.info("File opened for reading")
    for line in input_file:
        b9 = b2.analyze(line)
        for word in b9:
            if 'analysis' in word:
                for analysis in word['analysis']:
                    for grammar in fonk1(analysis['gr']):
                        b10 = "\t".join([grammar, analysis['lex'], word['text'].lower()])
                        b8.add(b10.encode("utf-8") + b"\n")
with open(b6, "w+") as parsed_output_file:
    for line in b8:
        parsed_output_file.write(line.decode("utf-8"))
b11 = {}
with open(b6, "r") as parsed_output_file:
    for line in parsed_output_file:
        if line.strip():
            description, lemma, b12 = line.strip().split("\t")
            if description not in b11:
                b11[description] = []
            b11[description].append((lemma, b12))
logging.info("Pairs acquired")
with open(b7, "w") as relations_output_file:
    for description, pairs in b11.items():
        for pair1 in pairs:
            for pair2 in pairs:
                if pair1 != pair2:
                    relations_output_file.write("\t".join([pair1[0], pair1[1], pair2[0], pair2[1]]) + "\n")
logging.info("Relations pairs acquired")