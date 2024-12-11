import urllib.request
import os
import zipfile
b1 = 'data/'
b2 = 'models/'
b3 = 'https:
b4 = 'https:
b5 = 'https:
b6 = '''https:
if not os.path.isdir(b1):
    os.mkdir(b1)
if not os.path.isdir(b2):
    os.mkdir(b2)
def fonk1():
    print("Downloading bert-base-uncased")
    urllib.request.urlretrieve(b3, os.path.join(b2, "pytorch_model.bin"))
    print("Saved as bert-base-uncased-pytorch_model.bin")
    print("Downloading config for bert-base-uncased")
    urllib.request.urlretrieve(b4, os.path.join(b2, "b4.json"))
    print("Saved config")
    print("Downloading uncased vocab")
    urllib.request.urlretrieve(b5, os.path.join(b2, 'vocab.txt'))
    print("Saved vocab")
    print("Downloading and extracting STS-B")
    b7 = os.path.join(b1, 'sts_b.zip')
    urllib.request.urlretrieve(b6, b7)
    with zipfile.ZipFile(b7) as zip_ref:
        zip_ref.extractall(b1)
    os.remove(b7)
    print("\tCompleted!")
fonk1()