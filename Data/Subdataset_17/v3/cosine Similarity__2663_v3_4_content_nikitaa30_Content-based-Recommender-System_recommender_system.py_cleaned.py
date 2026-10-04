import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def load_dataset(path):
    return pd.read_csv(path)
def create_tfidf_matrix(data, column):
    vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    return vectorizer.fit_transform(data[column]), vectorizer
def compute_cosine_similarities(tfidf_matrix):
    return linear_kernel(tfidf_matrix, tfidf_matrix)
def build_similarity_results(data, cosine_similarities):
    results = {}
    for idx, row in data.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], data['id'][i]) for i in similar_indices]
        results[row['id']] = similar_items[1:]
    return results
def get_item_description(data, item_id):
    return data.loc[data['id'] == item_id]['description'].values[0]
def recommend_similar_items(data, results, item_id, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to '{get_item_description(data, item_id)}'...")
    print("-------")
    recommendations = results[item_id][:num_recommendations]
    for score, recommended_item_id in recommendations:
        print(f"Recommended: '{get_item_description(data, recommended_item_id)}' (score: {score:.4f})")
def main():
    dataset_path = "/home/nikita/Downloads/sample-data.csv"
    data = load_dataset(dataset_path)
    tfidf_matrix, _ = create_tfidf_matrix(data, 'description')
    cosine_similarities = compute_cosine_similarities(tfidf_matrix)
    similarity_results = build_similarity_results(data, cosine_similarities)
    print('Processing complete!')
    recommend_similar_items(data, similarity_results, item_id=11, num_recommendations=5)
if __name__ == "__main__":
    main()