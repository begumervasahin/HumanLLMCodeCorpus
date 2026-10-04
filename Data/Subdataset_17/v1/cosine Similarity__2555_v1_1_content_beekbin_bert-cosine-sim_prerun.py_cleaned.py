import urllib.request
import os
import zipfile
data_dir = 'data/'
model_dir = 'models/'
bert_model_url = 'https:
bert_config_url = 'https:
bert_vocab_url = 'https:
stsb_dataset_url = 'https:
os.makedirs(data_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)
def download_file(url, save_path):
    print(f"Downloading {os.path.basename(save_path)}")
    urllib.request.urlretrieve(url, save_path)
    print(f"Saved as {os.path.basename(save_path)}")
def download_and_extract_zip(url, extract_to):
    zip_path = os.path.join(extract_to, 'temp.zip')
    download_file(url, zip_path)
    print("Extracting contents")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)
    print("Extraction completed")
def download_models():
    download_file(bert_model_url, os.path.join(model_dir, "pytorch_model.bin"))
    download_file(bert_config_url, os.path.join(model_dir, "bert_config.json"))
    download_file(bert_vocab_url, os.path.join(model_dir, "vocab.txt"))
    download_and_extract_zip(stsb_dataset_url, data_dir)
    print("All downloads and extractions completed")
if __name__ == "__main__":
    download_models()