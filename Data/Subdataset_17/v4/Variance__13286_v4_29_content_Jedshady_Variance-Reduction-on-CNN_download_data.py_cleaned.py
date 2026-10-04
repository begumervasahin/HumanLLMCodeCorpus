import urllib.request
import tarfile
import os
import sys
import argparse
def extract_tarfile(filepath):
    if os.path.exists(filepath):
        print('The tar file exists. Extracting it now...')
        with tarfile.open(filepath, 'r:gz') as tar:
            tar.extractall('.')
        print('Extraction finished!')
        sys.exit(0)
    else:
        print('The tar file does not exist.')
def check_dir_exist(dirpath):
    if os.path.exists(dirpath):
        print(f'Directory {dirpath} exists. To redownload the files, remove the existing directory and {dirpath}.tar.gz')
        return True
    return False
def do_download(dirpath, gzfile, url):
    if check_dir_exist(dirpath):
        sys.exit(0)
    print(f'Downloading CIFAR-10 from {url}')
    urllib.request.urlretrieve(url, gzfile)
    extract_tarfile(gzfile)
    print('Download and extraction finished!')
def main():
    parser = argparse.ArgumentParser(description='Download CIFAR-10 datasets')
    parser.add_argument('file', type=str, choices=['py', 'bin'], help='File type to download (py or bin)')
    args = parser.parse_args()
    if args.file == 'bin':
        dirpath = 'cifar-10-batches-bin'
        gzfile = 'cifar-10-binary.tar.gz'
        url = 'http:
    else:
        dirpath = 'cifar-10-batches-py'
        gzfile = 'cifar-10-python.tar.gz'
        url = 'http:
    do_download(dirpath, gzfile, url)
if __name__ == '__main__':
    main()