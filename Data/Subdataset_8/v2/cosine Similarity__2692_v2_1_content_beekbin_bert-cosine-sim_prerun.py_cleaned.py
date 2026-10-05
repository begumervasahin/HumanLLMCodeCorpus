import urllib.request
import os
import zipfile
data_dir = 'data/'
model_dir = 'models/'
bert_model = 'https:
bert_config = 'https:
bert_vocab = 'https:
stsb_dataset = 'https:
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)
if not os.path.isdir(model_dir):
    os.mkdir(model_dir)
def download_models():
    print("Downloading BERT model files...")
    urllib.request.urlretrieve(bert_model, os.path.join(model_dir, "pytorch_model.bin"))
    print("BERT model downloaded.")
    urllib.request.urlretrieve(bert_config, os.path.join(model_dir, "bert_config.json"))
    print("BERT config downloaded.")
    urllib.request.urlretrieve(bert_vocab, os.path.join(model_dir, 'vocab.txt'))
    print("BERT vocabulary downloaded.")
    print("Downloading and extracting STS-B dataset...")
    stsb_zip = os.path.join(data_dir, 'sts_b.zip')
    urllib.request.urlretrieve(stsb_dataset, stsb_zip)
    with zipfile.ZipFile(stsb_zip, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    os.remove(stsb_zip)
    print("STS-B dataset downloaded and extracted.")
    print("Download process completed.")
download_models()