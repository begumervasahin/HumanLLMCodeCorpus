import urllib.request
import os
import zipfile
b1 = 'data/'
b2 = 'models/'
b3 = 'https:
b4 = 'https:
b5 = 'https:
b6 = 'https:
os.makedirs(b1, b7 = True)
os.makedirs(b2, b7 = True)
def fonk1(url, save_path):
    b8 = os.path.basename(save_path)
    print(f"Downloading {b8}...")
    urllib.request.urlretrieve(url, save_path)
    print(f"Saved as {b8}.")
def fonk2(url, extract_to):
    b9 = os.path.join(extract_to, 'temp.zip')
    fonk1(url, b9)
    print("Extracting contents...")
    with zipfile.ZipFile(b9, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(b9)
    print("Extraction completed.")
def fonk3():
    fonk1(b3, os.path.join(b2, "pytorch_model.bin"))
    fonk1(b4, os.path.join(b2, "bert_config.json"))
    fonk1(b5, os.path.join(b2, "vocab.txt"))
    fonk2(b6, b1)
    print("All downloads and extractions completed.")
if b10 = = "__main__":
    fonk3()