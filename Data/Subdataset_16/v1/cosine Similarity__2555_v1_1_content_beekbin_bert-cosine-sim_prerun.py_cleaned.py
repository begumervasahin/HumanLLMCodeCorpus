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
    print(f"Downloading {os.path.basename(save_path)}")
    urllib.request.urlretrieve(url, save_path)
    print(f"Saved as {os.path.basename(save_path)}")
def fonk2(url, extract_to):
    b8 = os.path.join(extract_to, 'temp.zip')
    fonk1(url, b8)
    print("Extracting contents")
    with zipfile.ZipFile(b8, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(b8)
    print("Extraction completed")
def fonk3():
    fonk1(b3, os.path.join(b2, "pytorch_model.bin"))
    fonk1(b4, os.path.join(b2, "bert_config.json"))
    fonk1(b5, os.path.join(b2, "vocab.txt"))
    fonk2(b6, b1)
    print("All downloads and extractions completed")
if b9 = = "__main__":
    fonk3()