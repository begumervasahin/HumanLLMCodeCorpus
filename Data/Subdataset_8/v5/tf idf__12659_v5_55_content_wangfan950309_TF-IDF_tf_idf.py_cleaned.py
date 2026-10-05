import pandas as pd
import math
import numpy as np
from web_scraping.scraping import main_path
def search_algorithm(keywords):
    search_terms = keywords.split()
    df = pd.read_csv(f"{main_path()}/data/Job_search.csv")
    idf_values = {}
    for term in search_terms:
        term_count = sum(1 for field in df['Job_Name'] if term.lower() in field.lower())
        idf_values[term] = math.log(len(df) / (1 + term_count))
    for term in search_terms:
        tfidf_scores = []
        for field in df['Job_Name']:
            word_count = sum(1 for word in field.split() if word.lower() == term.lower())
            tfidf_scores.append(word_count / len(field.split()) * idf_values[term])
        df[term] = np.array(tfidf_scores)
    df['TF-IDF'] = df[search_terms].sum(axis=1)
    df = df.sort_values(by='TF-IDF', ascending=False)
    df = df[df['TF-IDF'] != 0]
    result_df = df.iloc[:, :4]
    return result_df