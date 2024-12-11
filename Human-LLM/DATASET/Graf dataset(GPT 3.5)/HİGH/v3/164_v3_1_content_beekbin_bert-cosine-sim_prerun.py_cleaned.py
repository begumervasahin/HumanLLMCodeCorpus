import urllib.request
import os
import zipfile
b1 = 'data/'
b2 = 'models/'
b3 = {
    'bert_model': 'https:
    'bert_config': 'https:
    'bert_vocab': 'https:
    'stsb_dataset': 'https:
}
os.makedirs(b1, b4 = True)
os.makedirs(b2, b4 = True)
def fonk1(url, filename):
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, os.path.join(filename))
    print(f"{filename} downloaded.")
def fonk2(zip_file, destination):
    print(f"Extracting {zip_file}...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)
    print(f"{zip_file} extracted.")
def fonk3():
    for b5, url in b3.items():
        if b5 = = 'stsb_dataset':
            fonk1(url, os.path.join(b1, b5 + '.zip'))
            fonk2(os.path.join(b1, b5 + '.zip'), b1)
            os.remove(os.path.join(b1, b5 + '.zip'))
        else:
            fonk1(url, os.path.join(b2, b5))
    print("Download process completed.")
fonk3()