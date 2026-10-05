import urllib.request
import os
import zipfile
data_dir = 'data/'
model_dir = 'models/'
bert_model_url = 'https:
bert_config_url = 'https:
bert_vocab_url = 'https:
stsb_dataset_url = 'https:
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)
if not os.path.isdir(model_dir):
    os.mkdir(model_dir)
def download_models():
    print("Starting download process...")
    print("Downloading bert-base-uncased model...")
    urllib.request.urlretrieve(bert_model_url, os.path.join(model_dir, "pytorch_model.bin"))
    print("BERT model downloaded and saved.")
    print("Downloading bert-base-uncased config file...")
    urllib.request.urlretrieve(bert_config_url, os.path.join(model_dir, "bert_config.json"))
    print("BERT config file downloaded and saved.")
    print("Downloading bert-base-uncased vocabulary file...")
    urllib.request.urlretrieve(bert_vocab_url, os.path.join(model_dir, 'vocab.txt'))
    print("BERT vocabulary file downloaded and saved.")
    print("Downloading STS-B dataset...")
    stsb_zip = os.path.join(data_dir, 'sts_b.zip')
    urllib.request.urlretrieve(stsb_dataset_url, stsb_zip)
    with zipfile.ZipFile(stsb_zip) as zip_ref:
        zip_ref.extractall(data_dir)
    os.remove(stsb_zip)
    print("STS-B dataset downloaded and extracted.")
    print("Download process completed.")
download_models()