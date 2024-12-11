11. Repository: sidmishraw/cs-267-project
   File: main.py
   URL: https:
   Code Content:
from re import sub
from json import dumps
from json import loads
from os.path import sep
from os.path import exists
import numpy as np
import pandas as pd
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
    '''
    Sets up the `corpora/stopwords` resource which is used for stemming by NLTK.
    :return: `None`
    '''
    if exists('mystopwords/corpora/stopwords') == False:
        download(b10 = 'mystopwords')
    return
def fonk2():
    '''
    Reads in data and initializes the pipeline.
    :return: `None`
    '''
    global b1, b3, b4, b6
    with open('properties.json', 'r') as props_read:
        b6 = loads(props_read.read())
    (b1, b2) = read_input_files(b6[b7])
    b3 = list(b2.keys())
    b4 = sorted(b1.keys())
def fonk3():
    '''
    Compute the term frequencies.
    :return: `None`
    '''
    global b4, b6
    b11 = dict()
    for doc in b4:
        b11[doc] = determine_word_positions(b1[doc])
    with open('{b12}{sep}output_term_freq.json'.format(\
        b12 = b6[b9], sep = sep), 'w') as tf_file_output:
        tf_file_output.write(dumps(b11, b13 = True, indent=2))
def fonk4():
    '''
    Computes the df.
    '''
    global b4, b3, b1, b6, b5
    b5 = determine_doc_frequency(b4, b3, b1)
    b5.to_csv('{b12}{sep}output_doc_freq.csv'.format(\
        b12 = b6[b9], sep = sep), header=b3, sep=',')
    np.savetxt('{b12}{sep}output_doc_freq.txt'.format(\
        b12 = b6[b9], sep = sep), b5.values, fmt='%d')
def fonk5():
    '''
    Use Simplical Complex algorithm to find frequent itemset.
    :return: `None`
    '''
    global b5, b6
    b14 = ''
    for index, series in b5.iterrows():
        b15 = r'\s+'
        b16 = np.array_str(series.values)
        b16 = sub(b15, '', b16)
        b14 += b14 + b16[1:len(b3)]
        b17 = b16[1:(len(b3))].encode('utf-8')
    b17 = b14.encode('utf-8')
    b18 = SimplicialComplex(shared_obj_path = b6[b8])
    b18.directProcess(1, 0.05, len(b3) - 1, len(b4), b17)
if b19 = = '__main__':
    fonk1()
    fonk2()
    fonk3()
    fonk4()
    fonk5()
   README Content:
Simplicial Complex Text Analysis
![](./thumbnail.png)
* PDF parser
* Word Stemmer
* Apriori modified version
