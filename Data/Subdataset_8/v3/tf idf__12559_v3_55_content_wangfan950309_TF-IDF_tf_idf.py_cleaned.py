import pandas as pd
import math
import numpy as np
def calculate_idf(search_terms, job_names):
    idf_values = {}
    total_jobs = len(job_names)
    for term in search_terms:
        term_count = sum(1 for name in job_names if term in name)
        idf_values[term] = math.log(total_jobs / (1 + term_count))
    return idf_values
def calculate_tf_idf(search_terms, idf_values, job_names):
    tf_idf_values = pd.DataFrame()
    for term in search_terms:
        term_tf_values = []
        for name in job_names:
            word_count = len(name.split())
            term_count = sum(1 for word in name.split() if word.lower() == term.lower())
            term_tf_values.append(term_count / word_count)
        tf_idf_values[term] = np.array(term_tf_values) * idf_values[term]
    return tf_idf_values
def search_algorithm(keywords, csv_file_path):
    search_terms = keywords.split()
    job_data = pd.read_csv(csv_file_path, index_col=None)
    job_names = job_data['Job_Name'].tolist()
    idf_values = calculate_idf(search_terms, job_names)
    tf_idf_values = calculate_tf_idf(search_terms, idf_values, job_names)
    job_data['TF-IDF'] = tf_idf_values.sum(axis=1)
    job_data = job_data.sort_values(by='TF-IDF', ascending=False)
    job_data = job_data.loc[job_data['TF-IDF'] != 0]
    job_data = job_data.iloc[:, :4]
    return job_data
csv_file_path = "path_to_your_data/Job_search.csv"
keywords = "data science"
result = search_algorithm(keywords, csv_file_path)
print(result)