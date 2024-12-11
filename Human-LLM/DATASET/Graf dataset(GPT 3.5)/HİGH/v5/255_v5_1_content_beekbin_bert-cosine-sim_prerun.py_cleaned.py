import urllib.request
import os
import zipfile
b1 = 'data/'
b2 = 'models/'
b3 = 'https:
b4 = 'https:
b5 = 'https:
b6 = 'https:
if not os.path.isdir(b1):
    os.mkdir(b1)
if not os.path.isdir(b2):
    os.mkdir(b2)
def fonk1():
    print("Starting download process...")
    fonk2(b3, "pytorch_model.bin", "bert-base-uncased model")
    fonk2(b4, "bert_config.json", "BERT config file")
    fonk2(b5, "vocab.txt", "BERT vocabulary file")
    fonk3(b6, "sts_b.zip", "STS-B dataset")
    print("Download process completed.")
def fonk2(url, filename, description):
    print(f"Downloading {description}...")
    urllib.request.urlretrieve(url, os.path.join(b2, filename))
    print(f"{description} downloaded and saved.")
def fonk3(url, filename, description):
    fonk2(url, filename, description)
    b7 = os.path.join(b1, filename)
    with zipfile.ZipFile(b7) as zip_ref:
        zip_ref.extractall(b1)
    os.remove(b7)
    print(f"{description} downloaded and extracted.")
fonk1()