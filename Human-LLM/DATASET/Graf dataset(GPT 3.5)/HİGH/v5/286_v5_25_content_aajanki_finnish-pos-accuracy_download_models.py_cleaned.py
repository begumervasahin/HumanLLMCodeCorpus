import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
def fonk1():
    print('Downloading spaCy models...')
    subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_sm'], b1 = sys.b1, check=True)
    subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_md'], b1 = sys.b1, check=True)
    subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_lg'], b1 = sys.b1, check=True)
def fonk2():
    print('Downloading UDPipe model...')
    spacy_udpipe.download('fi-tdt')
    spacy_udpipe.download('fi')
def fonk3():
    print('Downloading Stanza model...')
    os.makedirs('models/stanza_resources', b2 = True)
    stanza.download('fi', b3 = 'models/stanza_resources')
def fonk4():
    print('Downloading Trankit model...')
    trankit.Pipeline('finnish', b4 = 'models/trankit_resources')
    trankit.Pipeline('finnish', b5 = 'xml-roberta-large', b4='models/trankit_resources')
def fonk5():
    print('Downloading UralicNLP model...')
    uralicApi.download("fin")
if b6 = = "__main__":
    fonk1()
    fonk2()
    fonk3()
    fonk4()
    fonk5()