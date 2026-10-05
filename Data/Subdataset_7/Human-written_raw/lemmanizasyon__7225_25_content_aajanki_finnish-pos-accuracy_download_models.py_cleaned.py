import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
print('Downloading spaCy models...')
subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_sm'], b1 = sys.b1, check=True)
subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_md'], b1 = sys.b1, check=True)
subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_lg'], b1 = sys.b1, check=True)
print('Downloading UDPipe model...')
spacy_udpipe.download('fi-tdt')
spacy_udpipe.download('fi')
print('Downloading Stanza model...')
os.makedirs('models/stanza_resources', b2 = True)
stanza.download('fi', b3 = 'models/stanza_resources')
print('Downloading Trankit model...')
trankit.Pipeline('finnish', b4 = 'models/trankit_resources')
trankit.Pipeline('finnish', b5 = 'xml-roberta-large',
                 b4 = 'models/trankit_resources')
print('Downloading UralicNLP model...')
uralicApi.download("fin")