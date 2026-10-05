import os
import re
import math
import pathlib
import time
from collections import defaultdict
from nltk.stem import PorterStemmer
from Forward_Index_Build import indexingEachTerm
from Query_Extraction import extractDifferentQuery
from Data_Parsing_and_Processing import extractingdata
doc_num_dict = {}
word_dict = defaultdict(int)
sorted_inverted_index = {}
sorted_forward_index = {}
normalized_doc = {}
score = defaultdict(int)
current_directory = pathlib.Path('.')
start_time = time.time()
stopwords_path = current_directory / 'files' / 'stopwordlist.txt'
with open(stopwords_path, 'r') as file:
    stop_word_list = [word.strip() for line in file for word in line.split()]
extracted_text_list = []
extracted_doc_num_list = []
for i in range(15):
    filepath = current_directory / f'ft911/ft911_{i + 1}'
    text_list, doc_num_list = extractingdata(filepath, stop_word_list)
    extracted_text_list.extend(text_list)
    extracted_doc_num_list.extend(doc_num_list)
unique_texts = sorted(set(extracted_text_list))
word_counter = 1
doc_counter = 1
for text_token in unique_texts:
    word_dict[text_token] = word_counter
    word_counter += 1
for doc_num_string in extracted_doc_num_list:
    doc_num_dict[doc_num_string] = doc_counter
    doc_counter += 1
forward_index_file = open("files\\forward_index.txt", "w")
for i in range(15):
    filepath = current_directory / f'ft911/ft911_{i + 1}'
    forward_index = indexingEachTerm(filepath, stop_word_list, word_dict)
inverted_index = defaultdict(int)
for key, value in forward_index.items():
    for inner_key, inner_value in value.items():
        if inverted_index[inner_key] == 0:
            inverted_index[inner_key] = {key: inner_value}
        elif inverted_index[inner_key] != 0:
            inverted_index[inner_key].update({key: inner_value})
sorted_forward_index = {key: {inner_key: value for inner_key, value in sorted(idx.items())} for key, idx in forward_index.items()}
sorted_inverted_index = {key: {inner_key: value for inner_key, value in sorted(idx.items())} for key, idx in inverted_index.items()}
parser_output_file = open("files\\parser_output.txt", "w")
for key, value in word_dict.items():
    parser_output_file.write(f"{value}         {key}\n")
for key, value in doc_num_dict.items():
    parser_output_file.write(f"{value}         {key}\n")
for key, value in sorted_forward_index.items():
    forward_index_file.write(f"{key}         {value}\n")
forward_index_file.close()
inverted_index_file = open("files\\inverted_index.txt", "w")
for key, value in sorted_inverted_index.items():
    inverted_index_file.write(f"{key}         {value}\n")
inverted_index_file.close()
N = len(sorted_forward_index)
for key, value in sorted_forward_index.items():
    sum_of_squares = 0
    for inner_key, inner_value in value.items():
        df = len(sorted_inverted_index[inner_key])
        idf = math.log(N / df, 10)
        sum_of_squares += pow(inner_value * idf, 2)
    sqr_sum = math.sqrt(sum_of_squares)
    normalized_doc[key] = sqr_sum
total_doc = ""
query_numbers = []
with open(current_directory / 'files/topics.txt', "r+") as file:
    for line in file:
        striped_string = line.strip() + " "
        total_doc += striped_string
        if "<num>" in striped_string:
            query_num = re.sub('[^0-9]', '', striped_string)
            query_numbers.append(query_num)
titles = re.findall(r'<title>(.*?)<desc>', total_doc)
descriptions = re.findall(r'<desc> Description:(.*?)<narr>', total_doc)
narratives = re.findall(r'<narr> Narrative:(.*?)</top>', total_doc)
reference_query_docs = []
with open(current_directory / 'files/main.qrels') as file:
    for line in file:
        striped_string = line.strip().split(" ")
        query_doc_indicated = striped_string[2].split("-")
        if "FT911" in query_doc_indicated[0]:
            reference_query_docs.append(striped_string)
def calculate_precision_recall(calculated_score, query_number_to_evaluate_on):
    num_docs_given = 0
    num_relevant_docs_given = 0
    true_positive = 0
    for x in range(len(reference_query_docs)):
        if query_number_to_evaluate_on == reference_query_docs[x][0]:
            num_docs_given += 1
            if reference_query_docs[x][3] == '1':
                doc_num_in_ref = reference_query_docs[x][2].split("-")
                if int(doc_num_in_ref[1]) in calculated_score.keys():
                    true_positive += 1
                num_relevant_docs_given += 1
    precision_cal = true_positive / len(score)
    recall_cal = true_positive / num_relevant_docs_given
    calculated_score.clear()
    return precision_cal, recall_cal
query_results_file = open("files/OnlyTitleResults.txt", "w")
N = len(sorted_forward_index)
query_count = 0
score.clear()
queries_with_title = extractDifferentQuery(titles, stop_word_list)
for query_num in queries_with_title.keys():
    for query_term, tf_query in queries_with_title[query_num].items():
        query_id = word_dict[query_term]
        if query_id != 0:
            df = len(sorted_inverted_index[query_id])
            for inverted_key, tf_doc in sorted_inverted_index[query_id].items():
                idf = math.log(N / df, 10)
                tfidf = ((tf_doc * idf) * (tf_query * idf))
                score[inverted_key] += (tfidf / normalized_doc[inverted_key])
    counter_rank = 1
    for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
        query_results_file.write(f"{query_numbers[query_count]}        FT911-{key}        {counter_rank}        {value:.15f}\n")
        counter_rank += 1
    precision, recall = calculate_precision_recall(score, query_numbers[query_count])
    query_results_file.write(f"  Precision ==>  {precision}  Recall ==>  {recall}\n")
    score.clear()
    query_count += 1