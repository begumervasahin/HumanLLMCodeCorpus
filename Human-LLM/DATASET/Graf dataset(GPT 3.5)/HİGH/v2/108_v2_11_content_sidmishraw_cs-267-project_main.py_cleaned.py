
import sys
import os
import numpy as np
import pandas as pd
from re import sub
from json import dumps, loads
from os.path import sep, exists
from nltk import download
from apriori import *
from simplicial_complex import SimplicialComplex
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None
b6 = None
b7 = 'input_jsons_filepath'
b8 = 'shared_obj_filepath'
b9 = 'output_filepath'
def fonk1():
    if not exists('mystopwords/corpora/stopwords'):
        download(b10 = 'mystopwords')
def fonk2():
    global b1, b3, b4, b6
    with open('properties.json', 'r') as props_read:
        b6 = loads(props_read.read())
    b1, b2 = read_input_files(b6[b7])
    b3 = list(b2.keys())
    b4 = sorted(b1.keys())
def fonk3():
    global b4, b6
    b11 = {}
    for doc in b4:
        b11[doc] = determine_word_positions(b1[doc])
    with open(f'{b6[b9]}{sep}output_term_freq.json', 'w') as tf_file_output:
        tf_file_output.write(dumps(b11, b12 = True, indent=2))
def fonk4():
    global b4, b3, b1, b6, b5
    b5 = determine_doc_frequency(b4, b3, b1)
    b5.to_csv(f'{b6[b9]}{sep}output_doc_freq.csv', b13 = b3, sep=',')
    np.savetxt(f'{b6[b9]}{sep}output_doc_freq.txt', b5.values, b14 = '%d')
def fonk5():
    global b5, b6, b3
    b15 = ''
    for index, series in b5.iterrows():
        b16 = r'\s+'
        b17 = np.array_str(series.values)
        b17 = sub(b16, '', b17)
        b15 += b17[1:len(b3)]
        b18 = b17[1:(len(b3))].encode('utf-8')
    b18 = b15.encode('utf-8')
    b19 = SimplicialComplex(shared_obj_path=b6[b8])
    b19.directProcess(1, 0.05, len(b3) - 1, len(b4), b18)
if b20 = = '__main__':
    fonk1()
    fonk2()
    fonk3()
    fonk4()
    fonk5()