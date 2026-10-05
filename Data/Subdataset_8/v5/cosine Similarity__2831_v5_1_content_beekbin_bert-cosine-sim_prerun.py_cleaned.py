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
    download_file(bert_model_url, "pytorch_model.bin", "bert-base-uncased model")
    download_file(bert_config_url, "bert_config.json", "BERT config file")
    download_file(bert_vocab_url, "vocab.txt", "BERT vocabulary file")
    download_and_extract(stsb_dataset_url, "sts_b.zip", "STS-B dataset")
    print("Download process completed.")
def download_file(url, filename, description):
    print(f"Downloading {description}...")
    urllib.request.urlretrieve(url, os.path.join(model_dir, filename))
    print(f"{description} downloaded and saved.")
def download_and_extract(url, filename, description):
    download_file(url, filename, description)
    zip_path = os.path.join(data_dir, filename)
    with zipfile.ZipFile(zip_path) as zip_ref:
        zip_ref.extractall(data_dir)
    os.remove(zip_path)
    print(f"{description} downloaded and extracted.")
download_models()