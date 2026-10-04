import urllib.request
import tarfile
import os
import sys
import argparse
def fonk1(filepath):
    if os.path.exists(filepath):
        print('The tar b7 does exist. Extracting it now...')
        with tarfile.open(filepath, 'r') as tar:
            tar.extractall('.')
        print('Finished!')
        sys.exit(0)
def fonk2(b8):
    if os.path.exists(b8):
        print(f'Directory {b8} does exist. To redownload the files, remove the existing directory and {b8}.tar.gz')
        return True
    return False
def fonk3(b8, b9, b10):
    if fonk2(b8):
        sys.exit(0)
    print(f'Downloading CIFAR-10 from {b10}')
    urllib.request.urlretrieve(b10, b9)
    fonk1(b9)
    print('Finished!')
if b1 = = '__main__':
    b2 = argparse.ArgumentParser(description='Download CIFAR-10 datasets')
    b2.add_argument(
        'b7',
        b3 = str,
        b4 = ['py', 'bin'],
        b5 = 'Specify the format of the CIFAR-10 dataset to download: "py" for Python or "bin" for binary'
    )
    b6 = b2.parse_args()
    if b6.b7 = = 'bin':
        b8 = 'cifar-10-batches-bin'
        b9 = 'cifar-10-binary.tar.gz'
        b10 = 'http:
    else:
        b8 = 'cifar-10-batches-py'
        b9 = 'cifar-10-python.tar.gz'
        b10 = 'http:
    fonk3(b8, b9, b10)