import os
import subprocess
import sys
import spacy_udpipe
import stanza
import trankit
from uralicNLP import uralicApi
def run_subprocess(command):
    subprocess.run(command, stdout=sys.stdout, check=True)
def download_spacy_models():
    print('Downloading spaCy models...')
    spacy_models = ['fi_core_news_sm', 'fi_core_news_md', 'fi_core_news_lg']
    for model in spacy_models:
        run_subprocess(['python', '-m', 'spacy', 'download', model])
def download_udpipe_models():
    print('Downloading UDPipe models...')
    udpipe_models = ['fi-tdt', 'fi']
    for model in udpipe_models:
        spacy_udpipe.download(model)
def download_stanza_models():
    print('Downloading Stanza models...')
    model_dir = 'models/stanza_resources'
    os.makedirs(model_dir, exist_ok=True)
    stanza.download('fi', model_dir=model_dir)
def download_trankit_models():
    print('Downloading Trankit models...')
    cache_dir = 'models/trankit_resources'
    trankit.Pipeline('finnish', cache_dir=cache_dir)
    trankit.Pipeline('finnish', embedding='xlm-roberta-large', cache_dir=cache_dir)
def download_uralicnlp_models():
    print('Downloading UralicNLP models...')
    uralicApi.download("fin")
def download_all_models():
    download_spacy_models()
    download_udpipe_models()
    download_stanza_models()
    download_trankit_models()
    download_uralicnlp_models()
if __name__ == "__main__":
    print("Starting the model download process...")
    download_all_models()
    print("All models downloaded successfully.")