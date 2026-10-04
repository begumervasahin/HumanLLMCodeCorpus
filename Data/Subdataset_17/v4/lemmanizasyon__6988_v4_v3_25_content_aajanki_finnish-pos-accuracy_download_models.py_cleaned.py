import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
def download_spacy_models():
    print('Downloading spaCy models...')
    models = ['fi_core_news_sm', 'fi_core_news_md', 'fi_core_news_lg']
    for model in models:
        subprocess.run(['python', '-m', 'spacy', 'download', model], stdout=sys.stdout, check=True)
def download_udpipe_model():
    print('Downloading UDPipe model...')
    models = ['fi-tdt', 'fi']
    for model in models:
        spacy_udpipe.download(model)
def download_stanza_model():
    print('Downloading Stanza model...')
    model_dir = 'models/stanza_resources'
    os.makedirs(model_dir, exist_ok=True)
    stanza.download('fi', model_dir=model_dir)
def download_trankit_model():
    print('Downloading Trankit model...')
    cache_dir = 'models/trankit_resources'
    trankit.Pipeline('finnish', cache_dir=cache_dir)
    trankit.Pipeline('finnish', embedding='xml-roberta-large', cache_dir=cache_dir)
def download_uralicnlp_model():
    print('Downloading UralicNLP model...')
    uralicApi.download("fin")
def download_all_models():
    download_spacy_models()
    download_udpipe_model()
    download_stanza_model()
    download_trankit_model()
    download_uralicnlp_model()
if __name__ == "__main__":
    print("Initializing model downloads...")
    download_all_models()
    print("Model downloads completed successfully.")