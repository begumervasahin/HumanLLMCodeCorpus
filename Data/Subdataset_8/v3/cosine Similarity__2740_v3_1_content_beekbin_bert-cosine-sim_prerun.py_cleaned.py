import urllib.request
import os
import zipfile
data_dir = 'data/'
model_dir = 'models/'
urls = {
    'bert_model': 'https:
    'bert_config': 'https:
    'bert_vocab': 'https:
    'stsb_dataset': 'https:
}
os.makedirs(data_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)
def download_file(url, filename):
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, os.path.join(filename))
    print(f"{filename} downloaded.")
def extract_zip(zip_file, destination):
    print(f"Extracting {zip_file}...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)
    print(f"{zip_file} extracted.")
def download_models():
    for name, url in urls.items():
        if name == 'stsb_dataset':
            download_file(url, os.path.join(data_dir, name + '.zip'))
            extract_zip(os.path.join(data_dir, name + '.zip'), data_dir)
            os.remove(os.path.join(data_dir, name + '.zip'))
        else:
            download_file(url, os.path.join(model_dir, name))
    print("Download process completed.")
download_models()