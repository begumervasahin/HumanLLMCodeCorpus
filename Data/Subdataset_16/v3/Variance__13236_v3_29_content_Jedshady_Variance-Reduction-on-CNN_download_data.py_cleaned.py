import urllib.request
import tarfile
import os
import sys
import argparse
def fonk1(filepath):
    if os.path.exists(filepath):
        print('The tar file exists. Extracting it now...')
        with tarfile.open(filepath, 'r') as tar:
            tar.extractall('.')
        print('Extraction complete!')
        sys.exit(0)
def fonk2(b7):
    if os.path.exists(b7):
        print(f'Directory {b7} exists. To redownload the files, remove the existing directory and {b7}.tar.gz')
        return True
    return False
def fonk3(b7, b8, b9):
    if fonk2(b7):
        sys.exit(0)
    print(f'Downloading CIFAR-10 from {b9}...')
    urllib.request.urlretrieve(b9, b8)
    fonk1(b8)
    print('Download and extraction complete!')
def fonk4():
    b1 = argparse.ArgumentParser(description='Download CIFAR-10 datasets')
    b1.add_argument(
        'b6',
        b2 = str,
        b3 = ['py', 'bin'],
        b4 = 'Specify the format of the CIFAR-10 dataset to download: "py" for Python or "bin" for binary'
    )
    b5 = b1.parse_args()
    if b5.b6 = = 'bin':
        b7 = 'cifar-10-batches-bin'
        b8 = 'cifar-10-binary.tar.gz'
        b9 = 'http:
    else:
        b7 = 'cifar-10-batches-py'
        b8 = 'cifar-10-python.tar.gz'
        b9 = 'http:
    fonk3(b7, b8, b9)
if b10 = = '__main__':
    fonk4()