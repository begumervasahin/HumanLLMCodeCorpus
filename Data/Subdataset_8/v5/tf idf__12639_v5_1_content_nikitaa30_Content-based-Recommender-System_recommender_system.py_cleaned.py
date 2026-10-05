import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def load_data(file_path):
    return pd.read_csv(file_path)
def initialize_tfidf_vectorizer():
    return TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
def compute_cosine_similarities(tfidf_matrix):
    return linear_kernel(tfidf_matrix, tfidf_matrix)
def build_similar_items_dict(data, cosine_similarities):
    similar_items_dict = {}
    for idx, row in data.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], data['id'][i]) for i in similar_indices]
        similar_items_dict[row['id']] = similar_items[1:]
    return similar_items_dict
def get_item_description(data, item_id):
    return data.loc[data['id'] == item_id]['description'].tolist()[0].split(' - ')[0]
def recommend_similar_items(item_id, num_recommendations, data, similar_items_dict):
    print("Recommending {} products similar to {}...".format(num_recommendations, get_item_description(data, item_id)))
    print("-------")
    recommended_items = similar_items_dict[item_id][:num_recommendations]
    for rec in recommended_items:
        print("Recommended: {} (score:{})".format(get_item_description(data, rec[1]), rec[0]))
def main():
    data_path = "/home/nikita/Downloads/sample-data.csv"
    data = load_data(data_path)
    tfidf_vectorizer = initialize_tfidf_vectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['description'])
    cosine_similarities = compute_cosine_similarities(tfidf_matrix)
    similar_items_dict = build_similar_items_dict(data, cosine_similarities)
    print('Recommendation system setup is complete!\n')
    recommend_similar_items(item_id=11, num_recommendations=5, data=data, similar_items_dict=similar_items_dict)
if __name__ == "__main__":
    main()