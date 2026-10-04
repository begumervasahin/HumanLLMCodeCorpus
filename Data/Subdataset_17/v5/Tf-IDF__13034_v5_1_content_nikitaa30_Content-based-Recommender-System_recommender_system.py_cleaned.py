import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
ds = pd.read_csv("/home/nikita/Downloads/sample-data.csv")
tfidf_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(ds['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
similarity_results = {}
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]
    similarity_results[row['id']] = similar_items[1:]
print('Similarity computation done!')
def get_item_description(item_id):
    return ds.loc[ds['id'] == item_id]['description'].tolist()[0].split(' - ')[0]
def recommend_similar_items(item_id, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to {get_item_description(item_id)}...")
    print("-------")
    recommendations = similarity_results[item_id][:num_recommendations]
    for score, similar_item_id in recommendations:
        print(f"Recommended: {get_item_description(similar_item_id)} (score: {score})")
recommend_similar_items(item_id=11, num_recommendations=5)