import os
import argparse
def gen(n):
    k = ""
    for i in range(0,n):
        k += chr(65 + ord(os.urandom(1))%26)
    return k
def str_xor(a, b):
    c = ""
    for i in range(0,len(a)):
        c += chr(64 + (ord(a[i]) ^ ord(b[i])))
    return c
def clean(a):
    return a.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def unclean(a):
    return a.replace("a", " ").replace("b", ".").replace("c", ",").replace("d","'")
parser = argparse.ArgumentParser(
    description='Encrypt or Decrypt data using One-Time Pad')
parser.add_argument('-d', '--decrypt', action='store_true',
    help='Decrypt data (default is to encrypt)')
args = parser.parse_args()
if args.decrypt:
    key = raw_input("key: ")
    coded = raw_input("coded stuff: ")
    print unclean(str_xor(key,coded))
else:
    decoded = clean(raw_input("message: "))
    key = gen(len(decoded))
    print key, str_xor(decoded, key)