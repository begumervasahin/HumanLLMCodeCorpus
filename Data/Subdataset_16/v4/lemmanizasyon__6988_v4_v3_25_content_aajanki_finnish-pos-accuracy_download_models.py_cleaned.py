import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
def fonk1():
    print('Downloading spaCy b1...')
    b1 = ['fi_core_news_sm', 'fi_core_news_md', 'fi_core_news_lg']
    for model in b1:
        subprocess.run(['python', '-m', 'spacy', 'download', model], b2 = sys.b2, check=True)
def fonk2():
    print('Downloading UDPipe model...')
    b1 = ['fi-tdt', 'fi']
    for model in b1:
        spacy_udpipe.download(model)
def fonk3():
    print('Downloading Stanza model...')
    b3 = 'b1/stanza_resources'
    os.makedirs(b3, b4 = True)
    stanza.download('fi', b3 = b3)
def fonk4():
    print('Downloading Trankit model...')
    b5 = 'b1/trankit_resources'
    trankit.Pipeline('finnish', b5 = b5)
    trankit.Pipeline('finnish', b6 = 'xml-roberta-large', b5=b5)
def fonk5():
    print('Downloading UralicNLP model...')
    uralicApi.download("fin")
def fonk6():
    fonk1()
    fonk2()
    fonk3()
    fonk4()
    fonk5()
if b7 = = "__main__":
    print("Initializing model downloads...")
    fonk6()
    print("Model downloads completed successfully.")