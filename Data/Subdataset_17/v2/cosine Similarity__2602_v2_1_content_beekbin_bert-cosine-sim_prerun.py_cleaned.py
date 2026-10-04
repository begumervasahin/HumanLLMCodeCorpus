import urllib.request
import os
import zipfile
DATA_DIR = 'data/'
MODEL_DIR = 'models/'
BERT_MODEL_URL = 'https:
BERT_CONFIG_URL = 'https:
BERT_VOCAB_URL = 'https:
STSB_DATASET_URL = 'https:
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
def download_file(url, save_path):
    print(f"Downloading {os.path.basename(save_path)}...")
    urllib.request.urlretrieve(url, save_path)
    print(f"Saved as {os.path.basename(save_path)}.")
def download_and_extract_zip(url, extract_to):
    zip_path = os.path.join(extract_to, 'temp.zip')
    download_file(url, zip_path)
    print("Extracting contents...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)
    print("Extraction completed.")
def download_models():
    download_file(BERT_MODEL_URL, os.path.join(MODEL_DIR, "pytorch_model.bin"))
    download_file(BERT_CONFIG_URL, os.path.join(MODEL_DIR, "bert_config.json"))
    download_file(BERT_VOCAB_URL, os.path.join(MODEL_DIR, "vocab.txt"))
    download_and_extract_zip(STSB_DATASET_URL, DATA_DIR)
    print("All downloads and extractions completed.")
if __name__ == "__main__":
    download_models()