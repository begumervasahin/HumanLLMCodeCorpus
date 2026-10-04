import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
def fonk1(command):
    subprocess.run(command, b1 = sys.b1, check=True)
def fonk2():
    print('Downloading spaCy models...')
    b2 = ['fi_core_news_sm', 'fi_core_news_md', 'fi_core_news_lg']
    for model in b2:
        fonk1(['python', '-m', 'spacy', 'download', model])
def fonk3():
    print('Downloading UDPipe models...')
    b3 = ['fi-tdt', 'fi']
    for model in b3:
        spacy_udpipe.download(model)
def fonk4():
    print('Downloading Stanza models...')
    b4 = 'models/stanza_resources'
    os.makedirs(b4, b5 = True)
    stanza.download('fi', b4 = b4)
def fonk5():
    print('Downloading Trankit models...')
    b6 = 'models/trankit_resources'
    trankit.Pipeline('finnish', b6 = b6)
    trankit.Pipeline('finnish', b7 = 'xlm-roberta-large', b6=b6)
def fonk6():
    print('Downloading UralicNLP models...')
    uralicApi.download("fin")
def fonk7():
    fonk2()
    fonk3()
    fonk4()
    fonk5()
    fonk6()
if b8 = = "__main__":
    print("Starting the model download process...")
    fonk7()
    print("All models downloaded successfully.")