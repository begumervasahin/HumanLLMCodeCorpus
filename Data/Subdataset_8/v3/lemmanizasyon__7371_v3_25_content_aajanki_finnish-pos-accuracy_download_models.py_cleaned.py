import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
def download_spacy_models():
    print('Downloading spaCy models...')
    subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_sm'], stdout=sys.stdout, check=True)
    subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_md'], stdout=sys.stdout, check=True)
    subprocess.run(['python', '-m', 'spacy', 'download', 'fi_core_news_lg'], stdout=sys.stdout, check=True)
def download_udpipe_model():
    print('Downloading UDPipe model...')
    spacy_udpipe.download('fi-tdt')
    spacy_udpipe.download('fi')
def download_stanza_model():
    print('Downloading Stanza model...')
    os.makedirs('models/stanza_resources', exist_ok=True)
    stanza.download('fi', model_dir='models/stanza_resources')
def download_trankit_model():
    print('Downloading Trankit model...')
    trankit.Pipeline('finnish', cache_dir='models/trankit_resources')
    trankit.Pipeline('finnish', embedding='xml-roberta-large', cache_dir='models/trankit_resources')
def download_uralicnlp_model():
    print('Downloading UralicNLP model...')
    uralicApi.download("fin")
def download_models():
    download_spacy_models()
    download_udpipe_model()
    download_stanza_model()
    download_trankit_model()
    download_uralicnlp_model()
if __name__ == "__main__":
    print("Initializing model downloads...")
    download_models()
    print("Model downloads completed successfully.")