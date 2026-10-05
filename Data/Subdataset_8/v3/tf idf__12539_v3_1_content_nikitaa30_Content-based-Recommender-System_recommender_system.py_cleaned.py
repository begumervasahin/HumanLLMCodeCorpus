import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
dataset_path = "/home/nikita/Downloads/sample-data.csv"
data = pd.read_csv(dataset_path)
tfidf_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
similar_items_dict = {}
for idx, row in data.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-1][::-1]
    similar_items = [(cosine_similarities[idx][i], data.loc[i, 'id']) for i in similar_indices if i != idx]
    similar_items_dict[row['id']] = similar_items
print('Recommendation process completed!')
def get_item_description(item_id):
    return data.loc[data['id'] == item_id, 'description'].iloc[0].split(' - ')[0]
def recommend_similar_items(item_id, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to '{get_item_description(item_id)}'...")
    print("-------")
    recommendations = similar_items_dict.get(item_id, [])
    for idx, (similarity_score, similar_item_id) in enumerate(recommendations[:num_recommendations], start=1):
        print(f"{idx}. {get_item_description(similar_item_id)} (score: {similarity_score:.4f})")
recommend_similar_items(item_id=11, num_recommendations=5)