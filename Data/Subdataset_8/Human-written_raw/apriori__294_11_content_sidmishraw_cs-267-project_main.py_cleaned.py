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
corpus = None
tokens = None
token_list = None
docs = None
df_output = None
props = None
__INPUT_FILEPATH__ = 'input_jsons_filepath'
__SHARED_OBJ_FILEPATH__ = 'shared_obj_filepath'
__OUTPUT_FILEPATH__ = 'output_filepath'
def nltk_stopwords_setup():
    '''
    Sets up the `corpora/stopwords` resource which is used for stemming by NLTK.
    :return: `None`
    '''
    if exists('mystopwords/corpora/stopwords') == False:
        download(download_dir = 'mystopwords')
    return
def read_data_init():
    '''
    Reads in data and initializes the pipeline.
    :return: `None`
    '''
    global corpus, token_list, docs, props
    with open('properties.json', 'r') as props_read:
        props = loads(props_read.read())
    (corpus, tokens) = read_input_files(props[__INPUT_FILEPATH__])
    token_list = list(tokens.keys())
    docs = sorted(corpus.keys())
def get_term_frequency():
    '''
    Compute the term frequencies.
    :return: `None`
    '''
    global docs, props
    term_frequency_with_positions = dict()
    for doc in docs:
        term_frequency_with_positions[doc] = determine_word_positions(corpus[doc])
    with open('{filepath}{sep}output_term_freq.json'.format(\
        filepath = props[__OUTPUT_FILEPATH__], sep = sep), 'w') as tf_file_output:
        tf_file_output.write(dumps(term_frequency_with_positions, sort_keys=True, indent=2))
def compute_df():
    '''
    Computes the df.
    '''
    global docs, token_list, corpus, props, df_output
    df_output = determine_doc_frequency(docs, token_list, corpus)
    df_output.to_csv('{filepath}{sep}output_doc_freq.csv'.format(\
        filepath = props[__OUTPUT_FILEPATH__], sep = sep), header=token_list, sep=',')
    np.savetxt('{filepath}{sep}output_doc_freq.txt'.format(\
        filepath = props[__OUTPUT_FILEPATH__], sep = sep), df_output.values, fmt='%d')
def process_simplical_cmplx():
    '''
    Use Simplical Complex algorithm to find frequent itemset.
    :return: `None`
    '''
    global df_output, props
    string_vector_all = ''
    for index, series in df_output.iterrows():
        whitespace_regex = r'\s+'
        string_vector = np.array_str(series.values)
        string_vector = sub(whitespace_regex, '', string_vector)
        string_vector_all += string_vector_all + string_vector[1:len(token_list)]
        bit_vector_as_string = string_vector[1:(len(token_list))].encode('utf-8')
    bit_vector_as_string = string_vector_all.encode('utf-8')
    sc2 = SimplicialComplex(shared_obj_path = props[__SHARED_OBJ_FILEPATH__])
    sc2.directProcess(1, 0.05, len(token_list) - 1, len(docs), bit_vector_as_string)
if __name__ == '__main__':
    nltk_stopwords_setup()
    read_data_init()
    get_term_frequency()
    compute_df()
    process_simplical_cmplx()
   README Content:
Simplicial Complex Text Analysis
![](./thumbnail.png)
* PDF parser
* Word Stemmer
* Apriori modified version
